import streamlit as st


st.set_page_config(
    page_title="Multiple App",
)
st.title("Main page")
st.sidebar.success("Select a page above.")
if "my_input" not in st.session_state:
    st.session_state["my_input"]=""
my_input= st.text_input("Input a text here",st.session_state["my_input"])
submit=st.button('submit')   
if submit:
    st.session_state["my_input"]=my_input
    st.write("you have enterd:",my_input) 