import requests
import pandas as pd
import json

#Variable Definition
rownum, pgnum = '300', '1'

#List of DataFrame by months
ResultMonths = []

# References
url =  'http://apis.data.go.kr/B190017/service/GetInsurgTrgetFnltInfoService/getInsurgTrgetFnltInfoList'
queryParams = '?' + 'ServiceKey=' + 'SzfcS4DsKYQpTde0nf0wDoNDomO7hBvjakHgeNqSGwh0USlMlVeywpcOhL2mA5MwxGryRC238PEOnIdUJSsgQA%3D%3D' + \
              '&numOfRows=' + rownum + \
              '&pageNo=' + pgnum + \
              '&resultType=' + 'json'
url = url + queryParams


#Request & Json_Parser
result = requests.get(url)
json_object = json.loads(result.content)
df=pd.json_normalize(json_object['getInsurgTrgetFnltInfoList']['item'])

# Column Selection
df = df.loc[:, ['fnccmpNm','fncsecDscdNm','hmpgUrladr','fncIstAdr','cttpc']]

#Rename Column
df.columns = ['회사명','금융권','홈페이지','주소','전화번호']

#To_CSV
df.to_csv('Insurance_Deposit_Financial_Company_PowerBI_test.csv',encoding='euc-kr')