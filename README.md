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

