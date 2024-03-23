#!/usr/bin/env python
# coding: utf-8

# In[1]:


def format_columns(df):
    import pandas as pd
    import re
    col_list = df.columns
    col_list = pd.Series(col_list)

    col_list = col_list.apply(lambda i: i.lower())
    col_list = col_list.apply(lambda i: i.replace(' ','_'))
    col_list = col_list.apply(lambda i: re.sub('st', 'state', i) if re.search(r'^st$', i) else i)
    df.columns = col_list 

    return df

