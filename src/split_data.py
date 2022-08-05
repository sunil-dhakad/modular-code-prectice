import os
import argparse
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from get_data import read_param

def split_and_saved(config_path):
    config=read_param(config_path)
    test_data_path=config["split_data"]["test_path"]
    train_data_path=config["split_data"]["train_path"]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    test_size=config["split_data"]["test_size"]
    random_state=config["base"]["random_state"]

    df=pd.read_csv(raw_data_path,sep=",", encoding="utf-8")
    train,test=train_test_split(df,test_size=test_size,random_state=random_state)
    train.to_csv(train_data_path, sep=",", encoding="utf-8")
    test.to_csv(test_data_path, sep=",",  encoding="utf-8")

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="param.yaml")
    parsing_method=args.parse_args()
    split_and_saved(config_path=parsing_method.config)
