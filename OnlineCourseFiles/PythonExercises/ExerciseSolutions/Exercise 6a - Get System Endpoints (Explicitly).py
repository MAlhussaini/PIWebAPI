from PiWebApiClient import PiWebApiClient 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########         Exercise 6a - Get System Endpoints        #########
#########                    (Explicitly)                   #########
#########                                                   #########
#####################################################################


# Instantiate the http client class which uses the requests library
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")

# Build out the body for a batch request
body = {
    "GetSystemLanding": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system"
    },
    "GetCacheInstances": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system/cacheinstances"
    },
    "GetConfiguration": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system/configuration"
    },
    "GetUserInfo": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system/userinfo"
    },
    "GetVersions": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system/versions"
    },
    "GetStatus": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system/status"
    },
    "GetInstanceConfiguration": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system/instanceconfiguration"
    }
}

response = client.post(endpoint="batch", body=body)