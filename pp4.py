import streamlit as st
import pandas as pd

def app():
    def water_drive(bo,boi,gp,rs,bg,we,wp,bw,rsi,np):
        boi=float(boi)
        bo=float(bo)
        gp=float(gp)
        rs=float(rs)
        bg=float(bg)
        we=float(we)
        wp=float(wp)
        bw=float(bw)
        rsi=float(rsi)
        np=float(np)
        rp=gp/np
        n=(np*(bo+(rp-rs)*bg)-(we-wp*bw))/((bo-boi)+(rsi-rs)*bg)
        rf=np/n
        return rf,n
    st.title("""
    Enter Input Values
    
    (Common assumptions for water drive:- m=0, Ginj=Winj=0, Change in pore volume is neglected.)
    """)
    with st.form(key='form5'):
        col1,col2=st.beta_columns([1,1])
        with col1:
            rsi = st.text_input('Rsi, Initial gas solubility (scf/STB)')
            rs = st.text_input('Rs, Gas solubility (scf/STB)')
            boi = st.text_input('Boi, Initial oil formation volume factor (bbl/STB)')
            bo = st.text_input('Bo, Oil formation volume factor at p (bbl/STB)')
            gp = st.text_input('Gp, Cumulative gas produced (scf)')
        with col2:
            bg = st.text_input('Bg, Gas formation volume factor at p (bbl/scf)')
            we = st.text_input('We, Cumulative water influx (bbl)')
            wp = st.text_input('Wp, Cumulative water produced (bbl)')
            bw = st.text_input('Bw, Water formation volume factor at p (bbl/STB)')
            np = st.text_input('Np, Cumulative oil produced (STB)')
        submit5=st.form_submit_button(label='Calculate')
    if submit5:
        r,n=water_drive(bo,boi,gp,rs,bg,we,wp,bw,rsi,np)
        st.subheader('Original(Initial) Oil In Place (STB) :')
        st.write(n)
        st.subheader('Recovery factor for Solution gas drive reservoir (below bubble point pressure) :')
        st.write(r)