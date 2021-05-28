import streamlit as st
import pandas as pd

def app():
    def sol_gas_drive_abovebubblepoint(boi,pi,p,bo,sw,cw,cf,np):
        np=float(np)
        delta_p=float(pi)-float(p)
        sw=float(sw)/100
        so=1-sw
        co=(float(bo)-float(boi))/(float(boi)*delta_p)
        ce=((float(co)*so)+(float(cw)*sw)+float(cf))/so
        rf=(float(boi)*float(ce)*delta_p)/float(bo)
        n=np/rf
        return rf,n
    st.title("""
    Enter Input Values
    
    (Common assumptions for solution gas drive(above bubble point):- m=0, We=0, Ginj=Winj=0)
    """)
    with st.form(key='form2'):
        col1,col2=st.beta_columns([1,1])
        with col1:
            pi = st.text_input('Pi, Initial Reservoir Pressure (psi)')
            p = st.text_input('P, Volumetric average Reservoir Pressure (psi)')
            boi = st.text_input('Boi, Initial oil formation volume factor (bbl/STB)')
            bo = st.text_input('Bo,Oil formation volume factor at p (bbl/STB)')
        with col2:
            sw = st.text_input('Sw, Initial water Saturation (%)')
            cw = st.text_input('Cw, Water Compressibility (1/psi)')
            cf = st.text_input('Cf, Formation(rock) Compressibility (1/psi)')
            np = st.text_input('Np, Cumulative oil produced (STB)')
        submit2=st.form_submit_button(label='Calculate')
    if submit2:
        r,n=sol_gas_drive_abovebubblepoint(boi,pi,p,bo,sw,cw,cf,np)
        st.subheader('Original(Initial) Oil In Place (STB) :')
        st.write(n)
        st.subheader('Recovery factor for Solution gas drive reservoir (above bubble point pressure) :')
        st.write(r)