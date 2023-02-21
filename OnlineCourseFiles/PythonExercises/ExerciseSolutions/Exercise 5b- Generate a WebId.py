from PiWebApiClient import PiWebApiClient 
from WebIdHelper import WebIdHelper
import base64
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########         Exercise 5b: Generate a WebId            #########
#########                                                   #########
#####################################################################

# WebId Specification found at https://pisquare.osisoft.com/community/developers-club/blog/2018/01/26/pi-web-api-web-id-20-specification-tables

# Instantiate the http client class which uses the requests library
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")

# Give a path to an AF Attribute
afpath = "PISRV01\\NuGreen\\NuGreen\\Tucson\\Distilling Process\\Equipment\\P-871|Process Feedrate"

# Build WebId one piece at a time
webIdType = "P"
webIdVersion = "1"
objectMarker = "Ab"
baseElementMarker = "E"
base64EncodedPath = base64.b64encode(str(afpath.upper()).encode("utf-8")).decode("utf-8")

# Combine the parts
generatedWebId = webIdType + webIdVersion + objectMarker + baseElementMarker + base64EncodedPath

# Make a GetValue request using the path only WebId
response = client.get(endpoint = "streams/" + generatedWebId +"/value")
