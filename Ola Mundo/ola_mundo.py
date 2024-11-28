from bs4 import BeautifulSoup
html = "<html><body><h2>Hello, World!</h2></body></html>"
soup = BeautifulSoup(html, "html.parser")
print(soup.h2.text)
# Saída: Hello World!