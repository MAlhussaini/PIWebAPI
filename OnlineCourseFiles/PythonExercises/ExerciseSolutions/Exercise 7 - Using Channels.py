from PiWebApiClient import PiWebApiClient 
import json
import websocket
import ssl
import base64
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#####################################################################
#########                                                   #########
#########            Exercise 7: Using channels             #########
#########                                                   #########
#####################################################################

# This script uses the websocket-client library from the github page below:
# https://github.com/websocket-client/websocket-client

# Make an regular HTTP request to get the WebId
client = PiWebApiClient(base_url="https://pisrv01.pischool.int/piwebapi/")
response = client.get("points?path=\\\\PISRV01\\CDT158&selectedFields=WebId")
webId = response.json()['WebId']

# Use the WebId to create our channel uri
channelUri = "wss://pisrv01.pischool.int/piwebapi/streams/" + webId + '/channel'

# Create basic authorization header for websocket request
headers = {}
headers["Authorization"] = "Basic " + base64.b64encode(str("pischool\\student01:PasswordGoesHere").encode("utf-8")).decode("utf-8")

# Define the functions to call when our websocket opens, gets a message, receives an error, or closes
def on_open(ws):
    print("Opening websocket to " + channelUri)
    print(" Waiting for next message... (Press CTRL+C to exit)")

def on_message(ws, message):
    print(" Message Recieved:")
    print(json.dumps(json.loads(message), indent=2, separators=(", ", " : ")))
    print("\n Waiting for next message... (Press CTRL+C to exit)")


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Closing websocket")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(channelUri, 
                            header= headers,
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close,
                            on_open = on_open)
                            
    # This opens the websocket indefinitely, until it is closed by the server or we exit the program
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})