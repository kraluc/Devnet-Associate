import yaml

with open('vincent.yaml','r') as file:
    data = yaml.safe_load(file)

print(type(data))
print(data)
print(data['user']['name'])

data['user']['name']='kraluc'

with open('vincent.yaml','w') as f_write:
    yaml.dump(data, f_write, encoding='utf-8')

with open('vincent.yaml','r') as file:
    data = yaml.safe_load(file)
print(type(data))
print(data)
print(f"new name is {data['user']['name']}")

data['user']['name']='vincent'
with open('vincent.yaml','w') as f_write:
    yaml.dump(data, f_write, encoding='utf-8')

print(f"new name is {data['user']['name']}")