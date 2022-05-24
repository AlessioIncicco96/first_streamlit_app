import streamlit 
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text ('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔Hard-Boiled Free-Range Egg')
streamlit.text ('🥑🍞Avocado Toast')

streamlit.header('🍌🥭Build Your Onw Fruit Smoothie🥝🍇')

My_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
My_fruit_list=My_fruit_list.set_index('Fruit')


#let's put a pick list here, so they can pick the fruit they want to include
Fruit_selected=streamlit.multiselect("Pick some fruits:",list(My_fruit_list.index),['Avocado','Strawberries'])

#show a fruit selected before
Fruit_to_show=My_fruit_list.loc[Fruit_selected]
#display the table on the page
streamlit.dataframe(Fruit_to_show)

#New section to disply fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json()) #Just writes the data to the screen

#New section to disply fruityvice api response
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


