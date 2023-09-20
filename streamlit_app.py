import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 Oats breakfast')
streamlit.text(' 🥗 Poha')
streamlit.text(' 🐔 Khichdi')
streamlit.text(' 🥑🍞 Guacamole')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruit - ",list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.dataframe(my_fruit_list)

#display the table on the page
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json()) #just write data to screen

#add a text entry box and send the input to fruityvice as part of the API call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)

#take the jason version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output on the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

