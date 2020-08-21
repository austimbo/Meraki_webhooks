#/usr/bin/env python

import requests
import json
DEBUG=True
TeamsbasUrl="https://api.ciscospark.com/v1/"
messages="messages"
ACCESS_TOKEN="Bearer NjY2ZTE0NWItYjA5OS00ZDk4LTlhYjktYjlmNDZlMjg2MmYzMmI2NGRiMzMtNGYw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

headers = {'Authorization': ACCESS_TOKEN, 'Content-Type': 'application/json'}

def post_to_teams(url_ext, post_data):
    try:
        if DEBUG: print(TeamsbasUrl + url_ext)
        if DEBUG: print(TeamsbasUrl)
        response = requests.post(TeamsbasUrl + url_ext, headers=headers,data=post_data, timeout=(90, 90))
        if DEBUG: print(response.status_code)
        return response
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def send_teams_message(stuff_to_send):

    message_data ={
    "toPersonEmail": "xxxxx@cisco.com",
    "text": stuff_to_send
    }
    response=post_to_teams(messages,json.dumps(message_data))
    if DEBUG: print(response.text)

# Run as a test
'''
if __name__ == '__main__':
    send_teams_message("Test Message Ignore")
'''