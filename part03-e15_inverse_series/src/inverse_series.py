import pandas as pd

def inverse_series(s):
    return pd.Series(s.index.values, s.values)

def main():
    series = pd.Series(['a','b','c'])
    print(series)
    print(inverse_series(series))

if __name__ == "__main__":
    main()
