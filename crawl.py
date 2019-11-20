import requests
import bs4

# read url, return info dict
def retrievePage(url):
	request=requests.get(url)
	soup=bs4.BeautifulSoup(request.text,'html.parser')
	dict={}
	dict['url']=url
	dict['text']=soup.get_text()
	dict['encode']=request.encoding
	dict['title']=soup.title.string

	dict['author']=None
	dict['description']=None
	dict['keywords']=None
	metaList=soup.find_all(name='meta')
	for meta in metaList:
		if meta.get('name')=='author':
			dict['author']=meta['content']
		elif meta.get('name')=='description':
			dict['description']=meta['content']
		elif meta.get('name')=='keywords':
			dict['keywords']=meta['content']

	return dict

if __name__=='__main__':
	dictList=[]
	dictList.append(retrievePage('https://www.google.com/'))
	dictList.append(retrievePage('https://www.w3schools.com/'))
	dictList.append(retrievePage('https://github.com/'))
	dictList.append(retrievePage('https://www.yahoo.com/'))
	
	for dict in dictList:
		print(dict)
