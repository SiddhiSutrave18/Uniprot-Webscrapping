# Uniprot-Webscraping
## Requirements
1. An IDE to run python script: Pycharm(preferred),Vscode, Jupyternotebook, etc.
2. Chrome Driver ( https://www.youtube.com/watch?v=jQW2fjgUJrY&pp=ygUfY2hyb21lZHJpdmUgaW5zdGFsbGF0aW9uIGxhdGVzdA%3D%3D )
## Description:
The code contains 
## Scripts:
### 0.DATA_ANALYSIS.py
The code is primarily used for filtering and processing data related to proteins and organisms, and the resulting output can be further analyzed or used as input for another script ('Strain_Search_MODIFIED_CODE.py') to perform additional tasks.  
This code is recommended if the Input csv file contains rows more than 10k so as to shorten the time for running the next code (1.Strain_Search_MODIFIED_CODE.py).  
If the input file contains rows more than 10k, the script will take approximately 24hrs depending upon the speed of your computer.
  
**Input**  
Input the file downloaded from uniprot in csv format-------- [Input0.csv]
_NOTE (Minimum requirement of csv file downloaded from the Uniprot website): the input csv must contain the columns: 'Entry', 'Protein Names' & 'Organism'  _
**Output1**  
The code creates a separate CSV file containing only the 'Entry' column data and saves it as 'Output0.csv.' This listing file could be used as input for a subsequent code named 'Strain_Search_MODIFIED_CODE.py.'---------[Output0.csv]  
**Output2**  
[Check_File.csv]This file likely contains the entries that passed the previous filtration steps. 
  
**Code Description**  
1. Importing the necessary library:
   - The code begins by importing the Pandas library and giving it the alias 'pd.'

2. Loading the input CSV data:
   - The code reads an input CSV file named 'Input0.csv' (downloaded from the Uniprot website) into a Pandas DataFrame and makes a copy of it.

3. Filtering by Organism:
   - The code calculates the count of unique values in the 'Organism' column and stores this in the 'organism_counts' Series.
   - It then filters the DataFrame to keep only those entries where the organism name appears more than once. This is done to eliminate entries with unique organism names.

4. Filtering by Protein Names:
   - The code further filters the DataFrame to exclude entries where the 'Protein names' column contains the substring 'EC.' Entries with 'ec' in their protein names are removed.

5. Lowercasing Protein Names:
   - The code applies a lowercase transformation to the 'Protein names' column, but the result is not saved back to the DataFrame. It seems to be a redundant operation as it doesn't modify the DataFrame in place.

6. Keyword-Based Filtration:
   - The code specifies a keyword string containing several terms separated by the '|' symbol.
   - It filters the DataFrame to keep only those entries where the 'Protein names' column contains one of these specified keywords.

7. Saving the Output:
   - The code saves the filtered DataFrame to a CSV file named 'Check_File.csv.' This file likely contains the entries that passed the previous filtration steps.

8. Creating an Entry Listing File:
   - The code creates a separate CSV file containing only the 'Entry' column data and saves it as 'Output0.csv.' This listing file could be used as input for a subsequent code named 'Strain_Search_MODIFIED_CODE.py.'

The code is primarily used for filtering and processing data related to proteins and organisms, and the resulting output can be further analyzed or used as input for another script (presumably 'Strain_Search_MODIFIED_CODE.py') to perform additional tasks.
    
### 1.Strain_Search_MODIFIED_CODE.py  
This Python script utilizes the Selenium web automation library to scrape strain names from the UniProt website. The code's main purpose is to extract information about the "Strain" associated with UniProt entries specified by their UniProt IDs (accession numbers).
  
**Input**  
Give the input file of previous code--------[Output0.csv]  
OR   
You can directly provide input file as it is downloaded from the Uniprot website for desired gene name.  
NOTE (Minimum requirement of csv file downloaded from the Uniprot website): the input csv must contain the columns: 'Entry'

**Output**  
You will finally have a modified version of your csv file which will have an additional column 'Strain' with the corresponding strains of the given 'Entry'---------------[Output1.csv]  
  
**Code Description**  
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
