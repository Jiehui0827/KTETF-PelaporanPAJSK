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
username = "Student1"

st.title("Register")
with st.form("Register form"):
    st.write("Register KOKU Details")
    name=st.text_input("Name", value=username, disabled=True)

    kelas_option = st.selectbox(
    "Class",
    ("B25-BIO", "B25-PHY", "B25-EK1", "B25-EK2", "B25-PK1", "B25-PK2", "B25-PP1", "B25-PP2", "B25-BM1", "B25-KMK", "B25-SEJ", 
     "B25-SSB", "B25-SSP", "B25-SVS"),
    index=None,
    placeholder="Select your class",
    )

    race_option= st.selectbox("Race", ("Malay", "Chinese", "Indian", "Others"),index=None,placeholder="Select your race",)

    gender_option = st.selectbox("Gender",("Male", "Female"), index=None, placeholder="Select your gender")

    kelab_option = st.selectbox("Persatuan/Kelab", ("Kelab Malaysiaku", "Kelab Hospitaliti", "Persatuan Seni Visual", 
                                                    "Persatuan Bahasa", "Persatuan STEM", "Kelab Kerjaya", "Kelab Muzik dan Kebudayaan", "Kelab Pencinta Alam"),
                                                    index=None,
                                                    placeholder="Select your Persatuan/Kelab")
    
    uniform_option = st.selectbox("Badan Beruniform", ("Pengakap Kelana", "Pandu Puteri Klover", "St. John Ambulans", "Pasukan Institusi Pertahanan Awam (PISPA)", 
                                                       "Pengakap Udara"),
                                                       index=None,
                                                       placeholder="Select your Badan Beruniform")
    
    sukan_option = st.selectbox("Sukan/Permainan", ("Kelab Futsal", "Bola Tampar", "Kelab Bola Jaring", "Bola Keranjang", "Ping Pong", "Kelab Catur", "Kelab Frisbee", 
                                                    "Bola Baling", "Boling Tenpin"),
                                                    index=None,
                                                    placeholder="Select your Sukan/Permainan")

    new_row = [name,kelas_option,race_option,gender_option, kelab_option, uniform_option, sukan_option]

    submitted = st.form_submit_button("Submit")
    if submitted:
        sheet.append_row(new_row)