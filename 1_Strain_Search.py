from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

website = 'https://www.uniprot.org/'
path = r'C:\Windows\chromedriver.exe'
driver = webdriver.Chrome()

# Making a list of the Uniprot IDs to make up a column for Strain
ndf = pd.read_csv('SN_MlaA_organism.csv').copy()
IDs = list(ndf['Entry'])

batch_size = 50  # You can adjust the batch size as needed
num_batches = len(IDs) // batch_size + 1

Strain = []

for i in range(num_batches):
    batch_start = i * batch_size
    batch_end = (i + 1) * batch_size
    current_batch = IDs[batch_start:batch_end]

    for id in current_batch:
        try:
            driver.get(website)
            Search_element = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/div/main/div[1]/div[1]/div/section/form/div[2]/input')
            Search_element.send_keys(id)

            SearchClick = driver.find_element(By.XPATH,
                                              '//*[@id="root"]/div[1]/div/main/div[1]/div[1]/div/section/form/button')
            SearchClick.click()

            wait = WebDriverWait(driver, 10)
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/proteomes/")]'))
            )

            # Extract the text from the href attributes of these elements
            links = [element.get_attribute('href') for element in elements]

            # Click on each link to open the webpages
            for link in links:
                driver.get(link)

                # Wait for the element to be present and visiblez
                wait = WebDriverWait(driver, 10)

                strain_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='decorated-list-item__title tiny' and text()='Strain']/following-sibling::div[@class='decorated-list-item__content']")))
                # Get the text content from the element
                strain_text = strain_element.text
                Strain.append({'Entry': id, 'Strain': strain_text})

        except:
            Strain.append({'Entry': id, 'Strain': "Strain Number not found"})

    # Add a delay between batches to avoid overloading the server
    time.sleep(10)

driver.quit()

df = pd.DataFrame(Strain)
df['Strain'] = df['Strain'].str.split('/')

# Create a new DataFrame by stacking the split values into separate rows
df = df.explode('Strain')

# Strip any leading/trailing whitespace
df['Strain'] = df['Strain'].str.strip()

# Reset the index
df = df.drop_duplicates(subset=['Entry', 'Strain'])
df.reset_index(drop=True, inplace=True)

merged_df = pd.merge(ndf, df, on='Entry', how='outer')

#Enter the filename for output file:-
merged_df.to_csv('SN_MlaA_with_Strain_modified.csv')