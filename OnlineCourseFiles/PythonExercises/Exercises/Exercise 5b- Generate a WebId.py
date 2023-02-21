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
# TODO -> replace the string below with the path to your desired AF Object (omitting the \\ prefix)
afpath = "TODO"

# Build WebId one piece at a time
webIdType = "P"
webIdVersion = "1"
# TODO -> add object marker for type according to specification
objectMarker = "TODO"
base64EncodedPath = base64.b64encode(str(afpath.upper()).encode("utf-8")).decode("utf-8")

# Combine the parts
generatedWebId = webIdType + webIdVersion + objectMarker + base64EncodedPath

# Make a GetValue request using the path only WebId
response = client.get(endpoint = "streamsets/" + generatedWebId +"/value")