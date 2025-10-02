# %% [markdown]
# # inflation.ipynb
# 
# CSV file with CPI (Consumer Price Index) found at: https://datahub.io/core/cpi-us

# %%
import sys
sys.path.append("..")

import pandas as pd
from reader import generic_reader

# Function to read in CSV file and return cpi_by_year dictionary
def read_cpi_by_year(filename):
    
    # Read CSV file into dataframe
    df_cpi = generic_reader.read_csv_file_to_data_frame(filename)

    # Ensure Date is datetime type
    df_cpi['Date'] = pd.to_datetime(df_cpi['Date'])

    # Extract Year
    df_cpi['Year'] = df_cpi['Date'].dt.year

    # Group by Year and calculate average CPI
    df_cpi = df_cpi.groupby('Year')['Index'].mean().reset_index()

    # Convert to a Python dictionary where key='Year' and value='Index'
    cpi_by_year = dict(zip(df_cpi['Year'], df_cpi['Index']))
    
    return cpi_by_year


# Function to convert USD amount from one year to another year
def convert_usd(original_amount, original_year, new_year, cpi_by_year):
    if original_year not in cpi_by_year:
        raise ValueError(f"CPI data not available for original_year: {original_year}")
    if new_year not in cpi_by_year:
        raise ValueError(f"CPI data not available for new_year: {new_year}")
    
    cpi_original = cpi_by_year[original_year]
    cpi_new = cpi_by_year[new_year]

    new_amount = original_amount * (cpi_new / cpi_original)

    return new_amount



