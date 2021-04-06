import requests

def user_data(handle = None):
	payload = ";".join(handle)
	response = requests.get("https://codeforces.com/api/user.info?handles="+payload)
	return response
