import streamlit 
import pandas

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


