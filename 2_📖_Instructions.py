import streamlit as st
import pandas as pd

st.title('How to use this App?')

st.navigation([st.Page("App.py"), st.Page("3_About Me.py")])
st.write('''This App will help you calculate how much you need to score in the Entry Test.\n
The Formula to calculate CPN: 10 % of your Matric Percentage + 30 % of your Intermediate Percentage + 60% of test marks \n

To pass the test, You must score at least 50. \n
Because some departments have low merit, I have intentionally displayed 15 to 20 more marks to assure you are on the safe side.
Jis Department mn 50 s less minimum marks show hu rhe hn us s fool na hn. Uske lie apko 60s mn marks lane hn g. \n

Minimum marks s relax mt hu jaie ga. Seat mlne ka Last chance h woh. You still have to score better to get to the safe side. 
 \n Any sort of questions are welcome: pc19243.muhammmadyousuf@gmail.com
''')

required_cpn = {
    'BS CS': 64,
    'BS AI': 60,
    'BS Cyber': 57,
    'BE Architecture': 54,
    'BE CSE': 63,
    'BE Electronics': 55,
    'BE Energy & Environment': 51,
    'BE Industrial': 53,
    'BE Metallurgy Material': 50.32,
    'BE Petroleum': 50.41,
    'BE Telecom': 51,
    'BE Chemical': 52
}

df = pd.DataFrame(list(required_cpn.items()), columns=["Department", "Closing CPN 2023"])
st.dataframe(df)