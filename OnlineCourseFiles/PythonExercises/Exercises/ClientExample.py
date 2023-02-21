import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
from PiWebApiClient import PiWebApiClient 
import json
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Using requests only
headers={}
headers["content-type"] = "application/json"
result = requests.get("https://pisrv01.pischool.int/piwebapi/assetservers", auth=HTTPKerberosAuth(delegate=True, mutual_authentication=OPTIONAL), headers=headers, verify=False)
print("Request:")
print(" " + result.request.method + " " + result.request.url)
print("Response:")
print(" Status = " + str(result.status_code))
print(json.dumps(result.json(), indent=2, separators=(", ", " : ")))
print("")


# Using the wrapper class
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")
response = client.get(endpoint="assetservers") 