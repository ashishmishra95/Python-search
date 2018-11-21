#Google search using python script
import requests, sys, webbrowser, bs4
res = requests.get('https://www.google.com/search?q='+''.join(sys.argv[1:]))
# if status.code returns 200 that means no problem with internet connection
print(res.status_code)
#res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElements = soup.select('.r a')
# No. of pages you want to be searched
linkToOpen = min(4, len(linkElements))
for i in range(linkToOpen):
	webbrowser.open('https://www.google.com'+linkElements[i].get('href'))
	

	

	
