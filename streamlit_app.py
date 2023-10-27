import streamlit
import pandas

streamlit.header('test')
myfruitlist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruitlist = myfruitlist.set_index('Fruit')

streamlit.multiselect("pick some fruits:", list(myfruitlist.index))

streamlit.dataframe(myfruitlist)
