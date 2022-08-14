import requests
import json

url = "https://summerofcode.withgoogle.com/api/program/2022/organizations/"
content = requests.get(url).content
org_list = json.loads(content)
json_data = []
for org in org_list:
    json_org={}
    json_org['name']=org['name']
    json_org['description']='.'.join(org['description'].split('.')[:2])+'.'
    json_org['tech-stack']=org['tech_tags']
    json_org['fields']=org['topic_tags']
    json_data.append(json_org)
f = open('orgData.json','w')
f.write(json.dumps(json_data,indent=4,separators=(',', ': ')))
f.close()