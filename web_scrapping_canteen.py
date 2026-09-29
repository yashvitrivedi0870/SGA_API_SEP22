import requests
from bs4 import BeautifulSoup
import pandas as pd

url="http://10.11.20.24:5001/menu"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

item = soup.find_all("li")

data=[]
for item in item:
    text = item.text.strip()
    name, price= text.split("-")
    data.append({"Item":name, "Price":price})

df=pd.DataFrame(data)

print(df)

df.to_csv("canteen_menu.csv", index=False)
print("\nSaved to canteen_menu.csv")
