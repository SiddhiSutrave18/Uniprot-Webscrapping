import requests
import re
import pandas as pd
def fetch_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return None

# Function to extract the first line for a given protein ID
def extract_first_line_for_protein(data, protein_id):
    extracted_lines = {}
    lines = data.splitlines()
    current_protein_id = None

    for line in lines:
        if "/protein_id=" in line:
            current_protein_id = line.split("=")[1].strip('"\n')
        elif current_protein_id == protein_id and "CDS             " in line:
            extracted_lines[protein_id] = line

    return extracted_lines.get(protein_id, "First line not found for the specified protein ID.")

# The protein ID to search for
target_protein_id = "B4E628"

url = "http://getentry.ddbj.nig.ac.jp/getentry/na/JXCQ01000008"  # Replace with the actual URL

data = fetch_text_from_url(url)

# Initialize lists to store protein IDs before and after the target
protein_ids_before = []
protein_ids_after = []

# Use regular expressions to find protein IDs
protein_ids = re.findall(r'/protein_id="([^"]+)"', data)

# Find the index of the target protein ID
try:
    target_index = protein_ids.index(target_protein_id)
except ValueError:
    print(f"Target protein ID '{target_protein_id}' not found.")
    exit()

# Get the 5 protein IDs before and after the target
if target_index >= 5:
    protein_ids_before = protein_ids[target_index - 5:target_index]
protein_ids_after = protein_ids[target_index + 1:target_index + 6]

# Print the results
print("Proteins UPSTREAM:", protein_ids_before)
print("Proteins DOWNSTREAM :", protein_ids_after)

# Extract the first line for the specified protein IDs
print('LOCATION FOR TARGET Protein ID:')
for protein_id in [target_protein_id] :
    extracted_line = extract_first_line_for_protein(data, protein_id)
    print(f"Location of {protein_id}:\n{extracted_line}")

print('LOCATION FOR Proteins UPSTREAM:')
for protein_id in protein_ids_before:
    extracted_line = extract_first_line_for_protein(data, protein_id)
    print(f"Location of {protein_id}:\n{extracted_line}")

print('LOCATION FOR Proteins DOWNSTREAM:')
for protein_id in protein_ids_after:
    extracted_line = extract_first_line_for_protein(data, protein_id)
    print(f"Location of {protein_id}:\n{extracted_line}")

# Create a list of dictionaries to hold the data
data_list = []

# Add data for target protein
data_list.append({"Protein ID": target_protein_id, "Location": extract_first_line_for_protein(data, target_protein_id)})

# Add data for proteins upstream
for protein_id in protein_ids_before:
    data_list.append({"Protein ID": protein_id, "Location": extract_first_line_for_protein(data, protein_id)})

# Add data for proteins downstream
for protein_id in protein_ids_after:
    data_list.append({"Protein ID": protein_id, "Location": extract_first_line_for_protein(data, protein_id)})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Print the DataFrame
print(df)
df.to_csv("SN_MlaC_colored_Up_Down.csv")