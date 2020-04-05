#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    ldata = load()
    sepal = ldata[:,0]
    petal = ldata[:,2]
    return(scipy.stats.pearsonr(sepal,petal)[0])

def correlations():
    ldata = load()
    matrix = np.corrcoef(ldata, rowvar=False)
    return (matrix)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
