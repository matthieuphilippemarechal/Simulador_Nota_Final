import streamlit as st
import pandas as pd
import numpy as np
#import SessionState

### Config
st.set_page_config(
    page_title="Simulador de nota final",
    layout="wide"
)

### HEADER
st.title('Simula tu nota final')



#delay = pd.read_excel('get_around_delay_analysis.xlsx')

Nota_C1 = st.sidebar.selectbox("Indique la nota del control 1 (indicar 1 si ausente)",[x/10 for x in range(10,71)])

Nota_C2 = st.sidebar.selectbox("Indique la nota del control 2 (indicar 1 si ausente)",[x/10 for x in range(10,71)])

Nota_C3 = st.sidebar.selectbox("Indique la nota del control 3 (indicar 1 si ausente)",[x/10 for x in range(10,71)])

Borrar_control = st.sidebar.selectbox(
    "Borras un control?",
    ("NO","SI")
)

Nota_S1 = st.sidebar.selectbox("Indique la nota de la solemne 1 (indicar 1 si ausente)",[x/10 for x in range(10,71)])

Nota_S2 = st.sidebar.selectbox("Indique la nota de la solemne 2 (indicar 1 si ausente)",[x/10 for x in range(10,71)])

Nota_E = st.selectbox("Indique una nota para el examen",[x/10 for x in range(10,71)])

if Borrar_control == "SI":
  NC = 0.5 * (np.sum([Nota_C1,Nota_C2,Nota_C3]) - np.min([Nota_C1,Nota_C2,Nota_C3]))
else:
  NC = np.mean([Nota_C1,Nota_C2,Nota_C3])

if Nota_E > min([Nota_S1,Nota_S2]):
  if Nota_S1 <= Nota_S2:
    Nota_S1 = Nota_E
  else:
    Nota_S2 = Nota_E

NP = 0.1 * int(3 * NC + 3.5 * Nota_S1 + 3.5 * Nota_S2 + 0.5)

NF = 0.1 * int(7 * NP + 3 * Nota_E + 0.5)

df = pd.DataFrame({"C1":[Nota_C1],"C2":[Nota_C2],"C3":[Nota_C3],"NC":[NC],"S1":[Nota_S1],"S2":[Nota_S2],"NP":[NP],"NE":[Nota_E],"NF":[NF]})

st.write(df)
    
