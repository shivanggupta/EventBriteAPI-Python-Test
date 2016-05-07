import requests

getresponse = requests.get(
    "https://www.eventbriteapi.com/v3/users/me/owned_events/",
    headers = {
        "Authorization": "Bearer <ACCESS_TOKEN_HERE>",
    },
    verify = True,  # Verify SSL certificate
).json()


idlist = []
for i in getresponse['events']:
	idlist.append(int(i['id']))

print idlist

for id in idlist:
	postresponse = requests.post(
	    "https://www.eventbriteapi.com/v3/events/%d/discounts/" %id,
	    headers = {
	        "Authorization": "Bearer <ACCESS_TOKEN_HERE>",
	    },
		data={'discount.code': 'qwertyuiop', 'discount.percent_off' : '20'},
	    verify = True,  # Verify SSL certificate
	)