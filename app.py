import streamlit as st
import nuumpy as np
import matplotlib.pyplot as plt
st.sidebar.title("Software Educativo para el estudio de fenomenos ondulatorios")
op1=st.sidebar.radio("",["Ondas Estacionarias","Interderencia de ondas","Onda general"])
if op1=="Ondas Estacionarias":
  st.title(op1)
  n=st.slider("",1,10)
  x=np.linspace(0,2*np.pi,150)
#st.write(x)
  y=np.sin(n*x/2)
  fig, ax = plt.subplots()
  st.pyplot(fig)
