import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np
from helper import DataHelper
from css_helper import load_css
import time

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
        Motorbike (MB), Personal Loan (PL), New Car, and Truck. The purpose of this demo is to simulate the process of entering customer information, where the AI model will return a Credit Score along with the key factors influencing that score.
        This application is designed for demonstration purposes only and aims to highlight how AI can assist in improving credit evaluation processes.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h2 class="title">APPLICATION FORM</h2>', unsafe_allow_html=True)
_, center, _ = st.columns([1, 3, 1])
with center:
    loan_type = st.radio('Select the Loan type:', options=[
                         'Motobike', 'Personal Loan', 'Car', 'Truck'], horizontal=True)


def display_form(data):
    st.markdown(f"## {data['title']}:")
    with st.container(height=400, border=True):
        cols = st.columns(4)
        for idx, field in enumerate(data['fields']):
            col = cols[idx % 4]
            input_type = field['input_type']
            key = field['key']
            default_value = field['default']
            if input_type == 'text':
                col.text_input(f"{field['name']}", value=default_value, key=key)
            if input_type == 'number':
                col.number_input(
                    f"{field['name']}",
                    min_value=float(field['min']),
                    max_value=float(field['max']),
                    value=float(default_value),
                    step=float(field.get('step', 1.0)),
                    key=key
                )
            if input_type == 'boolean':
                col.checkbox(f"{field['name']}",
                            value=bool(default_value), key=key)


if loan_type == 'Personal Loan':
        with st.expander("Personal Information", expanded=True):          
            display_form(DataHelper().get_personal_data())
        with st.expander("Financial Information", expanded=False):
             display_form(DataHelper().get_financail_data())
        with st.expander("Insurance Information", expanded=False):
             display_form(DataHelper().get_insurance_data())
        with st.expander("Additional Information", expanded=False):     
            display_form(DataHelper().get_additional_data())
else:   
        with st.expander("Product Information", expanded=True):
            display_form(DataHelper().get_product_data())
        with st.expander("Personal Information", expanded=False):          
            display_form(DataHelper().get_personal_data())
        with st.expander("Financial Information", expanded=False):
             display_form(DataHelper().get_financail_data())
        with st.expander("Insurance Information", expanded=False):
             display_form(DataHelper().get_insurance_data())
        with st.expander("Additional Information", expanded=False):     
            display_form(DataHelper().get_additional_data())

run = st.button('Analysis')
if run:
    with st.spinner('Analyzing...'):
        time.sleep(2)  # Simulate a delay for analysis
    st.success('Analysis complete! Here are the results...')
    st.markdown('<h1 class="title">Credit Score Results</h1>',
                unsafe_allow_html=True)
    # Generate random score
    random_score = random.randint(1, 100)

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.markdown(f'''
    <h2 class="title">
        **Your credit score is <span style="color:organe; font-size:40px;">{random_score}</span>.**
    </h2>''', unsafe_allow_html=True)

        # Create a figure and axis
        fig, ax2 = plt.subplots(figsize=(6, 1))

        # Gradient from white to red
        gradient = np.linspace(0, 1, 100).reshape(1, -1)
        ax2.imshow(gradient, aspect='auto', cmap=plt.get_cmap('Reds'), extent=[0, 100, -0.25, 0.25])

        # Set x-axis limit
        ax2.set_xlim(0, 100)

        # Add threshold line at 80 (vertical)
        threshold = 80
        ax2.axvline(threshold, color='green', linestyle='--', label=f'Threshold = {threshold}')

        # Add random score line (dashed blue line)
        ax2.axvline(random_score, color='yellow', linestyle='--', label=f'Random Score = {random_score}')

        # Remove left and bottom ticks
        ax2.tick_params(axis='x', labelsize=6)
        ax2.set_yticks([])


        xticks_positions = [0,random_score, threshold, 100]
        xticks_labels = ['NON DEFAULT', 'Score', 'Threshold', 'DEFAULT']
        ax2.set_xticks(xticks_positions)
        ax2.set_xticklabels(xticks_labels)
    
        # Add custom labels for specific positions (0, 100, and 80)
        # ax2.text(0, -0.25, 'Non Default', color='black', fontsize=8, ha='center')
        # ax2.text(100, -0.25, 'Default', color='black', fontsize=8, ha='center')
        # ax2.text(threshold, -0.25, 'Threshold', color='black', fontsize=8, ha='center')
        # ax2.set_yticklabels(1, 3)
        # Remove spines for cleaner look
        sns.despine(left=True, bottom=True)

        # Display the chart in Streamlit
        st.pyplot(fig)
       
        st.image('app/demo_shap_chart.png',
                 caption="Credit Score Analysis Result")
