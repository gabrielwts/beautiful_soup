from bs4 import BeautifulSoup

html = """"<table>
<tr><th>Nome</th><th>Idade</th></tr>
<tr><td>Eric</td><td>18</td></tr>
<tr><td>Weslei</td><td>21</td></tr>
<tr><td>Jean</td><td>18</td></tr>
<tr><td>Adrian</td><td>21</td></tr>
<tr><td>Adão</td><td>18</td></tr>
<tr><td>Kain</td><td>21</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    print(cols)
    # print(f"Nome: {cols[0].text}, Idade: {cols[1].text}")

# Saída: Hello, World!