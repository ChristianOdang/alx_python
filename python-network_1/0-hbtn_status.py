""" 
This modules uses the request moduleno to get
and fetch requests from alu-intranet
"""
import requests


request = requests.get("https://alu-intranet.hbtn.io/status")
print("Body response:\n\t- type: {}\n\t- content: {}".format(type(request.text), request.text))
