import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np
from helper import DataHelper
from css_helper import load_css
import time
import os
import requests
import base64
from io import BytesIO
from PIL import Image

# Predict URLs constant
BASE_URL = os.getenv('BASE_URL')
MB_PRIDICT_ENDPOINT = "mb/predict"
PL_PREDICT_ENDPOINT = "pl/predict"
NC_PREDICT_ENDPOINT = "newcar/predict"
TRUCK_PREDICT_ENDPOINT = "truck/predict"

predict_url = ""
# Seting up header
st.set_page_config(page_title='JIVF Credit Score AI Demo',
                   page_icon='💰', layout='wide')
# Load CSS from the helper file
st.markdown(load_css(), unsafe_allow_html=True)
st.markdown('<h1 class="title">JIVF Credit Score Analysis</h1>',
            unsafe_allow_html=True)
# Add the image between title and caption
st.image('app/header_1.png', use_column_width=True)
# Caption
st.caption('Made by GMO')
# Add markdown content with reduced margin
st.markdown("""
    <div class="custom-markdown">
        This is a Proof of Concept (POC) demo showcasing the application of AI in JIVF to enhance the approval rate for loan applications across the following categories:
        Motorbike (MB), Personal Loan (PL), New Car, and Truck. The purpose of this demo is to simulate the process of entering customer information, where the AI model will return a Score of Default Probability along with the key factors influencing that score.
        This application is designed for demonstration purposes only and aims to highlight how AI can assist in improving credit evaluation processes.
    </div>
    """, unsafe_allow_html=True)
# Title
st.markdown('<h2 class="title">APPLICATION FORM</h2>', unsafe_allow_html=True)
# Center the radio selection of selecting product to middle screen.
_, center, _ = st.columns([1, 3, 1])
with center:
    loan_type = st.radio('Select the Loan type:', options=[
                         'Personal Loan', 'Motobike', 'New Car', 'Truck'], horizontal=True)

# Auto generate input form base on the radio "loan_type"
# The form have a container with multiple expanders to display group input field by category.


def display_form(data):

    st.markdown(f"## {data['title']}:")
    with st.container(height=400, border=True):
        cols = st.columns(4)
        for idx, field in enumerate(data['fields']):
            col = cols[idx % 4]
            input_type = field['input_type']
            key = field['key']
            default_value = field['value']
            if input_type == 'text':
                col.text_input(f"{field['label']}",
                               value=default_value, key=key)
            if input_type == 'number':
                col.number_input(
                    f"{field['label']}",
                    value=float(default_value),     
                    key=key
                )


if loan_type == 'Personal Loan':
    predict_url = BASE_URL + PL_PREDICT_ENDPOINT
    with st.expander("Personal Information", expanded=True):
        display_form(DataHelper().get_personal_data())
    with st.expander("Thông tin khoản vay", expanded=True):
        display_form(DataHelper().get_pl_data())
    with st.expander("Thông tin đại lý", expanded=False):
        display_form(DataHelper().get_dealer_data())
    with st.expander("Financial Information", expanded=False):
        display_form(DataHelper().get_financail_data())
    with st.expander("Insurance Information", expanded=False):
        display_form(DataHelper().get_insurance_data())
    with st.expander("Thông tin khách hàng bổ xung", expanded=False):
        display_form(DataHelper().get_address_data())
    with st.expander("Additional Information", expanded=False):
        display_form(DataHelper().get_additional_data())
elif loan_type == 'Motobike':
    predict_url = BASE_URL + MB_PRIDICT_ENDPOINT
    with st.expander("Personal Information", expanded=True):
        display_form(DataHelper().get_personal_data())
    with st.expander("Thông tin khoản vay", expanded=True):
        display_form(DataHelper().get_mb_data())
    with st.expander("Thông tin đại lý", expanded=False):
        display_form(DataHelper().get_dealer_data())
    with st.expander("Financial Information", expanded=False):
        display_form(DataHelper().get_financail_data())
    with st.expander("Insurance Information", expanded=False):
        display_form(DataHelper().get_insurance_data())
    with st.expander("Thông tin khách hàng bổ xung", expanded=False):
        display_form(DataHelper().get_address_data())
    with st.expander("Additional Information", expanded=False):
        display_form(DataHelper().get_additional_data())
