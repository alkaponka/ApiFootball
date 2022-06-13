import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("key_football")

headers = {
		"X-RapidAPI-Key": key,
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}
def country():    #list county

	response_country = requests.get("https://api-football-v1.p.rapidapi.com/v3/teams/countries", headers=headers)

	if response_country == 200:
		return print(response_country.text)
	else:
		print(f"Error country {response_country.status_code}")

def leagues(q: str):    #list leagues

	querystring1 = {"country": q}

	response_leagues = requests.get("https://api-football-v1.p.rapidapi.com/v3/leagues", headers=headers, params=querystring1)

	if response_leagues.status_code == 200:
		return print(response_leagues.text)
	else:
		print(f"error leagues {response_leagues.status_code}")

def comand_liga_status(year, liga :int): # list comand and season

	url = "https://api-football-v1.p.rapidapi.com/v3/standings"

	querystring2 = {"season": year, "league": liga}

	response_comand = requests.get("https://api-football-v1.p.rapidapi.com/v3/standings", headers=headers, params=querystring2)

	if response_comand.status_code == 200:
		return print(response_comand.text)
	else:
		print(f"error comand {response_comand.status_code}")

def main():
	country()
	q = str(input("Enter the country:"))
	leagues(q)
	year = int(input("Year of the season:"))
	liga = int(input("League id :"))
	comand_liga_status(year, liga)


if __name__ == '__main__':
	main()
