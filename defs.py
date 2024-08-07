import pandas as pd

sdf = pd.read_csv("master.csv")
hdf = pd.read_excel("DataForTable2.1.xls")


def df_del(first_df, second_df, first_df_column, second_df_column):
    for var in first_df[first_df_column]:
        if var in second_df[second_df_column]:
            pass
        else:
            if var in first_df[first_df_column]:
                first_df = first_df[first_df[first_df_column] != var]
                # first_df = first_df.drop(first_df.loc[first_df[first_df_column] == var].index)
            else:
                pass
    print(first_df)

