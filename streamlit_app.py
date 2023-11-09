import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.header('test')
myfruitlist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruitlist = myfruitlist.set_index('Fruit')

fruits_selected = streamlit.multiselect("pick some fruits:", list(myfruitlist.index))
fruits_to_show = myfruitlist.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)



try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to display information about")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("My fruit list contains:")
fruit_list2 = streamlit.dataframe(my_data_rows)



fruit_add = streamlit.text_input("What fruit would you like to add?")


