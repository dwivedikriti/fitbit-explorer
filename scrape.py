import json
import requests
from pprint import pprint

res = requests.get("https://www.openhumans.org/api/public-data/?format=json&source=fitbit").json()
file_list = res["results"]

for item in file_list:
	res = requests.get(item["download_url"]).json()
	dump = dict(
		user=item["user"],
		data=res
	)
	with open("{}.json".format(item["id"]), 'w+') as f:
		json.dump(dump, f, indent=2)
