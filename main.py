import requests

endpoint = "https://api-ssl.bitly.com/v4/shorten"
accessToken = "21d61e1bdda2653ee8523d0d2c62f3b31a16f203"
headers = {
    "Authorization": accessToken,
    "Content-Type": "application/json"
}

url = input("Enter a url to shorten(URL MUST BEGIN WITH 'www.'): ")
if "https://" not in url:
    url = f"https://{url}"

payload = {
    "long_url": url
}

response = requests.post(endpoint, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    shortened_url = data["id"]
    print(f"Shortened URL: https://www.{shortened_url}")
else:
    print("Wrong URL, An Error Occurred!")
