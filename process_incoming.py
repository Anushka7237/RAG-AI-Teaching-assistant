import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import requests
import json
from openai import OpenAI
from config import api_key

client=OpenAI(api_key=api_key)

df=joblib.load('embeddings.joblib')

def create_embedding(text_list):
    r=requests.post("http://localhost:11434/api/embed",json=
                {
                    "model":"bge-m3",
                    "input":text_list
                })
    embedding=r.json()['embeddings']
    return embedding


def inference(prompt):
    print("thinking...")
    r=requests.post("http://localhost:11434/api/generate",json=
                {
                    "model":"llama3.2",
                    "prompt":prompt,
                    "stream":False
                })
    response=r.json()
    # print(response)
    return response

# def inference_openai(prompt):
#     response = client.responses.create(
#     model="gpt-5",
#     input=prompt
#     )
#     return response.output_text
    
incoming_query=input("Ask your Question??")
question_embedding=create_embedding([incoming_query])[0]

# print(question_embedding)

#find the similarities of question_embedding with other embedding
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding'].shape))

similarities=cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
# print(similarities)
# print(similarities.argsort())
top_result=3
max_indx=similarities.argsort()[::-1][0:top_result]
# print(max_indx)

new_df=df.loc[max_indx]
# print(new_df[['number','title','text']])


prompt = f'''I am teaching React. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:
{new_df[['number','title','start','end','text']].to_json(orient='records')}
----------------------------------------------------------------------------------
{incoming_query}
User asked this question related to the video chunks, you have to answer where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course
'''

with open("prompt.txt","w") as f:
    f.write(prompt)
    
response=inference(prompt)
# response=inference_openai(prompt)

with open("response.txt","w") as f:
    print (response['response'])
    #also response is present in response.txt file 
    f.write(response['response'])
    

# for index,item in new_df.iterrows():
#     print(index,item['title'],item['number'],item['text'],item['start'],item['end'])