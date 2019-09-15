import pandas as pd
import magic
import os
import glob
import base64
import html
from IPython.display import HTML


def create_download_link( df, title = "Download CSV file", filename = "data.csv"):  
    csv = df.to_csv()
    b64 = base64.b64encode(csv.encode())
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload,title=title,filename=filename)
    return HTML(html)


path = input('please paste the path to your excel file here: ')

files = []
for file in os.listdir(path):
	if magic.from_file(path + '\\'+ file) == "Microsoft Excel 2007+":
		files.append(path + '\\'+ file)

print(files)

a=0
for f in files:
	if a == 0:
		all_data = pd.read_excel(f)
		a = a + 1
	else:
		all_data = all_data.append(pd.read_excel(f))

all_data.reset_index(drop=True)

create_download_link(all_data)