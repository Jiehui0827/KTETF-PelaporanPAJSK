import streamlit as st
from login import user_login

import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Connect to your Google Sheet
conn = st.connection("gsheets", type=GSheetsConnection)

# Create a sample Pandas DataFrame 
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 60, 45],
                   'City': ['New York', 'Los Angeles', 'Chicago']})

# Update GS using sample df
df = conn.update(
     worksheet="worksheet_name",
     data=df,
)


# Page config
st.set_page_config(
    page_title='Pengiraan PAJSK KTETF',
    # page_icon='maths',
    layout='wide',
)

if not user_login(): st.stop()

# Page title
st.title('Pengiraan PAJSK KTETF')
st.markdown('---')

# Page input: [sukan, kelab, uniform]
user_data = {
    'Kehadiran Kelab': [0, 0, 0],
    'Jawatan Kelab': ['', '', ''],
    'Peringkat Kelab': ['', '', ''],
    'Peringkat Pencapaian Kelab': ['', '', ''],
    'Pencapaian Kelab': ['', '', ''],
    'Nama Projek': ['', '', ''],
    'Jawatan Projek': ['', '', ''],
    'Peringkat Projek': ['', '', ''],
    'Ekstra Kurikulum Perkhidmatan': '',
    'Ekstra Kurikulum Anugerah Khas': '',
}

# Constants
JAWATAN_KELAB = {
    'Tiada': 0,
    'Pengerusi': 10,
    'Timbalan Pengerusi / Naib Pengerusi': 8,
    'Setiausaha / Bendahari': 7,
    'Penolong Setiausaha / Penolong Bendahari': 6,
    'Ahli Jawatankuasa': 5,
    'Ahli Aktif': 4,
}

PERINGKAT_KELAB = {
    'Tiada': 0,
    'Kebangsaan': 10,
    'Negeri': 8,
    'Daerah': 6,
    'Sekolah': 4,
}

PENCAPAIAN = {
    'Johan': 0,
    'Naib Johan': -1,
    'Ketiga': -2,
}

PENCAPAIAN_KELAB = {'Tiada': 0} | {
    f'{kelab} - {pencapaian}': start_value + adjust_value 
    for kelab, start_value in list(PERINGKAT_KELAB.items())[1:] 
    for pencapaian, adjust_value in PENCAPAIAN.items()
}

JAWATAN_PROJEK = {
    'Tiada': 0,
    'Pengerusi Projek': 10,
    'Timbalan Pengerusi / Naib Pengerusi / Setiausaha Projek': 9,
    'Bendahari Projek': 8,
    'Penolong Setiausaha / Penolong Bendahari Projek': 7,
    'Ahli Jawatankuasa Projek': 6,
    'Ahli': 5,
}

PERINGKAT_PROJEK = {
    'Tiada': 0,
    'Negeri': 10,
    'Daerah': 8,
    'PTE/KTE': 6,
}

EXTRA_KOKO_PERKHIDMATAN = {
    'Tiada': 0,
    'Ketua Murid / Pengerusi': 10,
    'Penolong Ketua Murid / Timbalan Pengerusi': 8,
    'Pengurusan Utama yang ditubuhkan untuk membantu sekolah/Exco Persatuan Tingkatan Enam/ Pengawas/ Ketua Asrama / BADAR/Ketua PRS/ Pengerusi Badan-Badan Perkhidmatan Sekolah ': 7,
    'Penolong Ketua Asrama/ BADAR/Pengawas Pusat Sumber/ Ahli Lembaga Pengarah Koperasi Sekolah': 6,
    'AJK Utama  Badan-badan Perkhidmatan atau Pengurusan/ Bendahari/ Setiausaha/ Ketua Biro - Asrama/BADAR/ PRS / Pegawas Koperasi/ Ketua Kelas / Ketua Tingkatan': 4,
    'Ahli-ahli J/Kuasa Perkhidmatan dan Sokongan - AJK Kecil Biro / Ketua Bilik / Ketua Dorm /BADAR/Penolong Ketua Kelas / Penolong Ketua Bilik': 3,
}

EXTRA_KOKO_ANUGERAH = {
    'Tiada': 0,
    'Anugerah Remaja Perdana (ARP) Anjuran Kementerian Belia dan Sukan - Emas': 10,
    'Anugerah Remaja Perdana (ARP) Anjuran Kementerian Belia dan Sukan - Perak': 7,
    'Anugerah Remaja Perdana (ARP) Anjuran Kementerian Belia dan Sukan - Gangsa': 5,
    'Anugerah Khas Sukan - Peringkat Kebangsaan': 5,
    'Anugerah Khas Sukan - Peringkat Negeri': 4,
    'Anugerah Khas Sukan - Peringkat Zon/Daerah/Bahagian': 3,
    'Anugerah Khas Sukan - Peringkat Sekolah': 2,
    'Penyertaan Peringkat Antarabangsa - Emas': 5,
    'Penyertaan Peringkat Antarabangsa - Perak': 4,
    'Penyertaan Peringkat Antarabangsa - Gangsa': 3,
    'Penyertaan Peringkat Antarabangsa - Penyertaan': 2,
    'Anugerah-anugerah lain/ Penghargaan Khas Setara - Peringkat Kebangsaan': 5,
    'Anugerah-anugerah lain/ Penghargaan Khas Setara - Peringkat Negeri': 4,
    'Anugerah-anugerah lain/ Penghargaan Khas Setara - Peringkat Zon/Daerah/Bahagian': 3,
    'Anugerah-anugerah lain/ Penghargaan Khas Setara - Penyertaan': 2,
    'Pengakap Raja/ Pandu Puteri Raja': 10,
}

