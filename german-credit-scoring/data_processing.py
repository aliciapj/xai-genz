import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


def one_hot_encoder(df, nan_as_category = False):
    original_columns = list(df.columns)
    categorical_columns = [col for col in df.columns if df[col].dtype == 'object']
    df = pd.get_dummies(df, columns= categorical_columns, dummy_na= nan_as_category, drop_first=True)
    new_columns = [c for c in df.columns if c not in original_columns]
    return df, new_columns


def preprocess_german_credit_scoring(df: pd.DataFrame) -> pd.DataFrame:
    
    # Valores nulos
    df['Saving accounts'] = df['Saving accounts'].fillna('no_inf')
    df['Checking account'] = df['Checking account'].fillna('no_inf')
    
    # Nuevas variables
    interval = (18, 25, 35, 60, 120)

    cats = ['Student', 'Young', 'Adult', 'Senior']
    # df["Age_cat"] = pd.cut(df.Age, interval, labels=cats)
    
    # Valores categóricos
    df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
    df['Housing'] = LabelEncoder().fit_transform(df['Housing'])
    df['Saving accounts'] = LabelEncoder().fit_transform(df['Saving accounts'])
    df['Checking account'] = LabelEncoder().fit_transform(df['Checking account'])
    df['Purpose'] = LabelEncoder().fit_transform(df['Purpose'])
    df['Risk'] = LabelEncoder().fit_transform(df['Risk'])
    # df['Age_cat'] = LabelEncoder().fit_transform(df['Age_cat'])
    
    # Selección de variables
    df = df.drop([
        'Unnamed: 0', 
        # 'Age', 
    ], 1,)
    
    return df
