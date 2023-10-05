# Contributing to corpus-es 📚✨

First and foremost, thank you for contributing to `corpus-es`! This repository aims to become a centralized location for NLP datasets, especially focused on the Spanish language & co (e.g., Catalan, Quechua). By sharing your dataset, you are helping the entire NLP community grow! 🚀

## Step-by-step Guide

### 1. 🍴 Fork the repository

Before making any changes, make sure you have a [GitHub account](https://github.com/). Then, start by forking the `corpus-es` repository. This will create a copy of the repository in your own GitHub account, allowing you to make changes without affecting the main repository.

### 2. 🧐 Decide which type of dataset you want to add

You can add any dataset you find interesting for the community if it is related to Spanish, LATAM or Spain.

Have a look at the [issues](https://github.com/somosnlp/corpus-es/issues). If the dataset you want to add is not on the list, create a new issue. Once you have decided which dataset to work on, comment on the corresponding issue to let everybody know it's in progress and avoid duplicated efforts.

There are three ways to contribute to the dataset list `corpus-es`:

| Type of Dataset    | Description                                                                                                                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existing Dataset   | Datasets natively in Spanish, you just have to add them to the list. Besides the link to the dataset, try to add all the information you can find about the dataset.                                                                      |
| Translated Dataset | Datasets translated from another language to Spanish. You can use tools like Google Translate, DeepL, OpenAI, etc. Example scripts for translation can be found in the [scripts](./scripts/) folder.                                      |
|                    |
| Original Dataset   | Datasets created from scratch involving processes like scrapping, cleaning, etc. They might be a combination of various sources or have undergone significant transformations. Make sure to upload your methodology and the scripts used. |

If you have translated a corpus or created one from scratch, join https://huggingface.co/hacktoberfest-corpus-es (clic on "request to join this org") and upload it. We also encourage you to upload already existent datasets available in other platform (if the license allows it!). Tu upload a dataset to the hub, follow these [instructions](https://huggingface.co/docs/datasets/create_dataset).

### 3. 📂 Add your dataset to the repo

1. Clone your forked repository to your local machine. Use the following command:

```bash
git clone https://github.com/<your_username>/corpus-es.git
```

2. Navigate to the `datasets` folder:

```bash
cd datasets
```

3. Create a new folder for your dataset. The name of the folder should be the name of the dataset. If it's an original dataset, choose a descriptive name related to the dataset content or source.

```bash
mkdir <your_dataset_name>
```

Include in the folder all the creation, cleaning and/or translation scripts.

5. Add a `README.md` in the folder with info about your dataset. Each README is divided into two sections: a YAML header and a body.

- Copy the [header template](./datasets/nuevo_dataset.md) and fill the information
- The Hugging Face team has already designed very complete Dataset Cards so we'll use their [template for the body](https://github.com/huggingface/datasets/blob/main/templates/README_guide.md).
- We want to focus on the quality of the datasets so if you provide info regarding the evaluation of the dataset you will be rewarded with extra points:
  - Calculate the perplexity distribution
  - Include a detailed description of the size besides "GB" or "number of tokens", e.g. distribution of the length of the sentences or documents
  - Evaluate the bias of the dataset
  - The more details the better!

### 4. 📄 Add your dataset to the table [datasets.csv](./datasets.csv)

Add a new line to the table and fill the corresponding information.

If you use VS Code, we recommend you to use extensions like Rainbow CSV or a CSV editor to simplify this task.

### 5. 🔄 Submit a Pull Request

1. Commit your changes:

```bash
git add .
git commit -m "add <existent/translated/original> dataset: <your_dataset_name>"
```

2. Push your changes to your forked repository:

```bash
git push
```

3. Create a `New Pull Request` providing a descriptive title: **"Add existent/translated/original dataset: YourDatasetName"** and explain why your dataset is a valuable addition to `corpus-es`. Once everything looks good, submit your pull request!

4. Your contribution will then be reviewed by the maintainers. Be prepared to address any comments and change requests.

5. Once everything is in order, it will be merged into the main repository. Thanks again for helping expand the `corpus-es` collection! 🥳🎉

If you have any questions, feel free to open an issue or contact us on [Discord](https://discord.com/invite/my8w7JUxZR).
