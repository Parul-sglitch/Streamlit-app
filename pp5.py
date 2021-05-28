import streamlit as st
import pandas as pd

def app():
    def combination_drive(bo,gp,np,rs,bg,we,wp,bw,boi,rsi,m,bgi):
        boi=float(boi)
        bo=float(bo)
        gp=float(gp)
        np=float(np)
        rs=float(rs)
        bg=float(bg)
        we=float(we)
        wp=float(wp)
        bw=float(bw)
        rsi=float(rsi)
        m=float(m)
        bgi=float(bgi)
        rp=gp/np
        n=(np*(bo+(rp-rs)*bg)-(we-wp*bw))/((bo-boi)-(rsi-rs)*bg+m*boi*((bg/bgi)-1))
        rf=np/n
        return rf,n
    st.title("""
    Enter Input Values
    
    (Common assumptions for combination drive:- Ginj=Winj=0, Change in pore volume is neglected.)
    """) 
    with st.form(key='form6'):
        col1,col2=st.beta_columns([1,1])
        with col1:
            rsi = st.text_input('Rsi, Initial gas solubility (scf/STB)')
            rs = st.text_input('Rs, Gas solubility (scf/STB)')
            boi = st.text_input('Boi, Initial oil formation volume factor (bbl/STB)')
            bo = st.text_input('Bo, Oil formation volume factor at p (bbl/STB)')
            gp = st.text_input('Gp, Cumulative gas produced (scf)')
            bgi = st.text_input('Bgi, Initial gas formation volume factor (bbl/scf)')
        with col2:
            bg = st.text_input('Bg, Gas formation volume factor at p (bbl/scf)')
            we = st.text_input('We, Cumulative water influx (bbl)')
            wp = st.text_input('Wp, Cumulative water produced (bbl)')
            bw = st.text_input('Bw, Water formation volume factor at p (bbl/STB)')
            np = st.text_input('Np, Cumulative oil produced (STB)')
            m = st.text_input('m, Ratio of initial gas-cap-gas reservoir volume to initial reservoir oil volume (bbl/bbl)')
        submit6=st.form_submit_button(label='Calculate') 
    if submit6:
        r,n=combination_drive(bo,gp,np,rs,bg,we,wp,bw,boi,rsi,m,bgi)
        st.subheader('Original(Initial) Oil In Place (STB) :')
        st.write(n)
        st.subheader('Recovery factor for Solution gas drive reservoir (below bubble point pressure) :')
        st.write(r)        