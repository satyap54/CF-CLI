import requests

def user_data(handle = None):
	payload = ";".join(handle)
	response = requests.get("https://codeforces.com/api/user.info?handles="+payload)
	return response

def get_latest_verdict(handle):
	r = requests.get(f'http://codeforces.com/api/user.status?handle={handle}&from=1&count=1')
	res = r.json()
	if(res['status'] != "OK"):
		raise ConnectionError('Unexpected response from CF/ Some problem with your internet')	
		
	res = res['result'][0]
	
	return {
		"id": res['id'],
		'verdict': res['verdict'],
		'time': res['timeConsumedMillis'],
		'memory': res['memoryConsumedBytes']/1000.0,
		'passedTests': res['passedTestCount']
	}