import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def check (dict_, key, string_):
    """" this function replace words for hey words in a list"""
    for i in dict_[key]:
        if i in string_:
            return key

def replace (df,column,source,output):
    """" this function will replace an unwanted word in a column 
    and will imput the desired nomenclature"""
    s = source
    o = output
    c = column
    df[c] = df[c].replace([s],[o])
    pass

def dropna_colum (df,column):
    """"this function will dropna in a specific column
    and return the dataframe displaying random 5 lines"""
    df = df.dropna(subset=["Column"])
    return df.sample(5)

def columnnullcount (df):
    """this function returns a list of all the columns 
    and the count of null values """
    return df.isnull().sum()

def get_html(url):
    """this function take the url and check for responce,
    grab the content and use beautifulsoup to turn into html"""
    import requests
    from bs4 import BeautifulSoup
    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, "html.parser")
    return soup

def select_html(html,tag):
    """this function take the soup from get_html and 
    use it to find all tags and class within that code
    and will return a sample on position 3"""
    from bs4 import BeautifulSoup
    sample = html.select(tag)
    return sample