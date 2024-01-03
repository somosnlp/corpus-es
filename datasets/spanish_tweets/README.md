---
- `name`: spanish_tweets
- `corpus_link`: https://huggingface.co/datasets/pysentimiento/spanish-tweets
- `languages`:
    - es
    - en
    - pt
- `countries`:
    - Spain
    - Mexico
    - Argentina
    - Colombia
    - Peru
    - Venezuela
    - Latin America
- `tasks`:
  - language modeling
- `subtasks`:
- `domains`:
  - social media
- `contributor_name`: Juan Manuel Pérez
- `contributor_affiliation`: Universidad de Buenos Aires
- `download_script`: https://github.com/pysentimiento/spritzer-tweets
- `creation_script`: https://github.com/pysentimiento/spritzer-tweets
- `cleaning_script`: https://github.com/pysentimiento/spritzer-tweets
---

# spanish-tweets

## A big corpus of tweets for pretraining embeddings and language models


## Dataset Description

- **Homepage**: https://github.com/pysentimiento/robertuito
- **Paper**: [RoBERTuito: a pre-trained language model for social media text in Spanish](https://aclanthology.org/2022.lrec-1.785/)
- **Point of Contact:** jmperez (at) dc.uba.ar

### Dataset Summary

A big dataset of (mostly) Spanish tweets for pre-training language models (or other representations).

### Supported Tasks and Leaderboards

Language Modeling

### Languages

Mostly Spanish, but some Portuguese, English, and other languages.

## Dataset Structure


### Data Fields

- *tweet_id*: id of the tweet
- *user_id*: id of the user
- *text*: text from the tweet

## Dataset Creation

The full process of data collection is described in the paper. Here we roughly outline the main points:

- A Spritzer collection uploaded to Archive.org dating from May 2019 was downloaded
- From this, we only kept tweets with language metadata equal to Spanish, and mark the users who posted these messages.
- Then, the tweetline from each of these marked users was downloaded.


This corpus consists of 622M tweets from around 432K users.

Please note that we did not filter tweets from other languages, so you might find English, Portuguese, Catalan and other languages in the dataset (around 7/8% of the tweets are not in Spanish)

### Citation Information

```
@inproceedings{perez-etal-2022-robertuito,
    title = "{R}o{BERT}uito: a pre-trained language model for social media text in {S}panish",
    author = "P{\'e}rez, Juan Manuel  and
      Furman, Dami{\'a}n Ariel  and
      Alonso Alemany, Laura  and
      Luque, Franco M.",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.785",
    pages = "7235--7243",
    abstract = "Since BERT appeared, Transformer language models and transfer learning have become state-of-the-art for natural language processing tasks. Recently, some works geared towards pre-training specially-crafted models for particular domains, such as scientific papers, medical documents, user-generated texts, among others. These domain-specific models have been shown to improve performance significantly in most tasks; however, for languages other than English, such models are not widely available. In this work, we present RoBERTuito, a pre-trained language model for user-generated text in Spanish, trained on over 500 million tweets. Experiments on a benchmark of tasks involving user-generated text showed that RoBERTuito outperformed other pre-trained language models in Spanish. In addition to this, our model has some cross-lingual abilities, achieving top results for English-Spanish tasks of the Linguistic Code-Switching Evaluation benchmark (LinCE) and also competitive performance against monolingual models in English Twitter tasks. To facilitate further research, we make RoBERTuito publicly available at the HuggingFace model hub together with the dataset used to pre-train it.",
}
```