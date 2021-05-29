import streamlit as st
import pandas as pd
from PIL import Image
import pp1,pp2,pp3,pp4,pp5

def app1():
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
        pp1.app1()
    elif status=='Solution gas drive reservoir (below bubble point pressure)':
        pp2.app()
    elif status=='Gas cap drive reservoir':
        pp3.app()
    elif status=='Water drive reservoir':
        pp4.app()
    elif status=='Combination drive reservoir':
        pp5.app()
main()
