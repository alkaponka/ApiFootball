import requests

def country():    #список країн
	url = "https://api-football-v1.p.rapidapi.com/v3/teams/countries"

	headers = {
		"X-RapidAPI-Key": "",
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}

	response_country = requests.request("GET", url, headers=headers)

	if response_country == 200:
		return print(response_country.text)
	else:
		print(f"Error country {response_country.status_code}")

def leagues(q: str):    #список ліг
	url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

	querystring1 = {"country": q}

	headers = {
		"X-RapidAPI-Key": "",
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}
	response_leagues = requests.request("GET", url, headers=headers, params=querystring1)
	if response_leagues.status_code == 200:
		return print(response_leagues.text)
	else:
		print(f"error leagues {response_leagues.status_code}")

def comand_liga_status(year, liga :int, str): #список команд в лізі + сезон

	url = "https://api-football-v1.p.rapidapi.com/v3/standings"

	querystring2 = {"season": "2020", "league": "39"}
	headers = {
		"X-RapidAPI-Key": "d26fee3105msh10f5ca34bebfe21p11bf79jsnbd00c854e495",
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}
	response_comand = requests.request("GET", url, headers=headers, params=querystring2)
	if response_comand.status_code == 200:
		return print(response_comand.text)
	else:
		print(f"error comand {response_comand.status_code}")

def main():
	country()
	q = str(input("Ведіть країну щоб отримати список ліг:"))
	leagues(q)
	year = int(input("Ведіть рік сезону:"))
	liga = str(input("Ведіть id ліги :"))
	comand_liga_status(year, liga)


if __name__ == '__main__':
	main()
