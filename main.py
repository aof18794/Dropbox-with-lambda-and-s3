import requests
import os
from dotenv import load_dotenv
import base64

load_dotenv()

welcome_text = """

    Welcome to myDropbox Application
    ======================================================
    Please input command (newuser username password password, login 
    username password, put filename, get filename, view, or logout). 
    If you want to quit the program just type quit.
    ======================================================
    
"""

print(welcome_text)

api_route = os.getenv("API_ROUTE")
if api_route == None:
    print("API_ROUTE not found")
    exit()

input_command = input(">>")

while input_command != "quit":
    try:
        method, filename = input_command.split()
    except:
        print("Invalid command: Try [put/get/view] [filename]")
        input_command = input(">>")
        continue

    if method == "put":
        try:
            with open('./file/' + filename, 'rb') as file:
                url = api_route + "add"
                x = requests.post(
                    url, headers={"file-name": filename}, data=file)
            print("File uploaded successfully")
        except:
            print("File not found")

    elif method == "view":
        print("")

    elif method == "get":
        try:
            url = api_route + "download"
            x = requests.post(
                url, json={"filename": filename})
            data = base64.b64decode(x.text)
            with open('./file/' + filename, 'wb') as file:
                file.write(data)

            print("Downloaded successfully")
        except:
            print("Cannot download file")

    input_command = input(">>")

print("======================================================")
