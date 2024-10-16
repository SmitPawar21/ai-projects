import streamlit as st
import langchainhelper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American", "French", "Chinese", "Thai"))

if cuisine:
    response = langchainhelper.generate_name_items(cuisine)

    st.header(response['restaurant_name'])

    menu_items = response['menu_items'].split(",")

    st.write("Suggested menu items")
    for item in menu_items:
        st.write("-", item)
