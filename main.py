from bs4 import BeautifulSoup
import requests

url = ''
conn = requests.get(url,headers={"Accept-Language":"en-US,en;q=0.9"})
soup = BeautifulSoup(conn.text, "html.parser")

all = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [i["href"] for i in all]
all_address = [i.getText().strip() for i in all]

all1 = soup.select(".PropertyCardWrapper")
all_price = [price.get_text().replace("/mo", "").split("+")[0].strip() for price in all1 if "$" in price.text]

print("Collecting Data......")