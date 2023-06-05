# SENTIMENTSCRAPE

# Web Scraping Script

This script performs web scraping on a specific webpage to extract financial news data from multiple tables and save the data into separate CSV files.

## Usage

1. Install the required libraries by running the following command:

   ```shell
   pip install requests pandas beautifulsoup4

Modify the script's URL variable (url) to specify the webpage containing the tables you want to scrape.
Run the script by executing the following command:

```shell
python sentimentscrape.py

After execution, the script will save each table as a separate CSV file in the current directory.
Dependencies

The script requires the following libraries:

requests: Used to send HTTP requests and retrieve the webpage content.
pandas: Used to create DataFrames and save data as CSV files.
beautifulsoup4: Used to parse HTML content and extract table data.
