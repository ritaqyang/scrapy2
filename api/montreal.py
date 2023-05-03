import requests
import pandas
from csv import writer

url = "https://www.collierscanada.com/coveo/rest/search/v2"

querystring = {"sitecoreItemUri":"sitecore://web/{FA041AD7-243D-4265-A0C4-522EF012F8FC}?lang=en-CA&amp;ver=2","siteName":"ColliersCanadaEN"}

payload = "actionsHistory=%5B%7B%22name%22%3A%22Query%22%2C%22time%22%3A%22%5C%222023-05-03T00%3A21%3A44.327Z%5C%22%22%7D%5D&referrer=https%3A%2F%2Fwww.collierscanada.com%2Fen-ca%2Fproperty-search&analytics=%7B%22clientId%22%3A%22a49c4cc9-fb42-aef2-e41a-44572daec786%22%2C%22documentLocation%22%3A%22https%3A%2F%2Fwww.collierscanada.com%2Fen-ca%2Fproperties%23first%3D60%26sort%3Drelevancy%26f%3Alistingtype%3D%5BAll%2520Listings%5D%26f%3Arecenttransactions%3D%5B0%5D%26f%3Alocation%3DQuebec%2520%253E%2520Greater%2520Montreal%22%2C%22documentReferrer%22%3A%22https%3A%2F%2Fwww.collierscanada.com%2Fen-ca%2Fproperty-search%22%2C%22pageId%22%3A%22%22%7D&visitorId=a49c4cc9-fb42-aef2-e41a-44572daec786&isGuestUser=false&aq=(%40propertylocationtypeaheadcomputed%3D%3D%22Quebec%20%3E%20Greater%20Montreal%22)%20(%40propertyforsaleorleasecomputed%3D%3D%22All%20Listings%22)%20(%40recentz32xtransactionz32xflag%3D%3D0)%20(%24qre(expression%3A'%40tier%3D%3D2'%2C%20modifier%3A5000))%20(%24qre(expression%3A'%40tier%3D%3D1'%2C%20modifier%3A3000))%20(((%40z95xpath%3D%3D07C74A35FEDA4D8EA0A85502AAEBF3EA%20(%40z95xtemplate%3D%3D534C0EB71D32434FBE0F62A2AB174F16%20%40country%3DFBD0C5CD4FFB4E788904B623EEF84783))%20NOT%20%40z95xtemplate%3D%3DFE5DD82648C6436DB87A7C4210C7413B))&cq=(%40z95xlanguage%3D%3D%22en-CA%22)%20(%40z95xlatestversion%3D%3D1)%20(%40source%3D%3D%22Coveo_web_index%20-%20COLLIERS-102-PROD%22)&searchHub=Properties&locale=en&maximumAge=0&firstResult=90&numberOfResults=30&excerptLength=200&enableDidYouMean=false&sortCriteria=relevancy&queryFunctions=%5B%5D&rankingFunctions=%5B%5D&groupBy=%5B%7B%22field%22%3A%22%40propertyforsaleorleasecomputed%22%2C%22maximumNumberOfValues%22%3A4%2C%22sortCriteria%22%3A%22nosort%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22allowedValues%22%3A%5B%22All%20Listings%22%2C%22For%20Sale%22%2C%22For%20Lease%22%2C%22For%20Sublease%22%5D%2C%22advancedQueryOverride%22%3A%22(%40propertylocationtypeaheadcomputed%3D%3D%5C%22Quebec%20%3E%20Greater%20Montreal%5C%22)%20(%40recentz32xtransactionz32xflag%3D%3D0)%20(%24qre(expression%3A'%40tier%3D%3D2'%2C%20modifier%3A5000))%20(%24qre(expression%3A'%40tier%3D%3D1'%2C%20modifier%3A3000))%20(((%40z95xpath%3D%3D07C74A35FEDA4D8EA0A85502AAEBF3EA%20(%40z95xtemplate%3D%3D534C0EB71D32434FBE0F62A2AB174F16%20%40country%3DFBD0C5CD4FFB4E788904B623EEF84783))%20NOT%20%40z95xtemplate%3D%3DFE5DD82648C6436DB87A7C4210C7413B))%22%2C%22constantQueryOverride%22%3A%22(%40z95xlanguage%3D%3D%5C%22en-CA%5C%22)%20(%40z95xlatestversion%3D%3D1)%20(%40source%3D%3D%5C%22Coveo_web_index%20-%20COLLIERS-102-PROD%5C%22)%22%7D%2C%7B%22field%22%3A%22%40propertytypescomputed%22%2C%22maximumNumberOfValues%22%3A201%2C%22sortCriteria%22%3A%22occurrences%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22allowedValues%22%3A%5B%5D%7D%2C%7B%22field%22%3A%22%40relatedez120xpertsfullnamecomputed%22%2C%22maximumNumberOfValues%22%3A1001%2C%22sortCriteria%22%3A%22alphaascending%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Atrue%2C%22allowedValues%22%3A%5B%5D%7D%2C%7B%22field%22%3A%22%40recentz32xtransactionz32xflag%22%2C%22maximumNumberOfValues%22%3A2%2C%22sortCriteria%22%3A%22occurrences%22%2C%22injectionDepth%22%3A1000%2C%22completeFacetWithStandardValues%22%3Afalse%2C%22allowedValues%22%3A%5B%221%22%5D%2C%22advancedQueryOverride%22%3A%22(%40propertylocationtypeaheadcomputed%3D%3D%5C%22Quebec%20%3E%20Greater%20Montreal%5C%22)%20(%40propertyforsaleorleasecomputed%3D%3D%5C%22All%20Listings%5C%22)%20(%24qre(expression%3A'%40tier%3D%3D2'%2C%20modifier%3A5000))%20(%24qre(expression%3A'%40tier%3D%3D1'%2C%20modifier%3A3000))%20(((%40z95xpath%3D%3D07C74A35FEDA4D8EA0A85502AAEBF3EA%20(%40z95xtemplate%3D%3D534C0EB71D32434FBE0F62A2AB174F16%20%40country%3DFBD0C5CD4FFB4E788904B623EEF84783))%20NOT%20%40z95xtemplate%3D%3DFE5DD82648C6436DB87A7C4210C7413B))%22%2C%22constantQueryOverride%22%3A%22(%40z95xlanguage%3D%3D%5C%22en-CA%5C%22)%20(%40z95xlatestversion%3D%3D1)%20(%40source%3D%3D%5C%22Coveo_web_index%20-%20COLLIERS-102-PROD%5C%22)%22%7D%5D&facetOptions=%7B%7D&categoryFacets=%5B%5D&retrieveFirstSentences=true&timezone=America%2FToronto&enableQuerySyntax=false&enableDuplicateFiltering=false&enableCollaborativeRating=false&debug=false&allowQueriesWithoutKeywords=true"
headers = {
    "authority": "www.collierscanada.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2OCI6dHJ1ZSwib3JnYW5pemF0aW9uIjoiY29sbGllcnNpbnRlcm5hdGlvbmFsIiwidXNlcklkcyI6W3sidHlwZSI6IlVzZXIiLCJuYW1lIjoiYW5vbnltb3VzIiwicHJvdmlkZXIiOiJFbWFpbCBTZWN1cml0eSBQcm92aWRlciJ9XSwicm9sZXMiOlsicXVlcnlFeGVjdXRvciJdLCJleHAiOjE2ODMxNTg2NDksImlhdCI6MTY4MzA3MjI0OX0.rnQbs9GFRZA2XMRFN4WQIVkMabCIllOZ-urfiXUY-48",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "collierscanadaen#lang=en-CA; collierscanadaen#colliers-country-id={FBD0C5CD-4FFB-4E78-8904-B623EEF84783}; collierscanadaen#colliers-metroarea-id=6ea6d26a-1549-4f01-a79e-daa5c521068f; _gcl_au=1.1.73535292.1681837438; _fbp=fb.1.1681837439117.1199486981; _gd_visitor=c35567d4-28d4-43d4-8ac9-219c17c68ebe; _gd_svisitor=3e043517de7b00007fcd3e64d2010000c3101700; SC_ANALYTICS_GLOBAL_COOKIE=1cd87ae43d8b4d72847669b2e7601cb9|True; _ga_8CJ4KEQLQ8=GS1.1.1681837447.1.1.1681837533.0.0.0; _gid=GA1.2.1057367209.1682956598; _an_uid=5783214813888520430; ln_or=eyIzNjYyMTYyIjoiZCJ9; shell#lang=en; ASP.NET_SessionId=t0m0ztm2srkkw3re0acdhf2h; __RequestVerificationToken=Lx-6oClxRqeaZyCKWdoUgUazoypLye_utdCYBk8MNA-jW14CnMIL3tDpXBm2DIvIPwUk4XgYgQZTip-uwBEI0pdHtPEvftVt68OBYnkiWBQ1; colliers.b58b34ce-6661-4097-a3ad-f5da8df4d194.1b00e5d5-d93d-4e0e-b540-965c839db41e=XwYS3T1OPCfRrNHZq5oeyz6KDeFo1wvAKVlAJy+65dzjqG6rN2FREbO7uPp7EwS/IntdtXbVdT/88nS9kCjOrg==; bm_mi=6A2685CD25750A605CEF0B8EB8114CC3~YAAQU4IsF/y6R8aHAQAAInvg3hNb5YlXEzVx/hiH2+cepYJhr5ztzudNpN5zvhto1so3tzL2oH83bGY0VudHo5XtZl4cAthCdt+Lz6RJabcv/g2XhVegn2k5IcCLR2rdv3V3lHhkW30q3A/oeo+BO9dkfQ/khR+SHjgcC30r4iX2pnsGWYhbrOxwTRFnmNHCB4uh/LtGxddUTt6aFDi+4k3kyfevtaX2v7TNADRD5OKpcxRhAl5EP3L66mOoP336kCSTBJvEoPNAsly/9Hnf4yFkDBa63iMCAuJ0BxQTJpPHndZipAjgt6LigHuJ8xfeRIek/YNlm2K/hzk=~1; ak_bmsc=0F266493C1C29D642D3234EC7FCD19BC~000000000000000000000000000000~YAAQU4IsF+68R8aHAQAAwZHg3hNfpPHiq9waFs+76+iy1XuMAEu8DC35BLTofSvIxiq/n/NuOXdadtJ0Jta2Q7FkYLKQq1gTBkg75zP94bb8lIQBDTkN1I92WypU0tbyZhg67uvwMjtnBS7PvUDBufMRXZ12iHPjjAovt9KRt8s35IG+LAn8AqWPSO4Wu2d4vMjkE5FUl9XXuQDuGO7yY5htOiHvTpVfCy5XYlvQdO1Uziyk3G7qXUNLsHpTyNFGTE3qaf6Fk1x/pVkGKgYWFERl7P1F4gIVOU2U3EiV1zSiwO5PfCeyhTFhszJusuF2+wcWjO8RUy7UBhzKgCfvG+smBWOfzh33IcIC7tiTf6gDAhlXe4dvcggORpb4IvBCo8OcY+xUoB+a6+Aqb2DimIuqmK85obi60/0DifDavPLIb/B9qcX7pQ==; _gcl_aw=GCL.1683071880.CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE; _gac_UA-432762-37=1.1683071880.CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE; _gac_UA-21456727-1=1.1683071880.CjwKCAjwxr2iBhBJEiwAdXECww3RYsGWW1mv3XGmsVVmIcxg-F6oHsVQEUDBYF2tdGtjQucX3gCpQhoCxT8QAvD_BwE; _gd_session=4688a0d5-81a8-443f-8e95-9fb7f9002e94; _ga_JLVMCBMZY3=GS1.1.1683071126.16.1.1683073302.0.0.0; OptanonAlertBoxClosed=2023-05-03T00:21:42.670Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+02+2023+20%3A21%3A43+GMT-0400+(Eastern+Daylight+Time)&version=202303.2.0&isIABGlobal=false&hosts=&consentId=1d2f7c33-c048-45da-80c9-77750f86e030&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=CA%3BQC&AwaitingReconsent=false&browserGpcFlag=0; _ga_5D1DKYRHTZ=GS1.1.1683071126.16.1.1683073304.60.0.0; _ga=GA1.2.587869553.1681837434; _gat_UA-21456727-1=1; bm_sv=2A25A555676D95FFEF95C0C0E7C87BBD~YAAQU4IsF+jsS8aHAQAAtokI3xNAo0PFTEjIeJ1LkHbI/v47ZlD6PIoYSLycNmC3LY2iKaL+Z69HM2Wq/JnWiN7Uiest6XpI4jb4g0UPqV1IkNlgYdl7jDIQ+tI5EXkeWeZE3tijxZGXaWBk9/YW+t2e97HBHXMmhjAewdOgbVa6nuW5PsdpFg9HJ98vKu3Xlc/2frSKjOfd7SXBnl9menm16hQGsspUGg24FQKxOEe4ukUsSgolyB063gOt/NiF1iAqSgA/EatY~1",
    "origin": "https://www.collierscanada.com",
    "referer": "https://www.collierscanada.com/en-ca/properties",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)


result=[]
data = response.json()
#print(data)


for p in data['results']:
    #res.append(p['raw']['description'])
    res=[]
    res.append(p['raw']['systitle'])
    res.append(p['raw']['urllink'])
    res.append(p['raw']['propertyz32xurlz32xtitle'])
    res.append(p['raw']['relatedz32xez120xpertsz32xvar'])
    res.append(p['raw']['propertyz32xfullz32xaddress'])
    res.append(p['raw']['managedz32xbyz32xemail'])
    with open('result.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(res)
        f_object.close()
    


# df = pandas.json_normalize(result)
# df.to_csv('~/Desktop/test.csv')
