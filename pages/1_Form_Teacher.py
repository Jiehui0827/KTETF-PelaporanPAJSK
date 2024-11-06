import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Page config
st.set_page_config(
    page_title='Form Teacher',
    page_icon='abacus',
    layout='wide',
)

if st.button("Log out", use_container_width=True):
    st.session_state.logged_in = False  # Reset the logged_in state
    st.rerun()  # Refresh the page to show the login form again

st.title("Form Teacher Class KOKU Attendance")
st.subheader("B25-BIO")

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

url="https://docs.google.com/spreadsheets/d/1gF7ylb6X-ouZtH205kJa0Kvj182Nu1DsVLPAi0fM_Co/edit?usp=sharing"
sh = client.open_by_url(url)
sheet = sh.worksheet('Classtest')

df = pd.DataFrame(sheet.get_all_records())
st.dataframe(df, use_container_width=True, hide_index=True)