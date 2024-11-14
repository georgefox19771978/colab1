# analysis.py
import pandas as pd

def load_and_clean_data(url):
    df = pd.read_csv(url)
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    url = "https://example.com/data.csv"
    df = load_and_clean_data(url)
    print(df.head())
    
print("George is here")
