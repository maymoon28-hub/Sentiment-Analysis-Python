# ingest
#import json
import time
#def ingest(filename, chunk_size=100):
#    with open (filename, "r" ) as f:
#        buffer = []
#        for line in f:
#            buffer.append(json.loads(line))
#            if len(buffer)==chunk_size:
#                yield buffer
#                buffer=[]
#                time.sleep(1)
#                #print(buffer)
#        if buffer:
#            yield buffer
            #print(buffer)

import time
import pandas as pd
def ingest(filename, chunk_size=100):
    df=pd.read_json(filename, lines=True)
    comments=[]
    for idx, row in enumerate(df['text']):
        #print(idx+1,":", row)
        comments.append(row)
    time.sleep(1) #simulate time delay
    return comments
    

