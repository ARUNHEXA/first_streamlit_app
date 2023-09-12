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