# Logic
tab1, tab2, tab3, tab4 = st.tabs(['SUKAN/PERMAINAN', 'KELAB/PERSATUAN', 'BADAN BERUNIFORM', 'EKSTRA KURIKULUM'])

with tab1:
    col1, col2 = st.columns(2)
    with col1: 
        user_data['Kehadiran Kelab'][0] = st.number_input('Kehadiran Kelab', max_value=20, step=1, key='Kehadiran Kelab 0')
        user_data['Jawatan Kelab'][0] = st.selectbox('Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 0')
        user_data['Peringkat Kelab'][0] = st.selectbox('Peringkat', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 0')
        user_data['Peringkat Pencapaian Kelab'][0] = st.selectbox('Peringkat Pencapaian', options=PENCAPAIAN_KELAB.keys(), key='Peringkat Pencapaian Kelab 0')
    with col2:
        user_data['Nama Projek'][0] = st.text_input('Nama Projek', key='Nama Projek 0')
        user_data['Jawatan Projek'][0] = st.selectbox('Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 0')
        user_data['Peringkat Projek'][0] = st.selectbox('Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 0')

with tab2:
    col1, col2 = st.columns(2)
    with col1: 
        user_data['Kehadiran Kelab'][1] = st.number_input('Kehadiran Kelab', max_value=20, step=1, key='Kehadiran Kelab 1')
        user_data['Jawatan Kelab'][1] = st.selectbox('Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 1')
        user_data['Peringkat Kelab'][1] = st.selectbox('Peringkat', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 1')
        user_data['Peringkat Pencapaian Kelab'][1] = st.selectbox('Peringkat Pencapaian', options=PENCAPAIAN_KELAB.keys(), key='Peringkat Pencapaian Kelab 1')
    with col2:
        user_data['Nama Projek'][1] = st.text_input('Nama Projek', key='Nama Projek 1')
        user_data['Jawatan Projek'][1] = st.selectbox('Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 1')
        user_data['Peringkat Projek'][1] = st.selectbox('Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 1')

with tab3:
    col1, col2 = st.columns(2)
    with col1: 
        user_data['Kehadiran Kelab'][2] = st.number_input('Kehadiran Kelab', max_value=20, step=1, key='Kehadiran Kelab 2')
        user_data['Jawatan Kelab'][2] = st.selectbox('Jawatan Kelab', options=JAWATAN_KELAB.keys(), key='Jawatan Kelab 2')
        user_data['Peringkat Kelab'][2] = st.selectbox('Peringkat', options=PERINGKAT_KELAB.keys(), key='Peringkat Kelab 2')
        user_data['Peringkat Pencapaian Kelab'][2] = st.selectbox('Peringkat Pencapaian', options=PENCAPAIAN_KELAB.keys(), key='Peringkat Pencapaian Kelab 2')
    with col2:
        user_data['Nama Projek'][2] = st.text_input('Nama Projek', key='Nama Projek 2')
        user_data['Jawatan Projek'][2] = st.selectbox('Jawatan Projek', options=JAWATAN_PROJEK.keys(), key='Jawatan Projek 2')
        user_data['Peringkat Projek'][2] = st.selectbox('Peringkat Projek', options=PERINGKAT_PROJEK.keys(), key='Peringkat Projek 2')

with tab4:
    user_data['Ekstra Kurikulum Perkhidmatan'] = st.selectbox('Ekstra Kurikulum Perkhidmatan', options=EXTRA_KOKO_PERKHIDMATAN.keys())
    user_data['Ekstra Kurikulum Anugerah Khas'] = st.selectbox('Ekstra Kurikulum Anugerah Khas', options=EXTRA_KOKO_ANUGERAH.keys())

def get_total(i):

    return (user_data['Kehadiran Kelab'][i] / 20 * 50 + 
        JAWATAN_KELAB[user_data['Jawatan Kelab'][i]] +
        PERINGKAT_KELAB[user_data['Peringkat Kelab'][i]] +
        PENCAPAIAN_KELAB[user_data['Peringkat Pencapaian Kelab'][i]] + 
        JAWATAN_PROJEK[user_data['Jawatan Projek'][i]] + 
        PERINGKAT_PROJEK[user_data['Peringkat Projek'][i]])

st.markdown('---')

# Table Display
st.html(f'''<table style="width: 100%;">
    <tr>
        <th style="border: 1px solid grey; padding: 10px;">ELEMEN</th>
        <th style="border: 1px solid grey; padding: 10px;">ASPEK</th>
        <th style="border: 1px solid grey; padding: 10px;" colspan=2>SUKAN/PERMAINAN</th>
        <th style="border: 1px solid grey; padding: 10px;" colspan=2>KELAB/PERSATUAN</th>
        <th style="border: 1px solid grey; padding: 10px;" colspan=2>BADAN BERUNIFORM</th>
        <th style="border: 1px solid grey; padding: 10px;">EKSTRA KURIKULUM</th>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;" rowspan=4>PENGLIBATAN</td>
        <td style="border: 1px solid grey; padding: 10px;">Kehadiran</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Kehadiran Kelab'][0]} / 20</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Kehadiran Kelab'][0] / 20 * 50}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Kehadiran Kelab'][1]} / 20</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Kehadiran Kelab'][1] / 20 * 50}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Kehadiran Kelab'][2]} / 20</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Kehadiran Kelab'][2] / 20 * 50}</td>
        <td style="border: 1px solid grey; padding: 10px;" rowspan=4>{user_data['Ekstra Kurikulum Perkhidmatan']}</td>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;">Jawatan</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Jawatan Kelab'][0]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_KELAB[user_data['Jawatan Kelab'][0]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Jawatan Kelab'][1]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_KELAB[user_data['Jawatan Kelab'][1]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Jawatan Kelab'][2]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_KELAB[user_data['Jawatan Kelab'][2]]}</td>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;">Peringkat</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Kelab'][0]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_KELAB[user_data['Peringkat Kelab'][0]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Kelab'][1]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_KELAB[user_data['Peringkat Kelab'][1]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Kelab'][2]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_KELAB[user_data['Peringkat Kelab'][2]]}</td>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;">Pencapaian</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Pencapaian Kelab'][0]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PENCAPAIAN_KELAB[user_data['Peringkat Pencapaian Kelab'][0]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Pencapaian Kelab'][1]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PENCAPAIAN_KELAB[user_data['Peringkat Pencapaian Kelab'][1]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Pencapaian Kelab'][2]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PENCAPAIAN_KELAB[user_data['Peringkat Pencapaian Kelab'][2]]}</td>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;" rowspan=3>PENGURUSAN PROJEK</td>
        <td style="border: 1px solid grey; padding: 10px;">Nama Projek</td>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>{user_data['Nama Projek'][0]}</td>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>{user_data['Nama Projek'][1]}</td>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>{user_data['Nama Projek'][2]}</td>
        <td style="border: 1px solid grey; padding: 10px;" rowspan=3>{user_data['Ekstra Kurikulum Anugerah Khas']}</td>
    </tr>    
    <tr>
        <td style="border: 1px solid grey; padding: 10px;">Jawatan</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Jawatan Projek'][0]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_PROJEK[user_data['Jawatan Projek'][0]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Jawatan Projek'][1]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_PROJEK[user_data['Jawatan Projek'][1]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Jawatan Projek'][2]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{JAWATAN_PROJEK[user_data['Jawatan Projek'][2]]}</td>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;">Peringkat</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Projek'][0]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_PROJEK[user_data['Peringkat Projek'][0]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Projek'][1]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_PROJEK[user_data['Peringkat Projek'][1]]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{user_data['Peringkat Projek'][2]}</td>
        <td style="border: 1px solid grey; padding: 10px;">{PERINGKAT_PROJEK[user_data['Peringkat Projek'][2]]}</td>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>SKOR</td>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>{get_total(0)}</td>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>{get_total(1)}</td>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>{get_total(2)}</td>
        <td style="border: 1px solid grey; padding: 10px;">{max(
            EXTRA_KOKO_PERKHIDMATAN[user_data['Ekstra Kurikulum Perkhidmatan']],
            EXTRA_KOKO_ANUGERAH[user_data['Ekstra Kurikulum Anugerah Khas']],
        )}</td>
    </tr>
    <tr>
        <td style="border: 1px solid grey; padding: 10px;" colspan=2>JUMLAH SKOR (%)</td>
        <td style="border: 1px solid grey; padding: 10px;" colspan=7>{sum(
            sorted([get_total(0), get_total(1), get_total(2)], reverse=True)[:2]
        ) / 2 + max(
            EXTRA_KOKO_PERKHIDMATAN[user_data['Ekstra Kurikulum Perkhidmatan']],
            EXTRA_KOKO_ANUGERAH[user_data['Ekstra Kurikulum Anugerah Khas']],
        )}</td>
    </tr>
</table>
''')

st.markdown('---')
st.markdown('Copyright © 2024 JYJH. All Rights Reserved')