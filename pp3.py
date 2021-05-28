import streamlit as st
import pandas as pd

def app():
    def gas_cap_drive(bo,boi,rsi,rs,bg,m,bgi,gp,np):
        boi=float(boi)
        bo=float(bo)
        rsi=float(rsi)
        rs=float(rs)
        bg=float(bg)
        m=float(m)
        bgi=float(bgi)
        gp=float(gp)
        np=float(np)
        rp=gp/np
        rf=((bo-boi)+(rsi-rs)*bg+m*boi*(bg-bgi)/bgi)/(bo+(rp-rs)*bg)
        n=np/rf
        return rf,n
    st.title("""
    Enter Input Values
    
    (Common assumptions for gas cap drive:- Ginj=Winj=0, Change in pore volume is neglected.)
    """)
    with st.form(key='form4'):
        col1,col2=st.beta_columns([1,1])
        with col1:
            rsi = st.text_input('Rsi, Initial gas solubility (scf/STB)')
            rs = st.text_input('Rs, Gas solubility (scf/STB)')
            boi = st.text_input('Boi, Initial oil formation volume factor (bbl/STB)')
            bo = st.text_input('Bo, Oil formation volume factor at p (bbl/STB)')
            bg = st.text_input('Bg, Gas formation volume factor at p (bbl/scf)')
        with col2:
            bgi = st.text_input('Bgi, Initial gas formation volume factor at p (bbl/scf)')
            gp = st.text_input('Gp, Cumulative gas produced (scf)')
            np = st.text_input('Np, Cumulative oil produced (STB)')
            m= st.text_input('m, Ratio of initial gas-cap-gas reservoir volume to initial reservoir oil volume (bbl/bbl)')
        submit4=st.form_submit_button(label='Calculate')
    if submit4:
        r,n=gas_cap_drive(bo,boi,rsi,rs,bg,m,bgi,gp,np)
        st.subheader('Original(Initial) Oil In Place (STB) :')
        st.write(n)
        st.subheader('Recovery factor for Solution gas drive reservoir (below bubble point pressure) :')
        st.write(r)