import pandas as pd
import os
import argparse
import time
from googletrans import Translator
import tqdm
import requests

def load_dataset(dataset_path: str) -> None:
    """
    The load dataset function will act as a function to to the following actions:
    1. download json, convert it into a csv
    2. add a column which is: 'ready_for_translation' = 'yes' or 'no' | default no
    3. add a column which is: 'translated' = 'yes' or 'no' | default no
    4. create a folder for the new translation of the dataset
    5. open csv files of the target translation files, but empty with the same columns as the original dataset

    Args:
        dataset_path (str): path to the dataset

    Returns: None
    """
    # load json
    # split the dataset path into folder and file name
    folder = dataset_path.split('/')[0]
    file_name = dataset_path.split('/')[1]
    csv_path = dataset_path[:-6] + '.csv'  # .jsonl -> .csv
    # create a translated_folder
    translated_folder = folder + '_translated'
    # create a translated_file_name, which will be an empty csv file
    translated_file_name = file_name[:-6] + '_translated.csv'
    # construct the following path for the destination csv: translated_folder/translated_file_name
    translated_file_path = translated_folder + '/' + translated_file_name

    # check if the csv file already exists, if yes, then return the path to the csv file
    if os.path.exists(csv_path):
        print('The csv file already exists.')
    else:
        df = pd.read_json(dataset_path, lines=True)
        # add a column which is: 'ready_for_translation' = 'yes' or 'no' | default no
        df['ready_for_translation'] = 0
        df['translated'] = 0

        # save the dataset as a csv with 2 new columns (processed, translated set to 0)
        df.to_csv(csv_path, index=False)

    # make the translated folder if it doesnt exist
    if not os.path.exists(translated_folder):
        os.makedirs(translated_folder)

    # check if the translated csv file already exists, if yes, then return the path to the csv file
    if os.path.exists(translated_file_path):
        print('The translated csv file already exists.')

    else:
        # create an empty df with the same columns as the original df
        translated_df = pd.DataFrame(columns=df.columns)
        # save the empty df as a csv
        translated_df.to_csv(translated_file_path, index=False)

    return csv_path, translated_file_path


def split_text(content, index):
    """
    Function to split the text content into chunks of less than 400 characters.
    Returns a list of tuples containing the chunked content and corresponding chunk_id.
    """
    chunks = []
    sentences = content.split('.')
    chunk_content = ""
    chunk_number = 0

    for sentence in sentences:
        if len(chunk_content) + len(sentence) < 400:
            chunk_content += sentence + '.'
        else:
            chunk_id = f"{index}_{chunk_number}"
            chunks.append((chunk_content, chunk_id))
            chunk_content = sentence + '.'
            chunk_number += 1

    if chunk_content:
        chunk_id = f"{index}_{chunk_number}"
        chunks.append((chunk_content, chunk_id))

    return chunks


# Group by original_id and concatenate the translations
def concat_translations(group):
    return group.str.cat(sep=' ')


def generate_batches(origin: str, destination: str, columns_for_translation: list):
    """
    Take the dataset, split it into chunks, translate the chunks and then rejoin the dataset
    """
    df = pd.read_csv(origin)

    # adding original_id column and initializing it to the current _id since later we split into chunks and we want to regroup them in order
    df['original_id'] = df['_id']

    translator = Translator()
    translator.raise_Exception = True

    new_rows = []
    for index, row in df.iterrows():
        for column in columns_for_translation:
            content = row[column]
            if len(content) > 400:
                chunks = split_text(content, row['original_id'])
                for chunk_content, chunk_id in chunks:
                    new_row = row.copy()
                    new_row[column] = chunk_content
                    new_row['ready_for_translation'] = 1
                    new_row['_id'] = chunk_id
                    new_rows.append(new_row)
            else:
                row['ready_for_translation'] = 1
                new_rows.append(row)

    # create a new DataFrame with the new rows
    new_df = pd.DataFrame(new_rows)

    # initialize a progress bar and begin translations loop
    with tqdm.tqdm(total=len(new_df)) as pbar:
        for index, row in new_df.iterrows():
            if row['ready_for_translation'] == 1:
                for column in columns_for_translation:
                    try:
                        result = translator.translate(row[column], dest='es')
                        row[column] = result.text
                        time.sleep(0.5)
                        # replace the new df row with the translated row
                        new_df.iloc[index] = row
                    except Exception as e:
                        print(f"Error translating column {column} in row {index}: {e}")
                        row[column] = 'error'
                        time.sleep(0.5)
            pbar.update()

    for column in columns_for_translation:
        new_df[column] = new_df.groupby('original_id')[column].transform(concat_translations)

    new_df.drop_duplicates(subset='original_id', keep='first', inplace=True)

    new_df.loc[new_df['ready_for_translation'] == 1, 'translated'] = 1
    new_df.to_csv(destination, index=False)


def download_and_open_dataset(dataset_name: str):
    # define the dataset you want to download
    url = f"https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{dataset_name}.zip"

    # download the dataset
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # save the dataset
    with open(f"{dataset_name}.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # open the zip folder
    os.system(f"open {dataset_name}.zip")


if __name__ == '__main__':
    # download_and_open_dataset('scidocs') this is only if u havent downloaded one of the retrieval datasets from the beir benchmark

    # the path should be scidocs for example: py translator.py -p 'scidocs/corpus.jsonl'
    # this will translate the corpus.jsonl file
    # you can also choose which columns/key values to translate from the json file

    parser = argparse.ArgumentParser(description="Load a dataset from Hugging Face and add unique IDs if not present.")
    parser.add_argument("-p", "--path", type=str, required=True, help="path to desired json you want to translate")
    parser.add_argument("-c", "--columns", type=list, required=True, help="columns to translate")
    args = parser.parse_args()

    # load dataset
    dataset_path = args.path
    # load the data + generate destination files, return the path to the destination csv
    # import pdb; pdb.set_trace() -> for debugging purposes
    original_csv_path, destinaton_csv_path = load_dataset(dataset_path)
    # check for the max char length from each column and split in a logical way
    generate_batches(origin=original_csv_path, destination=destinaton_csv_path, columns_for_translation=args.columns)
