import pandas
import glob
import os

# path to csv files in data folder
dataPath = os.path.join('data', '*.csv')
csvFiles = glob.glob(dataPath)
allData = []

for file in csvFiles:
    data = pandas.read_csv(file)
    data = data[data["product"] == "pink morsel"]
    data["price"] = data["price"].str.replace('$', '').astype(float)
    data["quantity"] = data["quantity"].astype(float)
    data["sales"] = data["quantity"] * data["price"]
    data = data[["sales" , "date" , "region"]]
    allData.append(data)

result = pandas.concat(allData, ignore_index=True)
result["sales"] = result["sales"].apply(lambda x: f"${x:.2f}")
result.to_csv("combinedSales.csv", index=False)