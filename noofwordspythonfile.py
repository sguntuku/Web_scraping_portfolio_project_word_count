url='https://www.lipsum.com/'
import requests
getrequest=requests.get(url)

htmltext=getrequest.text

from bs4 import BeautifulSoup
soup=BeautifulSoup(htmltext,'html')
text=soup.get_text()

from nltk.tokenize import RegexpTokenizer
words=RegexpTokenizer('\w+').tokenize(text)

newwords=[]
for i in words:
    newwords.append(i.lower())

import nltk
sw=nltk.corpus.stopwords.words('English')

finalwords=[]
for i in newwords:
    if i not in sw:
        finalwords.append(i)


import matplotlib.pyplot as plt
import seaborn as sns
plt.plot()
sns.set()


graphicaloutput=nltk.FreqDist(finalwords)
graphicaloutput.plot(25)
