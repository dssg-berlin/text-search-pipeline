This pipeline is part of a DSSG Berlin e.V. volunteering project that ran from 2022 to 2023 to support an aid organisation uncovering the different services sub-organisations offer to help homeless people. This public repository is for demonstration purpose and does not include all project outputs.

# Pipeline

![image](https://github.com/dssg-berlin/obdachlosenhilfe/assets/8211411/3965e70a-cb05-4268-9e73-ef84d74b801c)

## Thanks for the Contributions
Contribute to add your name to the list of contributors.

* [your GitHub name](https://www.github.com/)
* [SamerEssa-IT](https://github.com/SamerEssa-IT)
* [Saif-Mandour](https://github.com/Saif-Mandour)
* [mediasittich](https://github.com/mediasittich)
* [JOPloume](https://github.com/JOPloume)
* [bsenst](https://github.com/bsenst)

## Instructions to run the Pipeline

### Create a GitHub Codespace for this Repository

Create and open a codespace with 8 GB RAM on the repository main branch

![image](https://github.com/dssg-berlin/obdachlosenhilfe/assets/8211411/5dd73c3f-656c-4cfb-bd41-161c439a68d5)

This will open a new tab in your browser

![image](https://github.com/dssg-berlin/obdachlosenhilfe/assets/8211411/d25af6a4-23f6-40ca-ac50-f746f8a9b3de)

Go to https://github.com/codespaces

![image](https://github.com/dssg-berlin/obdachlosenhilfe/assets/8211411/b34afc00-5afd-486f-9ff8-f19b13471126)

Change the codespace machine type to a machine with a memory of 8 GB RAM

![image](https://github.com/dssg-berlin/obdachlosenhilfe/assets/8211411/2e34b6dd-bf2d-4186-a32f-8295ea57b806)

For the change of the machine type to become active stop the codespace ...

https://docs.github.com/en/codespaces/developing-in-codespaces/stopping-and-starting-a-codespace#stopping-a-codespace

... and restart it

https://docs.github.com/en/codespaces/developing-in-codespaces/stopping-and-starting-a-codespace#restarting-a-codespace

Open the tab of codespace inside your browser and enter the following commands into the terminal of your codespace

![image](https://github.com/dssg-berlin/obdachlosenhilfe/assets/8211411/351b65fd-12f3-4edf-9649-e58fe4060432)

### Run the Pipeline

Install dependencies

`pip install -r pipeline/tfidf-fasttext-pipe-codespace/pipeline_requirements.txt`

Download fasttext vector model provided by deepset.ai

`wget https://s3.eu-central-1.amazonaws.com/int-emb-fasttext-de-wiki/20180917/model.bin`

Create and save keywords for each document using TF-IDF, this will also download the sample anonymized dataset and the sklearn TF-IDF vectorizer

`python -W ignore pipeline/tfidf-fasttext-pipe-codespace/02_extract_keywords.py`

Run text search with predefined terms and cosine similarity cutoff

`python pipeline/tfidf-fasttext-pipe-codespace/03_search_documents_for_topic.py`

### Licenses

FastText under [Creative Commons Attribution-Share-Alike License 3.0](https://creativecommons.org/licenses/by-sa/3.0/), as described in P. Bojanowski*, E. Grave*, A. Joulin, T. Mikolov, [Enriching Word Vectors with Subword Information](https://arxiv.org/abs/1607.04606) and supplied by [https://www.deepset.ai/german-word-embeddings](https://www.deepset.ai/german-word-embeddings).
