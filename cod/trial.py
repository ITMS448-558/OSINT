import requests

url = "https://my.callofduty.com/api/papi-client/stats/cod/v1/title/mw/platform/battle/gamer/iShot%2321899/profile/type/mp"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
print(response)

id='7b409a4458db4501abece2a2bcdaea0f'
sec='k3sqP85HZ1NInsVUh8Z7PdLx0pWm5F3K 