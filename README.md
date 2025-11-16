# Ai-Assisted-Accessibility-Checker
This is an AI-assisted, educationally focused web accessibility checker. This project relies on 2 Application Programming Interfaces (WAVE and Google Gemini).
The WAVE API has limited monthly tokens; once those tokens run out, they won't replenish until the month resets.
In order to use, simply copy & paste the code into any code space like Visual Studio Code or even https://www.onlinegdb.com/# .
If you don't want to wait for the tokens to replenish, create an account at https://wave.webaim.org/api/register, and once you receive your API key, replace the API key on line 8.
To create your own API key for Google Gemini, go to https://aistudio.google.com/ and create an account. Replace the API key on line 28 with your key.
IMPORTANT: You MUST install the proper dependencies in the terminal beforehand: pip install python-gemini-api.
#
Here is a list of website URLs for anyone to test. Some of these were specifically created to be used in accessibility checker tools. Most of the inaccessible sites I got from Selfthinker (Anika Henke) on Github. Go here to see their profile: https://gist.github.com/selfthinker
Inaccessible:
  https://overlaysdontwork.com/
  https://record-a-goose-sighting.apps.live.cloud-platform.service.justice.gov.uk/
  https://codepo8.github.io/a11y-demos/page-with-errors.html 
  https://fakewinebarrel.com/
accessible:
