#importing things I need to begin coding with Gen AI (and eventually web checkers)
from google import genai
from google.genai import types
#Importing from WAVE API
import requests

#WAVE API - 100 uses per month free
APIKEY = "Dz9eZUmU5924"
websiteUrl = input("Please enter the URL for the website you want to check:")

response = requests.get(
    f"https://wave.webaim.org/api/request?key={APIKEY}&url={websiteUrl}"
)
data = response.json() 
#Python formatted string to make it easier for Google Gemini to understand
formatted_summary = f"""
Page Title: {data['statistics']['pagetitle']}
Page URL: {data['statistics']['pageurl']}
Total Accessibility Issues: {data['statistics']['allitemcount']}

Category Breakdown:
Errors: {data['categories']['error']['count']}
Contrast Errors: {data['categories']['contrast']['count']}
Alerts: {data['categories']['alert']['count']}
"""

#Google Gemini
client = genai.Client(api_key='AIzaSyBvA2AB1Xr04QMDhzCLD46ZBAbuzWA95Sk')

response = client.models.generate_content(
   model = "models/gemini-flash-lite-latest",
   contents= ("Using the following response from a web accessibility checker, please go into detail about each issue that you can in a simple and concise way. Please keep your response as short as possible while still being clear. Your response should include the WCAG standard/regulation that caused the failure and potential fixes and solutions. The accessibility report is as follows:", formatted_summary, "The response should be understandable for beginners and anyone wanting to learn.")
)


print(response.text)

userInput = input("Would you like me to go into more detail about any issue? If so, please specify")
response = client.models.generate_content(
   model = "models/gemini-flash-lite-latest",
   contents= (userInput)
)

print(response.text)
