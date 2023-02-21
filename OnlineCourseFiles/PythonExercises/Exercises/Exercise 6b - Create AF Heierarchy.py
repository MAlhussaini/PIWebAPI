from PiWebApiClient import PiWebApiClient 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########         Exercise 6b: Create AF Hierarchy          #########
#########                                                   #########
#####################################################################


# Instantiate the http client class which uses the requests library
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")

# Build out the body for a batch request to create the hierarchy
body = {
    "GetAFServer": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/assetservers?path=\\\\PISRV01",    
        "Headers": {
            "Cache-Control": "no-cache"
        }
    },
    "CreateAFDatabase": {
        "Method": "POST",
        "Resource": "https://pisrv01.pischool.int/piwebapi/assetservers/{0}/assetdatabases",
        "Content" : "{\"Name\": \"PIWebAPI_Batch_DB\"}",
        "Parameters": [
            # TODO -> Select the WebId field to pass in as a prarmeter to the Resource above
            "$.GetAFServer.Content.TODO"
        ],
        "ParentIds": [
            "GetAFServer"
        ],
        "Headers": {
            "Cache-Control": "no-cache"
        }
    },
    "CreateRootElement": {
        "Method": "POST",
        "Resource": "{0}/elements",
        "Content" : "{\"Name\": \"RootElement\", \"Description\": \"Made with a batch request\"}",
        "Parameters": [
            # TODO -> Select the Location header to pass into the Resource above 
            "$.CreateAFDatabase.Headers.TODO"
        ],
        "ParentIds": [
            "CreateAFDatabase"
        ],
        "Headers": {
            "Cache-Control": "no-cache"
        }
    },
    "CreateChildElement": {
        "Method": "POST",
        "Resource": "{0}/elements",
        "Content" : "{\"Name\": \"ChildElement\"}",
        "Parameters": [
            "$.CreateRootElement.Headers.Location"
        ],
        "ParentIds": [
            "CreateRootElement"
        ],
        "Headers": {
            "Cache-Control": "no-cache"
        }
    },   
    "CreateAttribute": {
        "Method": "POST",
        "Resource": "{0}/attributes",
        "Content" : "{\"Name\": \"NewAttribute\", \"Type\": \"Double\", \"DataReferencePlugIn\": \"PI Point\", \"ConfigString\": \"\\\\\\\\%server%\\\\CDT158\"}",
        "Parameters": [
            "$.CreateChildElement.Headers.Location"
        ],
        "ParentIds": [
            "CreateChildElement"
        ],
        "Headers": {
            "Cache-Control": "no-cache"
        }
    },
    "GetAttribute": {
        "Method": "GET",
        "Resource": "{0}",
        "Parameters": [
            "$.CreateAttribute.Headers.Location"
        ],"ParentIds": [
            "CreateAttribute"
        ],
        "Headers": {
            "Cache-Control": "no-cache"
        }
    },   
    "GetRecordedValuesForAttribute": {
        "Method": "GET",
        "Resource": "https://pisrv01.pischool.int/piwebapi/streams/{0}/recorded?starttime=*-15m&endtime=*",
        "Parameters": [
            "$.GetAttribute.Content.WebId"
        ],
        "ParentIds": [
            "GetAttribute"
        ],
        "Headers": {
            "Cache-Control": "no-cache"
        }
    }
}

response = client.post("batch", body=body)