from PiWebApiClient import PiWebApiClient 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########         Exercise 6a - Get System Endpoints        #########
#########                  (RequestTemplate)                #########
#########                                                   #########
#####################################################################


# Instantiate the http client class which uses the requests library
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")

# Use a request template to simplify the batch request
body = {
    "GetSystemLanding": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/system"
    },
    "GetAllLinkEndpoints": {
        "Method": "GET",
        "RequestTemplate": {
            "Resource": "{0}"
        },
        "Parameters": [
            "$.GetSystemLanding.Content.Links.*"
        ],
        "ParentIds": [
            "GetSystemLanding"
        ]
    }
}

response = client.post(endpoint="batch", body=body)