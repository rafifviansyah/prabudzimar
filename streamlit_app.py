import streamlit as st

st.title("Informatika Prabu Dzimar") 
st
st.header("Aplikasi menilai ganjil/genap") 
angka= st.number_input("70:", value=0, step=1) 

if(angka % 2) == 0:
  st.write(f"{2,4,6,8,10} adalah jumlah angka genap") 
else:
  st.write(f"{1,3,5,7,9} adalah jumlah angka ganjil")
