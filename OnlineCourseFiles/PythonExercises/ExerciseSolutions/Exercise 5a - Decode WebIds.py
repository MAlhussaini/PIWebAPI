from PiWebApiClient import PiWebApiClient 
from WebIdHelper import WebIdHelper
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########            Exercise 5a: Decode WebIds            #########
#########                                                   #########
#####################################################################

# WebId Specification found at https://pisquare.osisoft.com/community/developers-club/blog/2018/01/26/pi-web-api-web-id-20-specification-tables

# Instantiate the http client class which uses the requests library
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")

# Make a GetByPath request
response = client.get(endpoint="elements?path=\\\\PISRV01\\NuGreen\\NuGreen\\Houston&selectedFields=WebId&WebIdType=pathonly")

# Get the response body in JSON format
responseBody = response.json()

# Pick off the WebId field that was returned
webId = responseBody["WebId"]
print("WebId: " + webId)

# The first character of the WebId is the Type
webIdType = webId[0]
webIdDecodedType = WebIdHelper.decodeType(webIdType)
print(" Type: " + webIdType + " (" + webIdDecodedType + ")")

# The second character of the WebId indicates the version (1.0 or 2.0)
webIdVersion = webId[1]
webIdDecodedVersion = WebIdHelper.decodeVersion(webIdVersion)
print(" Version: " + webIdVersion + " (" + webIdDecodedVersion + ")")

# The next two characters mark which object type the WebId is representing
webIdObjectMarker = webId[2:4]
webIdDecodedObjectMarker = WebIdHelper.decodeObjectMarker(webIdObjectMarker)
print(" Object Marker: " + webIdObjectMarker + " (" + webIdDecodedObjectMarker + ")")

if (webIdDecodedType == "Full"):
    # If it is a "Full" WebId, the next thing encoded is System GUID
    webIdEncodedSystemGuid = webId[4:26]
    webIdDecodedSystemGuid = WebIdHelper.decodeGuid(webIdEncodedSystemGuid)
    print(" Encoded System GUID: " + webIdEncodedSystemGuid + " (" + webIdDecodedSystemGuid + ")")

    # If it is a "Full" WebId, the next thing encoded is the Object GUID
    webIdEncodedObjectGuid = webId[26:48]
    webIdDecodedObjectGuid = WebIdHelper.decodeGuid(webIdEncodedObjectGuid)
    print(" Encoded Object GUID: " + webIdEncodedObjectGuid + " (" + webIdDecodedObjectGuid + ")")

    # The rest of the WebId is the Base64 encoded Path
    webIdEncodedPath = webId[48:len(webId)]
    webIdDecodedPath = WebIdHelper.decodePath(webIdEncodedPath)
    print(" Encoded Path: " + webIdEncodedPath + " (" + webIdDecodedPath + ")")

if (webIdDecodedType == "Path Only"):
    # The rest of the WebId is the Base64 encoded Path
    webIdEncodedPath = webId[4:len(webId)]
    webIdDecodedPath = WebIdHelper.decodePath(webIdEncodedPath)
    print(" Encoded Path: " + webIdEncodedPath + " (" + webIdDecodedPath + ")")

if (webIdDecodedType == "ID Only"):
    # If it is a "IDOnly" WebId, the next thing encoded is System GUID
    webIdEncodedSystemGuid = webId[4:26]
    webIdDecodedSystemGuid = WebIdHelper.decodeGuid(webIdEncodedSystemGuid)
    print(" Encoded System GUID: " + webIdEncodedSystemGuid + " (" + webIdDecodedSystemGuid + ")")

    # If it is a "IDOnly" WebId, the next thing encoded is the Object GUID
    webIdEncodedObjectGuid = webId[26:48]
    webIdDecodedObjectGuid = WebIdHelper.decodeGuid(webIdEncodedObjectGuid)
    print(" Encoded Object GUID: " + webIdEncodedObjectGuid + " (" + webIdDecodedObjectGuid + ")")