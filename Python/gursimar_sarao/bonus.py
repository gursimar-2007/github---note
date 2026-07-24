import requests 
import sys 
import json
if len(sys.argv)>=3:
    print("high values")
elif len(sys.argv)<=3:
    print("low values")
else:
    response = requests.get("https://itunes.apple.com/search?term="+sys.argv[1]+"&media=music&entity=song&limit="+sys.argv[2])
    print(json.dumps(response.json(), indent=2))
# the api usually sends a request to a server for data and the 
# server processes the data sent by you if you have an api key the server also checks
# that api key and matches that usually api keys are confidential
# and if the api key matches then it converts it into json after that
# the data is given to the code and it processes and shows it to the user