import streamlit as st
import random
import string
import time
import pyperclip

## settings
page_title = "Ulta Secure Password Generator by 949 Web Designs"
page_icon = ":closed_lock_with_key:"
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title("Quickly generate a highly secure password!")

##hide streamlit branding
hide_st_style = """
    <style>
    #MainMenu {display: none;}
    footer {display: none;}
    header[class^="css-"] {display: none;}
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)


## drop down to select password features
include_numbers = ['Yes', 'No']
include_special_characters = ['Yes', 'No']

##input form
st.header("Choose your security optoins:")
with st.form("entry_form", clear_on_submit=False):
    st.slider("How long should your password be?", min_value=8, max_value=64, step=4, help="Longer passwords are more secure!", key="pass_length")
    col1, col2 = st.columns(2)
    col1.selectbox("Include numbers?", include_numbers, help="Passwords are much more secure with numbers but not all services will allow them.", key="inc_nums")
    col2.selectbox("Include special characters?", include_special_characters, help="Passwords are much more secure with special characters but not all services will allow them.", key="inc_spchar")

    submitted = st.form_submit_button("Generate Password")
    if submitted:
        length = st.session_state["pass_length"]
        incnums = st.session_state["inc_nums"]
        incspecsym = st.session_state["inc_spchar"]

        ##define data
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        if incnums == "Yes":
            if incspecsym == "Yes":
                ##combine the data
                all = lower + upper + num + symbols
            else:
                all = lower + upper + num
        else:
            if incspecsym == "Yes":
                all = lower + upper + symbols
            else:
                all = lower + upper


        ##use random 
        rando = random.choices(all,k=length)

        ##create the password 
        password = "".join(rando)

        ##print the password
        st.write(str(password))
        time.sleep(0.5)
        pyperclip.copy(password)
        st.write("Your new password has already been copied to the clipboard!")
