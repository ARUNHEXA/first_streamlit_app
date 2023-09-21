import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 Oats breakfast')
streamlit.text(' 🥗 Poha')
streamlit.text(' 🐔 Khichdi')
streamlit.text(' 🥑🍞 Guacamole')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#imprt pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruit - ",list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.dataframe(my_fruit_list)

#display the table on the page
streamlit.dataframe(fruits_to_show)

#create repeatable code block
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
   # streamlit.write('The user entered',fruit_choice)

#take the jason version of the response and normalize it
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output on the screen as a table
  return fruityvice_normalized
  

#import requests
streamlit.header("Fruityvice Fruit Advice!")
try: 
#streamlit.text(fruityvice_response.json()) #just write data to screen
#add a text entry box and send the input to fruityvice as part of the API call
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)



except URLError as e:
  streamlit.error()






streamlit.header("The fruit load list contains : ")
#snowflake related function
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()
  
 #Add a button to load a fruit 
if streamlit.button('Get fruit load list'):
    #import snowflake connector
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

#Allow end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
       return "Thanks for adding" + new_fruit
#adding additional text box
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function = insert_row_snowflake(add_my_fruit)
      my_cnx.close()
      streamlit.text(back_from_function)

streamlit.stop()


