import requests
from bs4 import BeautifulSoup

#this is just used to copy FHIR webpages into FHIR_Codings codings
import sys

if len(sys.argv) != 2:
    print("Usage: python potato/FHIR_Codings_Download/FHIR_Coding_Helper.py <FHIR value set url>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
codes_table = soup.find('table', {'class': 'codes'})

codings = {}
if codes_table:
    table = ""
    rows = codes_table.find_all('tr')[1:]
    for row in rows:
        cols = row.find_all(['td', 'th'])
        code = cols[0].get_text(strip=True)
        system = cols[1].get_text(strip=True)
        display = cols[2].get_text(strip=True)
        item = {
            'code': code,
            'display': display, 
        }

        if len(cols) > 3:
            definition = cols[3].get_text(strip=True)
            item['definition'] = definition
        
        if system in codings:
            codings[system].append(item)
        else:
            codings[system] = [item]

else:
    print("Could not find codes table on the page")


for coding in codings:
    writeCodingFile = "potato/FHIR_Codings/" + coding.replace("http://", "").replace("/", "_").replace("-", "_").replace(".", "_") + ".py"
    f = open(writeCodingFile, 'w')
    print(system + " written to " + writeCodingFile)
    f.write("system = \"" + system + "\"")
    f.write('\n')
    f.write("version = \"???\"")
    f.write('\n')
    #print(coding)
    f.write("coding = " + str(codings[coding]))
    f.write('\n')
    #print(codings[coding])
