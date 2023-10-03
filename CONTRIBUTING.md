# Contributing to corpus-es 📚✨

First and foremost, thank you for contributing to `corpus-es`! This repository aims to become a centralized location for NLP datasets, especially focused on the Spanish language & co (e.g., Catalan, Quechua). By sharing your dataset, you are helping the entire NLP community grow! 🚀

## Step-by-step Guide

### 1. Fork the Repository 🍴

Before making any changes, make sure you have a [GitHub account](https://github.com/). Then, start by forking the `corpus-es` repository. This will create a copy of the repository in your own GitHub account, allowing you to make changes without affecting the main repository.

### 2. Decide on the Dataset Type 🧐

There are three primary categories of datasets in `corpus-es`:

| Type of Dataset    | Description                                                                                                                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existing Dataset   | Datasets natively in the Spanish language, you just have to add them to the list. Try to add all the information you can find about the dataset.                                                                                          |
| Translated Dataset | Datasets translated from another language to Spanish. You can use tools like Google Translate, DeepL, OpenAI, etc. Example scripts for translation can be found in the [scripts](./scripts/) folder.                                      |
|                    |
| Original Dataset   | Datasets created from scratch involving processes like scrapping, cleaning, etc. They might be a combination of various sources or have undergone significant transformations. Make sure to upload your methodology and the scripts used. |

If you translate a corpus or create one from scratch, upload it to https://huggingface.co/hacktoberfest-corpus-es. We also encourage you to upload already existent datasets available in other platform (if the license allows it!). Tu upload a dataset to the hub, follow these [instructions](https://huggingface.co/docs/datasets/create_dataset).

### 3. Add Your Dataset 📂

1. Clone your forked repository to your local machine. Use the following command:

```bash
git clone https://github.com/<your_username>/corpus-es.git
```

2. Navigate to the `datasets` folder:

```bash
cd datasets
```

3. Create a new folder for your dataset. The name of the folder should be descriptive and related to your dataset's content or source.

```bash
mkdir <your_dataset_name>
```

Include in the folder all the creation, cleaning and/or translation scripts.

5. Add a `README.md` in your dataset folder:

- Copy the [plantilla](./datasets/nuevo_dataset.md) and fill the information
- Include a brief description of the dataset
- The evaluation of the dataset will be rewarded with extra points:
  - Calculate the perplexity distribution
  - Evaluate the bias of the dataset
- Add any other relevant metadata or notes

### 4. Add your dataset to the table [datasets.csv](./datasets.csv)

Add a new line to the table and fill the corresponding information.

If you use VS Code, we recommend you to use extensions like Rainbow CSV or a CSV editor to simplify this task.

### 5. Submit a Pull Request 🔄

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
