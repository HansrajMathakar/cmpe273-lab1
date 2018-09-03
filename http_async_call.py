import requests

for x in range(3):
    r = requests.get('https://webhook.site/88aa1176-fa21-4947-8e16-02959eeed119')
for y in range(3):
    print(r.headers['Date'])



