# CodeAlpha_WebScraping
CodeAlpha Data Analytics Internship - Task 1 Web Scraping using Python, BeautifulSoup and Pandas
# CodeAlpha Data Analytics Internship

## Task 1: Web Scraping Using Python

### Project Overview

This project was completed as part of the CodeAlpha Data Analytics Internship Program.

The objective of this project is to extract book information from a website using Python web scraping techniques and store the collected data in a CSV file for further analysis.

---

## Objective

The main objectives of this project are:

* Collect data automatically from a website.
* Extract useful information from HTML pages.
* Store scraped data in a structured format.
* Export the data into a CSV file for analysis.

---

## Technologies Used

* Python
* Requests
* BeautifulSoup (BS4)
* Pandas
* Visual Studio Code (VS Code)

---

## Website Used

**Books To Scrape**

https://books.toscrape.com

This website is specifically designed for practicing web scraping techniques.

---

## Data Extracted

The following information was collected for each book:

* Book Title
* Price
* Rating
* Availability Status

---

## Working Process

### Step 1: Send HTTP Request

The Requests library is used to connect to the website and retrieve the webpage content.

### Step 2: Parse HTML Content

BeautifulSoup is used to parse and navigate the HTML structure of the webpage.

### Step 3: Extract Required Data

The scraper extracts:

* Title
* Price
* Rating
* Availability

from each book listed on the webpage.

### Step 4: Store Data

The extracted data is stored in a Pandas DataFrame.

### Step 5: Export to CSV

The final dataset is exported as:

**books_data.csv**

---

## Sample Output

| Title                | Price  | Rating | Availability |
| -------------------- | ------ | ------ | ------------ |
| A Light in the Attic | £51.77 | Three  | In Stock     |
| Tipping the Velvet   | £53.74 | One    | In Stock     |
| Soumission           | £50.10 | One    | In Stock     |

---

## Results

* Successfully scraped book data from the website.
* Extracted multiple records automatically.
* Stored data in CSV format.
* Demonstrated practical web scraping and data collection skills.

---

## Applications of Web Scraping

* Market Research
* Price Monitoring
* Competitor Analysis
* Data Collection
* Business Intelligence
* Data Analytics

---

## Future Enhancements

* Scrape data from multiple pages.
* Store data in a database.
* Automate data collection using scheduling tools.
* Perform Exploratory Data Analysis (EDA).
* Build interactive dashboards using Power BI or Tableau.

---

## Conclusion

This project demonstrates the use of Python, Requests, BeautifulSoup, and Pandas for web scraping. The scraper successfully extracts book information from a website and stores it in a structured CSV file. This project showcases practical data collection techniques widely used in Data Analytics and Business Intelligence.

---

## Author

**Charan Kaniganti**

CodeAlpha Data Analytics Intern
