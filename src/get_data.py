# we need to read the parameters
# and need to process it
## and return it to some location,in our case location is raw data

import os
import pandas as pd 
import yaml
import argparse


def read_param(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
        return config 


def get_data(config_path):
    config=read_param(config_path)
    #print(config)
    data_path=config["data_source"]["s3_source"]
    df=pd.read_csv(data_path, sep=",",encoding='utf-8')
    return df



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="param.yaml")
    parsing_method=args.parse_args()
    data=get_data(config_path=parsing_method.config)