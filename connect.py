#connect to environment using requests libraries
import requests

#connect to another production API

def generate(text):

   #pass url to which connection needs to be made into get()
   response_API = "https://textvis-word-cloud-v1.p.rapidapi.com/v1/textToCloud"

     # Define the API parameters
   params = {
        "text": text,
        "words": 50,
        "font": "Trebuchet MS",
        "width": 500,
        "height": 500,
        "padding": 0
   }
   
   response = requests.get(response_API, params)
   if response.status_code == 200:
      data = response.json()
      print("Word cloud image URL: ", data["https://textvis-word-cloud-v1.p.rapidapi.com/v1/textToCloud"])
   else:
      print("failed", reponse.status_code)

   text = "text data for generating"
   generate(text)
   print(response_API.status_code)
