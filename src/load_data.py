import os
from get_data import read_param,get_data
import argparse

def load_and_save(config_path):
    config=read_param(config_path)
    df=get_data(config_path)
    new_columns=[col.replace(" ","_") for col in df.columns]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,sep=",",index=False,header=new_columns)


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="param.yaml")
    parsing_method=args.parse_args()
    load_and_save(config_path=parsing_method.config)
