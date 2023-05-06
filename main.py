import streamlit as st
from streamlit_searchbox import st_searchbox
from typing import List
import pandas as pd

df=pd.read_csv('./Dataset/dis_sym_dataset_comb.csv')
l=df.columns

element_map = {element: 0 for element in l}
picked_elements = []

def search_list(searchterm: str) -> List[str]:
    return [item for item in l if searchterm.lower() in item.lower()]

st.title("Which symptoms are you facing?")

selected_values = st.multiselect(
    label="Select elements", options=l, key="element_multiselect"
)

# Mark the selected elements as 1 in the map
for value in selected_values:
    element_map[value] = 1

# Display the picked elements
# st.write("**Your Symptoms:**")
# for element, value in element_map.items():
#     if value == 1:
#         st.write(element)
st.write(element_map)