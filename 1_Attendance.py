import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Page config
st.set_page_config(
    page_title='Attendance',
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

url="https://docs.google.com/spreadsheets/d/1gF7ylb6X-ouZtH205kJa0Kvj182Nu1DsVLPAi0fM_Co/edit?usp=sharing"
sh = client.open_by_url(url)
stjohn = sh.worksheet('StJohn')
pingpong = sh.worksheet('PingPong')

st.title("Attendance")
stjohn_df = pd.DataFrame(stjohn.get_all_records())
stjohn_df['total'] = stjohn_df.sum(axis=1)
st.write("St John Attendance")
st.dataframe(stjohn_df, hide_index=True)

st.divider()

pingpong_df = pd.DataFrame(pingpong.get_all_records())
pingpong_df['total'] = pingpong_df.sum(axis=1)
st.write("Ping Pong Attendance")
st.dataframe(pingpong_df, hide_index=True)
