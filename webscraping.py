from bs4 import BeautifulSoup

html_doc = """<html>
<head>
<title>Är det fredag?</title>
<meta name="description" content="Är det fredag?">
<meta name="keywords" content="fredag">
<meta name="title" content="Är det fredag?">
<script type="text/javascript" src="https://www.amidog.se/common/jquery-1.7.1.min.js" ></script>
<script type="text/javascript" src="https://www.amidog.se/common/textfill.js"></script>
</head>
<body>
<div id="header" class="headerfill"><span>Är det fredag?</span></div>
<div id="content" class="contentfill"><span>NEJ!</span></div>
<div id="content" class="contentfill"><span>NJA!</span></div>
<div id="content" class="contentfill"><span>NOPE!</span></div>

<div id="footer" class="footerfill">Det är 4 dagar kvar till fredag (2018-12-07).</div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
# print(soup.body)
# print(soup.head)
# print(soup.head.title)


# el = soup.find_all('div')

# el = soup.find_all(class_='headerfill')
# el = soup.find(attrs={"name":"title"})

# select
# el = soup.select('#header')[0]
# el = soup.select('.headerfill')[0]

# get_text()
# while True:
#   try:
#     el = soup.find(class_="headerfil2l").get_text()
#     break
#   except:
#     el = "Told ya"
#     print("No valid name")
#     break

# for item in soup.select('.contentfill'):
#   print(item.get_text())

#Navigation
# el = soup.body.contents[1].contents[0]

print(el)