import pandas as pd

df_wine = pd.read_csv("C:\\Users\\carol\\github-classroom\\CodeYou-Data-Jan2024\\wine-reviews-exercise-kykikimora\\data\\winemag-data-130k-v2.csv")

df_wine = df_wine.rename(columns={"country": "Country"})

reviews_per_country = pd.DataFrame(df_wine.Country.value_counts())

avgpts = pd.DataFrame(df_wine.groupby("Country").points.mean().round(1))

combined = pd.concat([reviews_per_country,avgpts],axis=1,join="inner")

combined.to_csv("data\\reviews-per-country.csv")

#issue with permissions; unable to read in csv file from git repository.
#issues with calling in pandas module
