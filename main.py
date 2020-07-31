import serialize, json

def find_next_contest(li):
	l = 0
	r = len(li) - 1
	mid = None
	res = None

	while(l <= r):
		mid = l + (r  - l)//2

		if(li[mid]["phase"] == "BEFORE"):
			res = mid
			l = mid + 1
		else:
			r = mid - 1

	if(res == None):
		return -1
	else:
		return res

def main():

	serialize.create_contest_details_json()
	
	try:
		with open("./assets/contests_details.json", "r") as f:
			data = json.load(f)
			#print(data["result"])
			idx = find_next_contest(data["result"])

			if(idx == -1):
				print("No upcoming contests")
			else:
				contest = data["result"][idx]
				print(contest)

	except FileNotFoundError:
		print("contests_details.json file is not present inside assets directory")

	finally:
		pass



if __name__ == "__main__":
	main()