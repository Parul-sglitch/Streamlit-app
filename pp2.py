import streamlit as st
import pandas as pd

def app():
    def sol_gas_drive_belowbubblepoint(bo,boi,rsi,rs,bg,rp,np):
        bo=float(bo)
        boi=float(boi)
        rsi=float(rsi)
        rs=float(rs)
        bg=float(bg)
        rp=float(rp)
        np=float(np)
        rf=(bo-boi+((rsi-rs)*bg))/(bo+((rp-rs)*bg))
        n=np/rf
        return rf,n
    st.title("""
    Enter Input Values
    
    (Common assumptions for solution gas drive(below bubble point):- m=0, We=0, Ginj=Winj=0, Change in pore volume is neglected.)
    """)
    with st.form(key='form3'):
        col1,col2=st.beta_columns([1,1])
        with col1:
            rsi = st.text_input('Rsi, Initial gas solubility (scf/STB)')
            rs = st.text_input('Rs, Gas solubility (scf/STB)')
            boi = st.text_input('Boi, Initial oil formation volume factor (bbl/STB)')
            bo = st.text_input('Bo, Oil formation volume factor at p (bbl/STB)')
        with col2:
            bg = st.text_input('Bg, Gas formation volume factor at p (bbl/scf)')
            rp = st.text_input('Rp, Water Compressibility (1/psi)')
            np = st.text_input('Np, Cumulative oil produced (STB)')
        submit3=st.form_submit_button(label='Calculate')

    if submit3:
        r,n=sol_gas_drive_belowbubblepoint(bo,boi,rsi,rs,bg,rp,np)
        st.subheader('Original(Initial) Oil In Place (STB) :')
        st.write(n)
        st.subheader('Recovery factor for Solution gas drive reservoir (below bubble point pressure) :')
        st.write(r)