import requests
#import urllib.parse
#from config import apikeys as cfg

targetUrl = "https://github.com/mickalleny2k/pands-problem-sheet/blob/main/andrewtomichael.txt"
#targetUrl = "https://www.atu.ie/"

#apikey = cfg["githubkey"]
#apiurl = 'https://api.html2pdf.app/v1/generate'

#params = {'html': targetUrl,'apiKey': apikey}
#parsedparams = urllib.parse.urlencode(params)

#requestUrl = apiurl +"?" + parsedparams 
#print (requestUrl)

response = requests.get(targetUrl)

print (response.status_code)
result =response.content

with open("andrewtomichael.txt", "wb") as handler:
    #handler.replace("Andrew", "Michael")
    handler.write(result)