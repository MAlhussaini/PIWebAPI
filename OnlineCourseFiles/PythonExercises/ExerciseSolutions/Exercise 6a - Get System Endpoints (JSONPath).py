from PiWebApiClient import PiWebApiClient 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########         Exercise 6a - Get System Endpoints        #########
#########                    (JSONPath)                     #########
#########                                                   #########
#####################################################################


# Instantiate the http client class which uses the requests library
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")

# Change the batch request to make all of the requests in one go
body = {
    "GetSystemLanding": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system"
    },
    "GetCacheInstances": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.CacheInstances",
        "ParentIds": [
            "GetSystemLanding"
        ]
    },
    "GetConfiguration": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.Configuration",
        "ParentIds": [
            "GetSystemLanding"
        ]
    },
    "GetUserInfo": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.UserInfo",
        "ParentIds": [
            "GetSystemLanding"
        ]
    },
    "GetVersions": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.Versions",
        "ParentIds": [
            "GetSystemLanding"
        ]
    },
    "GetStatus": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.Status",
        "ParentIds": [
            "GetSystemLanding"
        ]
    },
    "GetInstanceConfiguration": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.InstanceConfiguration",
        "ParentIds": [
            "GetSystemLanding"
        ]
    }
}

response = client.post(endpoint="batch", body=body)
