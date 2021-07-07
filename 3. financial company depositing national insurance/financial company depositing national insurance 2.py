import requests
import pandas as pd
import json

#Variable Definition
rownum, pgnum, ym = '1000', '1', '201203'

# References
url = 'http://apis.data.go.kr/B190017/service/GetInsurgFnltMngmtInfoService2/getLfinsGnrlPstaList'
queryParams = '?' + 'ServiceKey=' + 'SzfcS4DsKYQpTde0nf0wDoNDomO7hBvjakHgeNqSGwh0USlMlVeywpcOhL2mA5MwxGryRC238PEOnIdUJSsgQA%3D%3D' + \
              '&numOfRows=' + rownum + \
              '&pageNo=' + pgnum + \
              '&resultType=' + 'json' + \
              '&basYm=' + '201712'
url = url + queryParams


#Request & Json_Parser
result = requests.get(url)
json_object = json.loads(result.content)
df=pd.json_normalize(json_object['getLfinsGnrlPstaList']['item'])
print(df)

#To_CSV
df.to_csv('LifeInsurance_Map_PowerBI.csv',encoding='euc-kr')
