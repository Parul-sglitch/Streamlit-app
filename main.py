import streamlit as st
import pandas as pd
from PIL import Image

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

def app2():
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


def app3():
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
def app4():
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
def app5():
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
def main():
    col1,col2=st.beta_columns([1,2])
    with col1:
        img = Image.open("rig.jpeg")
        st.image(img, width=200)    
    with col2:
        st.title("Original Oil In Place & Recovery Factor Calculation")
    st.sidebar.title('Different Drive Reservoirs')
    status=st.sidebar.radio('Select type of reservoir:',('Solution gas drive reservoir (above bubble point pressure)','Solution gas drive reservoir (below bubble point pressure)','Gas cap drive reservoir','Water drive reservoir','Combination drive reservoir'))
    if status=='Solution gas drive reservoir (above bubble point pressure)':
        app1()
    elif status=='Solution gas drive reservoir (below bubble point pressure)':
        app2()
    elif status=='Gas cap drive reservoir':
        app3()
    elif status=='Water drive reservoir':
        app4()
    elif status=='Combination drive reservoir':
        app5()
if __name__ == "__main__":
    main()
