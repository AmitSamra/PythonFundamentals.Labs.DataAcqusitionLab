import urllib.request
import urllib.parse
import json
from dotenv import load_dotenv

dotenv_local_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_local_path, verbose=True) 


file_counter = 0
offset_counter = 1

while file_counter < 39:

	headers = {'token':token_value}

	myurl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&' + 'offset=' + str(offset_counter)
	request = urllib.request.Request(myurl, headers = headers)
	file_path = './locations_'+str(file_counter)+'.json'

	with urllib.request.urlopen(request) as f:
		data = json.load(f)

		with open(file_path, 'w') as g:
			json.dump(data,g)

	file_counter += 1
	offset_counter += 1000

