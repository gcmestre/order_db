import json

data = []
managers_list = {}
watchers_list = {}

with open('source_file_2.json') as json_file:
    data = json.load(json_file)
    for i in data:
    	print(i)

data_order = sorted(data, key = lambda i: i['priority'])

for project in data_order:
	for manager in project['managers']:
		if manager in managers_list:
			managers_list[manager].append(project['name'])
		else:
			managers_list[manager] = [project['name']]
			

with open('managers.json', 'w') as outfile:
    json.dump(managers_list, outfile)


for project in data_order:
	for manager in project['watchers']:
		if manager in watchers_list:
			watchers_list[manager].append(project['name'])
		else:
			watchers_list[manager] = [project['name']]
			

with open('watcher.json', 'w') as outfile:
    json.dump(watchers_list, outfile)