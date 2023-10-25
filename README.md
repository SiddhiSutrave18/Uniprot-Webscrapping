# Uniprot-Webscraping
## Requirements
1. An IDE to run python script: Pycharm(preferred),Vscode, Jupyternotebook, etc.
2. Chrome Driver ( https://www.youtube.com/watch?v=jQW2fjgUJrY&pp=ygUfY2hyb21lZHJpdmUgaW5zdGFsbGF0aW9uIGxhdGVzdA%3D%3D )
## Description:
The code contains 
## Scripts:
### 0.DATA_ANALYSIS.py
The code is primarily used for filtering and processing data related to proteins and organisms, and the resulting output can be further analyzed or used as input for another script (presumably 'Strain_Search_MODIFIED_CODE.py') to perform additional tasks.  
This code is recommended if the Input csv file contains rows more than 10k so as to shorten the time for running the next code (1.Strain_Search_MODIFIED_CODE.py).  
If the input file contains rows more than 10k, the script will take approximately 24hrs depending upon the speed of your computer.
  
**Input**  
Input the file downloaded from uniprot in csv format-------- [Input0]
NOTE (Minimum requirement of csv file downloaded from the Uniprot website): the input csv must contain the columns: 'Entry', 'Protein Names' & 'Organism'  
**Output1**  
[Check_File.csv]This file likely contains the entries that passed the previous filtration steps.  
**Output2**  
  
### 0.DATA_ANALYSIS.py  
This Python script utilizes the Selenium web automation library to scrape information from the UniProt website. The code's main purpose is to extract information about the "Strain" associated with UniProt entries specified by their UniProt IDs (accession numbers). Here's a description of the code's main components and steps:
  
1. Importing Libraries:  
   - The script starts by importing the necessary libraries: Selenium for web automation, Pandas for data manipulation, and time for adding delays.  
  
2. Initializing WebDriver:  
   - A WebDriver instance for Google Chrome is created using the specified ChromeDriver executable path.  
  
3. Reading UniProt IDs:  
   - The code reads a CSV file ('Output0.csv') that presumably contains UniProt Entry IDs. These IDs are stored in a list named `IDs`.  
  
4. Batch Processing:  
   - To avoid overloading the UniProt website, the script processes the UniProt IDs in batches. The `batch_size` variable determines the number of IDs to process in each batch.  
  
5. Scraping Strain Information:  
   - For each batch, the script iterates through the UniProt IDs.  
   - It navigates to the UniProt website, enters the UniProt ID into the search box, and clicks the search button.  
   - It waits for elements containing links to proteomes (organisms) to load on the page.  
   - For each proteome link, it follows the link to the organism's page.  
   - It extracts the "Strain" information from the page by searching for a specific XPath element.  
  
6. Error Handling:  
   - If any errors occur during the web scraping process (e.g., "Strain" information not found), the script appends a default value ("Strain Number not found") to the 'Strain' column.  
  
7. Adding Delays:  
   - The script includes a 10-second delay between batches to avoid overloading the UniProt website.  
  
8. Quitting WebDriver:  
   - After processing all UniProt IDs, the WebDriver instance is closed.  
  
9. Data Post-Processing:  
   - The collected strain information is stored in a list of dictionaries, with each dictionary containing an 'Entry' (UniProt ID) and 'Strain' key-value pair.  
   - The 'Strain' values are split by '/' to handle multiple strain names and are then stacked into separate rows using Pandas' `explode` function.  
   - Leading and trailing whitespace is stripped from the 'Strain' values.  
   - Duplicate rows are removed based on 'Entry' and 'Strain' columns.  
   - The resulting DataFrame is saved to a new CSV file named 'Output1.csv,' which likely contains the extracted strain information.  
  
In summary, this code automates the process of fetching strain information associated with UniProt IDs from the UniProt website and then organizes this data into a structured output file for further analysis or integration into a larger biological or bioinformatics research workflow.  
