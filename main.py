import requests

url = "https://api-football-v1.p.rapidapi.com/v3/leagues?code=gb"

headers = {
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "d26fee3105msh10f5ca34bebfe21p11bf79jsnbd00c854e495"
}

response = requests.request("POST", url, headers=headers)

print(response.text)