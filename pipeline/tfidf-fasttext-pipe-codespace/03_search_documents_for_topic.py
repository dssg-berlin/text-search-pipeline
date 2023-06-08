import json, gensim
import pandas as pd

with open("../tf_idf_vectors.json") as infile:
    json_data = json.load(infile)

print(len(json_data), json_data[-1].keys())

df = pd.read_json("data-assets/obdachlos_sample_anon.json.zip")

ddf = df.rename(columns={"md5_file": "md5_file", "text": "fulltext"})
print(ddf.head())

url_md5 = pd.read_json("data-assets/url_md5_sample.json.zip")
print(url_md5.head())
urls = list(url_md5.url)

print("Loading FastText language model which takes a while...")
ft = gensim.models.fasttext.load_facebook_vectors('model.bin')
print("Finished loading language model")
print("Starting predefined search...")

def search(term, similarity_threshold):
    for i, doc in enumerate(json_data):
        for keyword in doc.keys():
            similarity = ft.similarity(term, keyword)
            if similarity>similarity_threshold:
                print(i, round(similarity, 3), keyword, end=" ")
                md5 = ddf.md5_file.iloc[i]
                if any(url_md5.md5.eq(md5)):
                    print(url_md5[url_md5.md5==md5].url.values[0], end=" ")
                print()

if __name__ == "__main__":
    search("Wärmebus", 0.7)
    search("Wärmehalle", 0.8)
    search("Kältehilfe", 0.8)
    search("Kältebus", 0.62)
    search("Obdachlosenheim", 0.8)
    search("Obdachlosenunterkunft", 0.9)
    search("obdachlosen", 0.9)
    search("kleiderkammern", 0.8)
    search("tafel", 0.8)