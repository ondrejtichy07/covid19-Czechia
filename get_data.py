import requests


html_testy='https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/testy.csv'
html_nakaza='https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/nakaza.csv'
html_osoby='https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/osoby.csv'
html_pomucky='https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/pomucky.csv'
html_nakazeni='https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/nakazeni-vyleceni-umrti-testy.csv'

t_testy = requests.get(html_testy).content
n_testy = requests.get(html_nakaza).content
o_testy = requests.get(html_osoby).content
p_testy = requests.get(html_pomucky).content
n_testy = requests.get(html_nakazeni).content

with open('/home/pi/Desktop/py/ipynb/data/testy.csv','wb') as f:
    f.write(t_testy)

with open('/home/pi/Desktop/py/ipynb/data/nakaza.csv','wb') as f:
    f.write(n_testy)

with open('/home/pi/Desktop/py/ipynb/data/osoby.csv','wb') as f:
    f.write(o_testy)

with open('/home/pi/Desktop/py/ipynb/data/pomucky.csv','wb') as f:
    f.write(p_testy)

with open('/home/pi/Desktop/py/ipynb/data/nakazeni.csv','wb') as f:
    f.write(n_testy)