import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.YTJkoo4za00')

print(page.status_code)

soup_content = BeautifulSoup(page.content, 'html.parser')

# The entire page
# print(soup_content)

forecast_week = soup_content.find(id = 'seven-day-forecast-container')

# print(forecast_week)

# Period Names
pnames_container = forecast_week.findAll(class_ = 'period-name')

p_names = []

for name in pnames_container:
    n_text = name.get_text()

    p_names.append(n_text)

# print(p_names)

# Temperature
temp_container = forecast_week.findAll(class_ = 'temp')

temps = []
for t in temp_container:
    content = t.get_text()
    temps.append(content)

print(temps)
print(len(temps))

# Descriptions
short_desc_container = forecast_week.findAll(class_ = 'short-desc')
long_desc_container = forecast_week.findAll('img')

# print(short_desc_container)
# print(long_desc_container)

# Short Descriptions
short_descs = []
for s_desc in short_desc_container:
    content = s_desc.get_text()
    short_descs.append(content)

# print(short_descs)
print(len(short_descs))

# Detailed description
descs = []
for d_desc in long_desc_container:
    content = d_desc['title']
    descs.append(content)

# print(descs)

# Wrapping into a dataframe

import pandas as pd

forecast_df = pd.DataFrame(
    {
        'Period' : p_names,
        'Temparature' : temps,
        'Desc': short_descs,
        'Remark' : descs
    }
)


print(forecast_df)






