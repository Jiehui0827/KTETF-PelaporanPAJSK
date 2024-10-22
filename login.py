import streamlit as st
# from streamlit_gsheets import GSheetsConnection
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials


def user_login():
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

    # # Connect to your Google Sheet
    # conn = st.connection("gsheets", type=GSheetsConnection, ttl=10)
    # credentials = conn.read(worksheet="Student")
    df_credential = pd.DataFrame(worksheet.get_all_records())
    print(df_credential)
    df_credential["password"] = df_credential["password"].astype(str)
    # print(df_credential["password"])
    # st.dataframe(df_credential)

    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Function to check credentials
    def check_credentials(username, password):
        valid_user = df_credential[(df_credential["username"] == username) & (df_credential["password"] == password)]
        return not valid_user.empty

    if not st.session_state.logged_in:
        with st.form("Credentials"):
            st.markdown('## Login to KTETF - Pengiraan PAJSK')
            st.markdown('---')
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button("Log in")

            if submit_button:
                if check_credentials(username, password):
                    st.session_state.logged_in = True
                    st.success("Logged in successfully!")
                    st.cache_data.clear()
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
                    st.cache_data.clear()
        
            st.markdown('---')
            st.markdown('Copyright © 2024 JYJH. All Rights Reserved')

    if st.session_state.logged_in:
        return True

    return False