import streamlit
import pandas
import requests
import snowflake.connector as cn
from urllib.error import URLError


connection = cn.connect(
  user="1026303",
  password="ElderBerry42!",
  account="JPQYJYD-KEMPER",
  warehouse="corp_wh",
  role="useradmin"
)

cur = cn.cursor()
cur.execute("select current_account()")
streamlit.write(cur.fetchall())


