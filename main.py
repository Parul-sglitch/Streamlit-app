import streamlit as st
import pandas as pd
from PIL import Image
import pp1,pp2,pp3,pp4,pp5
def main():
    col1,col2=st.beta_columns([1,2])
    with col1:
        img = Image.open("https://github.com/Parul-sglitch/Streamlit-app/blob/main/rig.jpeg")
        st.image(img, width=200)    
    with col2:
        st.title("Original Oil In Place & Recovery Factor Calculation")
    st.sidebar.title('Different Drive Reservoirs')
    status=st.sidebar.radio('Select type of reservoir:',('Solution gas drive reservoir (above bubble point pressure)','Solution gas drive reservoir (below bubble point pressure)','Gas cap drive reservoir','Water drive reservoir','Combination drive reservoir'))
    if status=='Solution gas drive reservoir (above bubble point pressure)':
        pp1.app()
    elif status=='Solution gas drive reservoir (below bubble point pressure)':
        pp2.app()
    elif status=='Gas cap drive reservoir':
        pp3.app()
    elif status=='Water drive reservoir':
        pp4.app()
    elif status=='Combination drive reservoir':
        pp5.app()
main()
