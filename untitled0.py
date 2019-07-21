# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:30:17 2019

@author: kvp_1_000
"""

import pandas as pd
def test():
    lst = [[1,2,3],[1,2,3],[1,2,3]]
    df = pd.DataFrame(lst, columns=['first','second','third'])
    #df.to_html('filename.html')
    print(df.to_html())