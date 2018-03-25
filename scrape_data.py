import urllib2
from bs4 import BeautifulSoup


#create list of all the cocktails
cocktails = [
'mimosa',
'paloma',
'rob-roy',
'blood-and-sand',
'gin-fizz',
'whiskey-smash',
'aviation',
'manhattan',
'mojito',
'gimlet',
'mint-julep',
'sazerac',
'negroni',
'drambuie-rusty-nail',
'old-fashioned',
'daiquiri',
'french-75',
'dry-martini',
'scofflaw',
'clover-club',
'gibson',
'boulevardier',
'vesper',
'moscow-mule',
'mudslide']

cocktail_dict = {}

for cock in cocktails:
	html_page = 'https://www.liquor.com/recipes/' + cock + '/'
	page = urllib2.urlopen(html_page) #stores html from website in page
	
	soup = BeautifulSoup(page, 'html.parser') # parses the html into our beautiful soup object

	ingredients = soup.find_all("div", class_="col-xs-8 x-recipe-ingredient")
	ingredients_cleaned = []
	for item in ingredients:
		text = item.get_text().split()
		text = ' '.join(text)
		ingredients_cleaned.append(text)
	
	cocktail_dict[cock] = ingredients_cleaned

print cocktail_dict



'''


html_page = 'https://www.liquor.com/recipes/moscow-mule/' #url of page

page = urllib2.urlopen(html_page) #stores html from website in page
soup = BeautifulSoup(page, 'html.parser') # parses the html into our beautiful soup object

ingredients = soup.find_all("div", class_="col-xs-8 x-recipe-ingredient")
for item in ingredients:
	text = item.get_text().split()
	text = ' '.join(text)
	print(text)

'''