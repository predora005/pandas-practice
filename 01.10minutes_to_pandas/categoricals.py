# coding: utf-8

import numpy as np
import pandas as pd

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    df = pd.DataFrame( {
        "id": range(1,7), 
        "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e'],
        "categorical_grade": pd.Categorical(['a', 'b', 'b', 'a', 'a', 'e'])
    } )
    
    print("------------------------------------------------------------------")
    print("df:")
    print(df)

    print("------------------------------------------------------------------")
    print("Convert the raw grades to a categorical data type.")
    print("----------------------------------------")
    df['grade'] = df['raw_grade'].astype('category')
    print("df['raw_grade'].astype('category')")
    print(df['grade'])
    
    print("------------------------------------------------------------------")
    print("Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!).")
    print("----------------------------------------")
    df['grade'].cat.categories = ['very good', 'good', 'very bad']
    print("[df['grade'].cat.categories = ['very good', 'good', 'very bad']]")
    print(df['grade'])
    
    print("------------------------------------------------------------------")
    print("Reorder the categories and simultaneously add the missing categories")
    print("(methods under Series .cat return a new Series by default).")
    print("----------------------------------------")
    df['grade'] = df['grade'].cat.set_categories(
        ['very bad', 'bad', 'medium', 'good', 'very good'])
    print(df['grade'])
    
    print("------------------------------------------------------------------")
    print("Sorting is per order in the categories, not lexical order.")
    print("----------------------------------------")
    df_sorted = df.sort_values(by='grade')
    print("[df.sort_values(by='grade')]")
    print(df_sorted)
    
    print("------------------------------------------------------------------")
    print("Grouping by a categorical column also shows empty categories.")
    print("----------------------------------------")
    df_grouped = df.groupby('grade').size()
    print("[df.groupby('grade').size()]")
    print(df_grouped)
    