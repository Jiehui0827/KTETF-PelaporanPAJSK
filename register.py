import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Page config
st.set_page_config(
    page_title='Register',
    page_icon='abacus',
    layout='wide',
)

##connect google sheets
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]

skey = st.secrets["gcp_service_account"]
credentials = Credentials.from_service_account_info(
    skey,
    scopes=scopes,
)
client = gspread.authorize(credentials)

url="https://docs.google.com/spreadsheets/d/1SQtxbYvBVwdWcyeUUkhqHetn9QlJkwCrAhTsE1bPQYw/edit?usp=sharing"
sh = client.open_by_url(url)
sheet = sh.worksheet('Student')

st.title("Register")
with st.form("Register form"):
    st.write("Register KOKU Details")
    name=st.text_input("Name")
    kelas=st.text_input("Class")

    new_row = [name,kelas]

    submitted = st.form_submit_button("Submit")
    if submitted:
        sheet.append_row(new_row)