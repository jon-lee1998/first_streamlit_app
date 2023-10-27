import streamlit
import pandas

streamlit.header('test')
myfruitlist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruitlist = myfruitlist.set_index('Fruit')

fruits_selected = streamlit.multiselect("pick some fruits:", list(myfruitlist.index))
fruits_to_show = myfruitlist.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
