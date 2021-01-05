import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro!')
else:
    print('Deu certo')
    print(site.read())  # Traz o codigo fonte do site
