# import requests
# import sys
# import json

# if len(sys.argv) != 2:
#     sys.exit("Usage: python song.py <song name>")

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# # print(json.dumps(response.json(), indent=2))

# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])
import requests
import sys
import json

if len(sys.argv)>3:
    print("jada values pa diti")
elif len(sys.argv)<3:
    print("ghat values pa diti")
else:
    response = requests.get("https://itunes.apple.com/search?term="+sys.argv[1]+"&media=music&entity=song&limit="+sys.argv[2])
    # print(json.dumps(response.json(), indent=2))
    data = response.json()
    for items in data["results"]:
        print(items["trackName"])