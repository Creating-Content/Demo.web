import streamlit as st



name = st.text_input("Enter ur name :")
fname = st.text_input("Enter ur gf name :")
adr = st.text_area("Enter ur text :")
classdata = st.selectbox("Enter ur class:",(1,2,3,4,5,6,7,8,9))


button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Gf name : {fname}
    address : {adr}
    class : {classdata}""")

