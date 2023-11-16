import streamlit
import pandas
import requests
import snowflake.connector as cn
from urllib.error import URLError


connection = cn.connect(**streamlit.secrets["snowflake"])

cur = cn.cursor()
cur.execute("select current_account()")
streamlit.write(cur.fetchall())


