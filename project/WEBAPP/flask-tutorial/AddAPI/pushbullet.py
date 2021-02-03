import requests
import json
import datetime

def push_message(title, body,token):
	# token = "o.GkTg42mI2Jpb3GlmMvxLHaojJdQ66uHw"#pushbulletのアクセストークン
	if token is not None:
		url = "https://api.pushbullet.com/v2/pushes"	
		headers = {"content-type": "application/json", "Authorization": 'Bearer '+token}
		data_send = {"type": "note", "title": title, "body": body}

		_r = requests.post(url, headers=headers, data=json.dumps(data_send))