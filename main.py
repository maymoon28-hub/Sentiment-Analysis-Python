import argparse
import pandas as pd
from ingest import ingest
from preprocess import preprocess
from analyse import analyse
from visualise import visualise
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from analyse import label_from_compound


import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    filename="logs/pipeline.log",  #writes to file
    filemode="a"                   
)
logger = logging.getLogger(__name__)






def main(input_file, output_file, plot_path):
    try:
        logger.info(f"Pipeline started with input_file: {input_file}")

    
        for row in ingest(input_file):   #ingest returns comments list
            #print(preprocess(row))
            revised_filtered = preprocess(row) #preprocess
            compound_score = analyse(revised_filtered) #analyse
        
        sia=SentimentIntensityAnalyzer()
        comments=ingest(input_file)
        logger.info("Comments loaded")
        
        df1=pd.DataFrame(comments, columns= ["feedback_text"])
        df1.dropna(subset=["feedback_text"], inplace=True)
        logger.info("Cleaned DataFrame Null Values")
    
        df1["compound"]=df1["feedback_text"].astype(str).apply(lambda row: label_from_compound(sia.polarity_scores(row)["compound"]))
        df1["sentiment"]=df1["feedback_text"].apply(lambda row: sia.polarity_scores(row)["compound"])
        df1.to_csv(output_file,  index=False)
        logger.info(f"Saved csv results into: {output_file}")
    
        # code is excuted well in csv file
        #Visualisee
        visualise(df1, plot_path)
        logger.info(f"Plot saved to: {plot_path}")
            
            
        print('Processing complete.')
        logger.info("Pipeline completed Successfully")
        
    except Exception:
        logger.exception("Pipeline failed due to an unexpected Error")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, help='Path to input jsonl file')
    parser.add_argument('--output_file', required=True, help='Path to save output CSV file')
    parser.add_argument('--plot_path', required=True, help='Path to save sentiment distribution plot png file')
    args = parser.parse_args()
    main(args.input_file, args.output_file, args.plot_path)

""" 
Used only standard python logging. Website referred:
https://www.geeksforgeeks.org/python/difference-between-logging-and-print-in-python/

"""
    
