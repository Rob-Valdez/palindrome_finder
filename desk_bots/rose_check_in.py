#!python3 C:\Users\kruser\PycharmProjects\desk_bots
#a script that checks into Rose

import requests
from bs4 import BeautifulSoup

page = requests.get("https://toolbelt.kaufmanrossin.com/users/sign_in")
soup = BeautifulSoup(page.content, 'html.parser')

#TODO: identify the login box

#TODO: get credentials from credentials_file

#TODO: input credentials

#TODO: load the contents of rose

#TODO: click status

#TODO: select status as not available
