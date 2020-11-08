import json
import yaml

with open('vincent.yaml','r') as f_read:
    data = yaml.safe_load(f_read)

print(f"data read from yaml: {data}" )

with open('vincent.json', 'w') as f_write:
    json.dump(data, f_write, indent=4)

with open('vincent.json', 'r') as f_read:
    data = json.load(f_read)

user = data['user']
name = user['name']
for role in user['roles']:
    print(f"{name}'s role: {role}")