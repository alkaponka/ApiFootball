import requests


def country():    #список країн
	url = "https://api-football-v1.p.rapidapi.com/v3/teams/countries"
	headers = {
		"X-RapidAPI-Key": "",
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}
	response1 = requests.request("GET", url, headers=headers)
	if response1 == 200:
		return print(response1.text)
	else:
		print(f"Error country {response1.status_code}")


def leagues(q: str):    #список ліг
	url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
	querystring = {"country": q}
	headers = {
		"X-RapidAPI-Key": "",
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	if response.status_code == 200:
		return print(response.text)
	else:
		print(f"error leagues {response.status_code}")

def main():
	country()
	q = str(input("Ведіть країну щоб отримати список ліг:"))
	leagues(q)

if __name__ == '__main__':
	main()
