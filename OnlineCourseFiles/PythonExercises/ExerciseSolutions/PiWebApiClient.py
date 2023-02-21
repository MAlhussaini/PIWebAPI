import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
import json

class PiWebApiClient():

    def __init__(self, base_url="https://pisrv01.pischool.int/piwebapi/", use_basic=False, verify=None, **kwargs):
        self.base_url = base_url
        self.__s = requests.Session()
        self.__s.headers.update({"accept": "application/json"})
        self.__s.hooks = {"response": self.__print_response}
        if verify is not None:
            self.__s.verify = verify
        else:
            self.__s.verify = False
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        if use_basic:
            self.username = kwargs.get("username")
            self.password = kwargs.get("password")
            self.__s.auth = HTTPBasicAuth(self.username, self.password)
        else:
            self.__s.auth = HTTPKerberosAuth(delegate=True, mutual_authentication=OPTIONAL)

    def get(self, endpoint="", headers={}):
        print("Request:\n GET " + self.base_url + endpoint)
        return self.__s.get(self.base_url + endpoint, headers=headers)

    def delete(self, endpoint="", headers={}, body=""):
        print("Request:\n DELETE "+ self.base_url + endpoint)
        headers["x-requested-with"] = "piwebapiclient"
        return self.__s.delete(self.base_url + endpoint, headers=headers)

    def post(self, endpoint="", headers={}, body=""):
        print("Request:\n POST "+ self.base_url + endpoint)
        self.__add_headers(headers)
        return self.__s.post(self.base_url + endpoint, headers=headers, json=body)

    def put(self, endpoint="", headers={}, body=""):
        print("Request:\n PUT "+ self.base_url + endpoint)
        self.__add_headers(headers)
        return self.__s.put(self.base_url + endpoint, headers=headers, json=body)

    def patch(self, endpoint="", headers={}, body=""):
        print("Request:\n PATCH "+ self.base_url + endpoint)
        self.__add_headers(headers)
        return self.__s.patch(self.base_url + endpoint, headers=headers, json=body)

    def __add_headers(self, headers):
        headers.update({"content-type": "application/json"})
        headers.update({"x-requested-with": "piwebapiclient"})

    def __print_response(self, res, *args, **kwargs):
        print("Response:")
        print(" Status = " + str(res.status_code))
        print(json.dumps(res.json(), indent=2, separators=(", ", " : ")))
        print("")