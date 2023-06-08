import time, json, pickle
import pandas as pd

df = pd.read_json("data-assets/obdachlos_sample_anon.json.zip")

fulltext = list(df.text)

print("len_fulltexts", len(fulltext))

with open("data-assets/vectorizer.pk", "rb") as infile:
    vectorizer = pickle.load(infile)

# https://www.kaggle.com/code/rowhitswami/keywords-extraction-using-tf-idf-method

feature_names = vectorizer.get_feature_names_out()
tf_idf_vectors = []
start = time.time()

def sort_coo(coo_matrix):
    """Sort a dict with highest score"""
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []
    
    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature, score
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

print("Creating keywords using TF-IDF...")

for i, text in enumerate(fulltext):
    text = str(text)
    if i % 10_000 == 0: 
        print(i, round(time.time()-start,0))
        with open('../tf_idf_vectors.json', 'w') as outfile:
            json.dump(tf_idf_vectors, outfile)
    try:
        # generate tf-idf for the given document
        tf_idf_vector = vectorizer.transform([text])

        # sort the tf-idf vectors by descending order of scores
        sorted_items=sort_coo(tf_idf_vector.tocoo())
        
        tf_idf_vectors.append(extract_topn_from_vector(feature_names,sorted_items))
    except Exception as e:
        print(i, text[:30])
        print(e)
        tf_idf_vectors.append([""])

print(i, round(time.time()-start,0))
with open('../tf_idf_vectors.json', 'w') as outfile:
    json.dump(tf_idf_vectors, outfile)

print("len_tf_idf_vectors", len(tf_idf_vectors))
