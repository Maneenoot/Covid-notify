import requests
r = requests.get('https://covid19.th-stat.com/api/open/today')

print("UpdateDate : ", r.json()['UpdateDate'])
print("Confirmed : ", r.json()['Confirmed'])
print("NewConfirmed : ", r.json()['NewConfirmed'])
print("NewDeaths : ", r.json()['NewDeaths'])

# Code for Line Notification
url = 'https://notify-api.line.me/api/notify'
token = ''   # Token from Line Notify
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}

msg = "UpdateDate : " + str(r.json()['UpdateDate'])
msg2 = "Confirmed : " + str(r.json()['Confirmed'])
msg3 = "NewConfirmed : " + str(r.json()['NewConfirmed'])
msg4 = "NewDeaths : " + str(r.json()['NewDeaths'])

r1 = requests.post(url, headers=headers, data = {'message':msg})
r2 = requests.post(url, headers=headers, data = {'message':msg2})
r3 = requests.post(url, headers=headers, data = {'message':msg3})
r4 = requests.post(url, headers=headers, data = {'message':msg4})