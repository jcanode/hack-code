import pandas as pd
import regex as re
import numpy as np
# import matplotlib.pyplot as plt
# import nltk

def network_parse(filename):
    # read in data file
    df = pd.read_csv(filename)
    # add network columns
    df["network"] = ""
    # set up regex 
    regex_1 = re.compile(r'case 1')
    regex_2 =  re.compile(r'Case 2')
    regex_3 = re.compile(r'Case 3')
    print(df.columns.name)
    for i in range(len(df)):
        data = df.iloc[i].value
        # check case  1-
        if regex_1.findall(data):
            print('case 1')
            # append case 1 to column
            if regex_2.findall(data):
                print("case 2")
            # 
                df.network[i] = '2'
            elif regex_3.findall(data):
                df.network[i] = '3'
        else:
            print('not case 1')
            df.network[i] = 'network ' # todo, parse out specific network
    return df
network_parse("df1.csv")