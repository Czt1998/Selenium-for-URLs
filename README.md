# Selenium for persons
<br>Get all persons\` name with it\` s URL of personal page
## Personal document
<br>Using movies\` name from folders to collect related persons\` name with speific URL, and then store them into mongodb
<br>
## Main codes
* info.py <br>
Get movies` name from folders and then crwal related information by selenium
* mondoss.py
	<br>  Store all the information



## Operating environment
<br>Based on python3.5, first need to install:
* io
* re
* selenium (for webdriver)
* pyquery
* Chrome browser
* geckdriver.log
* pymongo

## Operating Instructions
<br>Open pycharm IDE and run info.py

## Bullet points
<br>Key skills that I` ve learned
* Selenium
* pyquery
* pymongo

## Case:
* Take [西游降魔篇](http://movie.mtime.com/208325/fullcredits.html) as an example.
* Get it\`s movie name from the folder first, and then enter person\`s page.

### Each item
Actor
Director
Members
<br>
![](https://github.com/G1704/Test/blob/master/Item.png "Actor & Director")
<br>
![](https://github.com/G1704/Test/blob/master/Item2.png "Members")


### Save as json file
Page [‘演员’] = ele1
<br>Page [‘导演’] = elem2
<br>Page [membername] = elem3
