# Contributing to corpus-es 📚✨

First and foremost, thank you for considering contributing to `corpus-es`! This repository aims to become a centralized location for NLP datasets, especially focused on the Spanish language. By sharing your dataset, you are helping the entire NLP community grow. 🚀

## Step-by-step Guide

### 1. Fork the Repository 🍴

Before making any changes, make sure you have a [GitHub account](https://github.com/). Then, start by forking the `corpus-es` repository. This will create a copy of the repository in your own GitHub account, allowing you to make changes without affecting the main repository.

### 2. Decide on the Dataset Type 🧐

There are three primary categories of datasets in `corpus-es`:

- **Existing Spanish datasets**: These are datasets natively in the Spanish language.
  
- **Translated datasets**: These datasets originally existed in another language and were translated into Spanish.
  
- **Curated datasets**: Handpicked or modified datasets that might be a combination of various sources or have undergone significant transformations.

Ensure you've read the specific instructions for each dataset type in the repository's documentation to make sure your dataset aligns with the criteria.

### 3. Add Your Dataset 📂

1. Clone your forked repository to your local machine. Use the following command:
```bash
git clone https://github.com/[Your-Username]/corpus-es.git
```
2. Navigate to the `datasets` folder:

```bash
cd datasets
```

3. Create a new folder for your dataset. The name of the folder should be descriptive and related to your dataset's content or source.

```bash
mkdir [your-dataset-name]
```

4. Add your dataset to the [csv](./datasets_list.csv)

5. Add a `README.md` in your dataset folder. This should contain:
- A brief description of the dataset.
- The source of the dataset, and how to download it.
- If it's a translated dataset, mention the original language and the translation method/tool used. If you used a script, include the script.
- Any other relevant metadata or notes

### 4. Submit a Pull Request 🔄

1. Commit your changes:

example commit message:
```bash
git add .
git commit -m "Added [Your-Dataset-Name] to the [Dataset-Type] category."
```
2. Push your changes to your forked repository:

```bash
git push 
```


3. Create a `New Pull Request`.

4. Provide a descriptive title and detailed comment about your dataset and why it's a valuable addition to `corpus-es`.

5. Once everything looks good, submit your pull request!

---

Your contribution will then be reviewed by the maintainers, and if everything is in order, it will be merged into the main repository. Thanks again for helping expand the `corpus-es` collection! 🥳🎉

If you have any questions, feel free to open an issue or contact the maintainers.
