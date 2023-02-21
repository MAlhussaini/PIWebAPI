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
# TODO -> enter ParentIds for each of the subrequests
body = {
    "GetSystemLanding": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system"
    },
    "GetCacheInstances": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.CacheInstances",
        "ParentIds": [
            "TODO"
        ]
    },
    "GetConfiguration": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.Configuration",
        "ParentIds": [
            "TODO"
        ]
    },
    "GetUserInfo": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.UserInfo",
        "ParentIds": [
            "TODO"
        ]
    },
    "GetVersions": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.Versions",
        "ParentIds": [
            "TODO"
        ]
    },
    "GetStatus": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.Status",
        "ParentIds": [
            "TODO"
        ]
    },
    "GetInstanceConfiguration": {
        "Method": "GET",
        "Resource": "$.GetSystemLanding.Content.Links.InstanceConfiguration",
        "ParentIds": [
            "TODO"
        ]
    }
}

response = client.post(endpoint="batch", body=body)