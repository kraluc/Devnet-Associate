import sys
import requests
import xml.dom.minidom


# We need to import the JSON library just to handle our request to the API login
# json.dumps(dict) converts a json dictionary into a string
import json

encoded_body = json.dumps({
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd" : "ciscopsdt"
        }
    }
})


### Step 1 - Get Tenant information after Authorization (token)

print(f'\nPOST request raw body: {encoded_body}\n')
# Now lets make the request and store the data
resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)

# print response status code, cookie and header
print(f'\nresponse status code: {resp.status_code}')
print(  f'cookies is a dictionary-like class with keys(): {resp.cookies.keys()}')
print(  f"resp.cookies['APIC-cookie'] -> Token: {resp.cookies.values()[0]}")
print(f'\nheaders: {resp.headers}\n')

# This stores the received APIC-cookie from the login as a value to be used in subsequent REST calls
header = {"Cookie": "APIC-cookie=" + resp.cookies["APIC-cookie"]}

# Now we make a call towards the tenant class on the ACI fabric with the proper header value set.
# We leverage the .xml ending to receive the data back as XML.  We're adding health and faults to the printout to ensure that we get levels of data back from the APIC
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.xml?rsp-subtree-include=health,faults", headers=header, verify=False)

print(f'\n\n{dir(tenants)}')


# Requests stores the text of the response in the .text attribute.  Lets print it to see raw XML (tenants.txt is a string)
print(tenants.text)


###  Step 2 - Parse tenant info into XML format using minidom

print("\n\n\n ###########  STEP 2 ######### \n\n\n")
dom = xml.dom.minidom.parseString(tenants.text)
xml = dom.toprettyxml()
print(xml)