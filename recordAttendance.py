import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import datetime

# Page config
st.set_page_config(
    page_title='Attendance',
    page_icon='abacus',
    layout='wide',
)

st.title("Record Attendance")

st.subheader(datetime.date.today())

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

kelab_option = st.selectbox("Choose which Persatuan/Kelab", ("StJohn","PingPong"),
                                                    index=None,
                                                    placeholder="Select your Persatuan/Kelab")


recordsheet = sh.worksheet(kelab_option)

data_df = pd.DataFrame(
    {
        "studentList" : ["Student1", "Student2", "Student3"],
        # "Attend": [True, False, True],
        "Attend Today": [True] * 3
    }
)



st.data_editor(
    data_df,
    column_config={
        "Attend Today": st.column_config.CheckboxColumn(
            "Attend or not?",
            help="Select his/her **attendance**",
            default=False,
        )
    },
    disabled=["studentList"],
    hide_index=True,
    use_container_width=True
)

# recordsheet.append_row(new_row)

