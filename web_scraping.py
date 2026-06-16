import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send Request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Empty list
data = []

# Extract Data
for book in books:

    title = book.h3.a["title"]

    price = book.find(
        "p",
        class_="price_color"
    ).text

    rating = book.p["class"][1]

    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    data.append([
        title,
        price,
        rating,
        availability
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Title",
        "Price",
        "Rating",
        "Availability"
    ]
)

# Save CSV
df.to_csv(
    "books_data.csv",
    index=False
)

print("Web Scraping Completed Successfully")