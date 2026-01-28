import os
import whisper
import json

model=whisper.load_model("large-v2")

audios=os.listdir("audios")

for audio in audios:
    # print(audio)
    number=audio.split("_")[0]
    title=audio.split("_")[1][:-4]
    print(number,title)
    # result = model.transcribe(audio=f"audios/13_Sample Video.mp3",
    result = model.transcribe(audio=f"audios/{audio}",
                            language="hi",
                            task="translate",
                            word_timestamps=False
    )
    chunks=[]
    for segment in result["segments"]:
        chunks.append({"number":number,"title":title,"start":segment["start"],"end":segment["end"],"text":segment["text"]})
    
    chunk_with_meta_data={"chunks":chunks,"text":result["text"]}
    
    with open(f"json/{audio}.json","w") as f:
        json.dump(chunk_with_meta_data,f)