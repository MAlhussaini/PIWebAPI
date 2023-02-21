from PiWebApiClient import PiWebApiClient 
import json
import base64
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########        Exercise 8: Using Stream Updates           #########
#########                                                   #########
#####################################################################


# Make an regular HTTP request to retrieve the WebId
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")
response = client.get("points?path=\\\\PISRV01\\CDT158&selectedFields=WebId")
webId = response.json()['WebId']

# Use the WebId to register this stream for updates
response = client.post("streams/" + webId + '/updates')

# Get the LatestMarker field from the response
marker = response.json()["LatestMarker"]

while True:
    # Wait for user input to continue
    print("Press enter to retrieve updates (type \"q\" and enter to quit)")
    inp = input()
    if inp == "q":
        break
    
    # Retrieve the updates
    response = client.get("streams/updates/" + marker)

    # Get the next marker from the response
    marker = response.json()["LatestMarker"]


