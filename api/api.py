import requests
import pandas

url = "https://www.collierscanada.com/coveo/rest/search/v2"

querystring = {"sitecoreItemUri":"sitecore://web/{FA041AD7-243D-4265-A0C4-522EF012F8FC}?lang=en-CA&amp;ver=1","siteName":"ColliersCanadaEN"}

headers = {
    "cookie": "collierscanadaen#lang=en-CA; collierscanadaen#colliers-country-id={FBD0C5CD-4FFB-4E78-8904-B623EEF84783}; collierscanadaen#colliers-metroarea-id=6ea6d26a-1549-4f01-a79e-daa5c521068f; _gcl_au=1.1.73535292.1681837438; _fbp=fb.1.1681837439117.1199486981; _gd_visitor=c35567d4-28d4-43d4-8ac9-219c17c68ebe; _gd_svisitor=3e043517de7b00007fcd3e64d2010000c3101700; SC_ANALYTICS_GLOBAL_COOKIE=1cd87ae43d8b4d72847669b2e7601cb9|True; _ga_8CJ4KEQLQ8=GS1.1.1681837447.1.1.1681837533.0.0.0; _gid=GA1.2.1057367209.1682956598; _an_uid=5783214813888520430; ln_or=eyIzNjYyMTYyIjoiZCJ9; _gd_session=1f7c0df8-d323-4d8e-824b-3a36f7051444; shell#lang=en; ASP.NET_SessionId=t0m0ztm2srkkw3re0acdhf2h; __RequestVerificationToken=Lx-6oClxRqeaZyCKWdoUgUazoypLye_utdCYBk8MNA-jW14CnMIL3tDpXBm2DIvIPwUk4XgYgQZTip-uwBEI0pdHtPEvftVt68OBYnkiWBQ1; colliers.b58b34ce-6661-4097-a3ad-f5da8df4d194.1b00e5d5-d93d-4e0e-b540-965c839db41e=XwYS3T1OPCfRrNHZq5oeyz6KDeFo1wvAKVlAJy+65dzjqG6rN2FREbO7uPp7EwS/IntdtXbVdT/88nS9kCjOrg==; _gcl_aw=GCL.1683062817.CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE; ak_bmsc=8C0D66E1CBF0573A60CFA08210BF532D~000000000000000000000000000000~YAAQU0A2Fyrr1t2HAQAAtINc3hNipn21M7WpxwAYe9/f0k2k2fmCn+HOKyV6ZXQ/x6AJvgCULfoaEBAL+5DXQMSSS0jA/E/md1lSMqpsPvutLmgSwWU0lB4oKbEwohVM+Ske+YhBVV8CAfX5pK2KU37EezguqbdVg7qLwJNRg8MEcOVLkfnw7Axa97Tyvaqrplhxl4qdi/l5j5Apv428yiKMflVXrjhOSq4poPEf6nnqa+cKWKZ/uYVYZt1zwa85wBPMbJD+isx8ldMiGwaiKBb3jMl2KqYQxqDwEdIq+b+23RZs9iAdLtb+Gkg1ru8bnxeKzLLNAilSEDR1jzorHqrYQ+wonHQgFf0DtUiVCs7/FH7aPXkRJUcI4d2uZJ2BWqbt0UtAkOQf3kaQ5//XV32AyF6zW/dm+0ID0DLySdz3A6pXpKF63Vh4hqDyFs35i0qcarVQG14Wf2Zdsnrl1hFWc/xtSzhhSLtw6SIJ0RX6w/RFUZMe02tj4LOUgb/7rBM=; _gac_UA-21456727-1=1.1683062869.CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE; _gac_UA-432762-37=1.1683062869.CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE; _gat_UA-21456727-1=1; _gat_UA-432762-37=1; _ga=GA1.1.587869553.1681837434; _ga_JLVMCBMZY3=GS1.1.1683065819.14.1.1683065821.0.0.0; _ga_5D1DKYRHTZ=GS1.1.1683065817.14.1.1683065821.56.0.0; OptanonAlertBoxClosed=2023-05-02T22:17:01.901Z; bm_sv=0741FCBA70623D93507A1F3E6A0EDE6D~YAAQU0A2F93+6d2HAQAAIF+K3hM2TEIFHRdt9gTt/AoH7v+4sO29EsFtqVNQIukHW0Zer9iAnqDKi8ASDLDQfsyp2nfoduXrXcynlrnsg6Enny6cnC1t6wkSpkbBa86Vd/EfyVJz5znjCTYG3KG6m0vcEuHB5TsGQJNpaqeCcPkwqCKQOh9cyq/rAzAhjjeDPMNUBHeki/VUkGqDw0PQ6Gx6bdUlRJyzhco+QJqwgryZsEnE1LJEmwZG6IR+1VYNqWbId/14VH0O~1; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+02+2023+18%3A17%3A03+GMT-0400+(Eastern+Daylight+Time)&version=202303.2.0&isIABGlobal=false&hosts=&consentId=1d2f7c33-c048-45da-80c9-77750f86e030&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=CA%3BQC&AwaitingReconsent=false&browserGpcFlag=0",
    "authority": "www.collierscanada.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2OCI6dHJ1ZSwib3JnYW5pemF0aW9uIjoiY29sbGllcnNpbnRlcm5hdGlvbmFsIiwidXNlcklkcyI6W3sidHlwZSI6IlVzZXIiLCJuYW1lIjoiYW5vbnltb3VzIiwicHJvdmlkZXIiOiJFbWFpbCBTZWN1cml0eSBQcm92aWRlciJ9XSwicm9sZXMiOlsicXVlcnlFeGVjdXRvciJdLCJleHAiOjE2ODMxNTE0NjgsImlhdCI6MTY4MzA2NTA2OH0.F2SYs73noD8bxkw6lxCoJETT73Rd8lT32ZbtpR7vpfo",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.collierscanada.com",
    "referer": "https://www.collierscanada.com/en-ca/properties",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.json())
res = []
data = response.json()
for p in data['results']:
    res.append(p)


df = pandas.json_normalize(res)
df.to_csv('~/Desktop/test.csv')



