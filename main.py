# import defs
import numpy as np
import pandas as pd
import openpyxl
import lxml
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import yfinance as yf
from plotly import graph_objects as go
from sklearn.preprocessing import LabelEncoder


def df_del(first_df, second_df, first_df_column, second_df_column):
    for var in first_df[first_df_column]:
        if var in second_df[second_df_column]:
            pass
        else:
            if var in first_df[first_df_column]:
                first_df = first_df.drop(first_df.loc[first_df[first_df_column] == var].index)
            else:
                pass
    print(first_df)


sdf = pd.read_csv("master.csv")
hdf = pd.read_csv("DataForTable2.1.csv")

# sdf = sdf.drop(columns=["HDI for year", "generation"]).dropna()
# hdf = hdf.drop(hdf["Country name"])
# print(hdf)

df_del(hdf, sdf, "Country name", "country")
df_del(sdf, hdf, "country", "Country name")

