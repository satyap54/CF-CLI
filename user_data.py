import requests

def user_data(handle = None):
	payload = {
		"handles" : ";".join(handle)
	}

	response = requests.get("https://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan", data = payload)
	return response
