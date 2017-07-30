import requests

# requests has a built in json parser

URL = 'https://haveibeenpwned.com/api/v2/breachedaccount/'
ACCOUNT = input("Email >>")

response = requests.get(URL+ACCOUNT)
print(response.url)

if response.status_code == requests.codes.ok:
    data = response.json()
    print("{}: {}".format("Number of breaches", len(data)))
    for breach in data:
        print("{}: {}".format("Title", breach["Title"]))
        print("{}: {}".format("Domain", breach["Domain"]))
        print("{}: {}".format("Date of Breach", breach["BreachDate"]))
        print("{}: {}".format("Pwn Count", breach["PwnCount"]))
        print("{}: {}".format("Description", breach['Description']))
    else:
        print("{} {}".format(response.reason, response.stats_code))
        
input("Press any key to continue.")