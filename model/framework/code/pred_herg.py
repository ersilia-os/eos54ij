import sys
from bs4 import BeautifulSoup
import requests
import pandas as pd


import warnings
warnings.filterwarnings('ignore')


url = 'http://predherg.labmol.com.br/predict'

df_predictions = pd.DataFrame(columns=['SMILES','potential_cardiotoxic_plus_confidence','strong_or_extrem_confidence','noncardiotoxic_neg_confidence','applicability_domain','ad_value','ad_limit'])

# Using readlines()
input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()
  
for input_smiles in Lines:
    input_smiles = input_smiles.strip()
    payload = { 'smiles' : input_smiles }
    r = requests.post(url, data = payload)
    soup = BeautifulSoup(r.text, features = 'html.parser')
    Table = soup.find('table')


    d = Table.text.split('\n')
    d = [name for name in d if name.strip()]
    predictions = [x.strip(' ') for x in d]
    predictions.pop(3)


    ad = predictions[5].split()[0]

    if ad == 'Yes':
        ad = 1
    else:
        ad = 0
    
    if predictions[-1] == 'Not applicable':
        new_row = {
                'SMILES': input_smiles,
                'potential_cardiotoxic_plus_confidence': None,
                'strong_or_extrem_confidence': None,
                'noncardiotoxic_neg_confidence': float(predictions[4].rstrip("%"))/100,
                'applicability_domain': ad,
                'ad_value': predictions[5].split()[2],
                'ad_limit': predictions[5].split()[6]
             }
    else:
        new_row = {
                'SMILES': input_smiles,
                'potential_cardiotoxic_plus_confidence': float(predictions[4].rstrip("%"))/100,
                'strong_or_extrem_confidence': float(predictions[7].rstrip("%"))/100,
                'noncardiotoxic_neg_confidence': None,
                'applicability_domain': ad,
                'ad_value': predictions[5].split()[2],
                'ad_limit': predictions[5].split()[6]
             }
#append row to the dataframe
    df_predictions = df_predictions.append(new_row, ignore_index=True)
    
df_predictions.to_csv(sys.argv[2], index=False)