elif loan_type == 'New Car':
    predict_url = BASE_URL + NC_PREDICT_ENDPOINT
    with st.expander("Personal Information", expanded=True):
        display_form(DataHelper().get_personal_data())
    with st.expander("Thông tin khoản vay", expanded=True):
        display_form(DataHelper().get_nc_data())
    with st.expander("Thông tin đại lý", expanded=False):
        display_form(DataHelper().get_dealer_data())
    with st.expander("Financial Information", expanded=False):
        display_form(DataHelper().get_financail_data())
    with st.expander("Insurance Information", expanded=False):
        display_form(DataHelper().get_insurance_data())
    with st.expander("Thông tin khách hàng bổ xung", expanded=False):
        display_form(DataHelper().get_address_data())
    with st.expander("Additional Information", expanded=False):
        display_form(DataHelper().get_additional_data())
elif loan_type == 'Truck':
    predict_url = BASE_URL + TRUCK_PREDICT_ENDPOINT
    with st.expander("Personal Information", expanded=True):
        display_form(DataHelper().get_personal_data())
    with st.expander("Thông tin khoản vay", expanded=True):
        display_form(DataHelper().get_truck_data())
    with st.expander("Thông tin đại lý", expanded=False):
        display_form(DataHelper().get_dealer_data())
    with st.expander("Financial Information", expanded=False):
        display_form(DataHelper().get_financail_data())
    with st.expander("Insurance Information", expanded=False):
        display_form(DataHelper().get_insurance_data())
    with st.expander("Thông tin khách hàng bổ xung", expanded=False):
        display_form(DataHelper().get_address_data())
    with st.expander("Additional Information", expanded=False):
        display_form(DataHelper().get_additional_data())
else:
    st.error("Product not supports")


def display_predict_result(data):
    st.markdown('<h1 class="title">ANALYSIS RESULT</h1>',
                unsafe_allow_html=True)
    score = data['predict_score'] * 100

    _, col2, _ = st.columns([1, 6, 1])

    with col2:
        st.markdown(f'''
    <h2 class="title">
        **Default Probability is <span style="color:organe; font-size:40px;">{score}%</span>.**
    </h2>''', unsafe_allow_html=True)

        # Create a figure and axis
        fig, ax2 = plt.subplots(figsize=(6, 1))
        # Gradient from white to red
        gradient = np.linspace(0, 1, 100).reshape(1, -1)
        ax2.imshow(gradient, aspect='auto', cmap=plt.get_cmap(
            'Reds'), extent=[0, 100, -0.25, 0.25])
        # Set x-axis limit
        ax2.set_xlim(0, 100)
        # Add threshold line at 80 (vertical)
        threshold = 67
        ax2.axvline(threshold, color='green', linestyle='--',
                    label=f'Threshold = {threshold}')
        # Add random score line (dashed blue line)
        ax2.axvline(score, color='yellow', linestyle='--',
                    label=f'Random Score = {score}')
        # Remove left and bottom ticks
        ax2.tick_params(axis='x', labelsize=6)
        ax2.set_yticks([])

        xticks_positions = [score]
        xticks_labels = [f'Score: {score}']
        ax2.set_xticks(xticks_positions)
        ax2.set_xticklabels(xticks_labels)
        # Add threshold label
        ax2.text(threshold, 0.3,
                 f'Threshold: {threshold}', color='black', fontsize=6, ha='center')
        ax2.text(0, 0.3, 'NON DEFAULT', color='black', fontsize=6,
                 ha='center')  # Vị trí y = 0.3 sẽ nằm phía trên biểu đồ
        ax2.text(100, 0.3, 'DEFAULT', color='black', fontsize=6, ha='center')
        sns.despine(left=True, bottom=True)
        # Display the chart in Streamlit
        st.pyplot(fig)
        # Display "waterfall_base64_image"
        # Decode the base64 string into bytes
        image_bytes = base64.b64decode(data['waterfall_base64_image'])
        image = Image.open(BytesIO(image_bytes))
        st.image(image,
                 caption="Score Analysis Result")


if st.button("Analysis Score!", type="primary"):
    with st.spinner("Loading, please wait a momment!"):
        json_data = DataHelper().get_input_data(loan_type)
        st.write(json_data)
        
        # time.sleep(2)
        #response = requests.post(predict_url, json=get_input_data())

    #if response.status_code == 200:
        # st.success('Analysis complete! Here are the results...')
        #display_predict_result(response.json())
