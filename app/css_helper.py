def load_css():
    return """
    <style>
    body {
            background-color: lightgrey;
        }
    .title {
        text-align: center;
    }
    .center-button {
        display: flex;
        justify-content: center;
    }
    .custom-markdown {
        margin-bottom: 0px;
    }
    /* Main container styling */
    .app-container {
        border: 2px solid #d3d3d3;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stVerticalBlock {
        max-height: 600px;  /* Set the maximum height of the container */
        overflow-y: auto;   /* Add vertical scrollbar if content overflows */
    }
    /* Columns and input field border styling */
    .stTextInput, .stNumberInput, .stSlider, .stCheckbox {
        border: 1px solid #d3d3d3 !important;
        border-radius: 5px !important;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stRadio > label {
        display: block;
        text-align: center;
    }
    div[role="radiogroup"] {
        display: flex;
        justify-content: center;
    }
    div.stButton > button {
        display: block;
        margin-left: auto;
        margin-right: auto;
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 15px 40px; /* Increased padding for a wider button */
        font-size: 16px;
        font-weight: bold;  /* Make text bold */
        border: none;
        cursor: pointer;
        text-transform: uppercase; /* Capitalize text */
    }
     /* Checkbox height adjustment */
    div[data-testid="stCheckbox"] {
        height: 90px; /* Adjust this value to match other inputs */
        display: flex;
        align-items: center;
    }
    
    </style>
    """
