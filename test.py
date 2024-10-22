import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]

skey = st.secrets["gcp_service_account"]
credentials = Credentials.from_service_account_info(
    skey,
    scopes=scopes,
)
client = gspread.authorize(credentials)

url="https://docs.google.com/spreadsheets/d/1A6ASlg_Cidng86cmDaYaNTaA0-1-HzRw7EU1cd1P-f4/edit?usp=sharing"
sh = client.open_by_url(url)
worksheet = sh.worksheet('Student')

new_row = ['Value1', 'Value2', 'Value3']
worksheet.append_row(new_row)
print(worksheet.row_values(2))
worksheet.update("A3",[["john","yes","blabla","test","123"]])


# # Perform SQL query on the Google Sheet.
# # Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
# def load_data(url, sheet_name="Student"):
    
#     df = pd.DataFrame(sh.worksheet(sheet_name).get_all_records())
#     return df

# link=""
# print(load_data(link))

