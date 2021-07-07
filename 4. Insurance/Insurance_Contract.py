import requests
import pandas as pd
import json
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd

#Variable Definition
rownum, pgnum, ym = '300', '1', '201203'

#Time Difference
now = pd.datetime.now()
base = pd.datetime.strptime(ym,'%Y%m')
diff = rd(now, base)
monthdiff = diff.years*12 + diff.months

#List of DataFrame by months
ResultMonths = []

for i in range(0, monthdiff+1, 3):
    #Time Repetition
    ymtemp = base + pd.DateOffset(months=i)
    ymtemp = dt.strftime(ymtemp,'%Y%m')

    # References
    url =  'https://api.odcloud.kr/api/3034284/v1/uddi:4c3a0eb0-90d4-44b0-8b08-f6f1c0270031?page=1&perPage=10&serviceKey=kj9nvVsyAjFy1XXlSm6KJCWbcCy4y%2B9Pl3qXfo77cRrOUDI4Da7JqgJCN0eYoO1X%2F1yM2wMcKFdyRpdGoYrs7Q%3D%3D'
    queryParams = '?' + 'ServiceKey=' + 'SzfcS4DsKYQpTde0nf0wDoNDomO7hBvjakHgeNqSGwh0USlMlVeywpcOhL2mA5MwxGryRC238PEOnIdUJSsgQA%3D%3D' + \
                  '&numOfRows=' + rownum + \
                  '&pageNo=' + pgnum + \
                  '&resultType=' + 'json' + \
                  '&basYm=' + str(ymtemp) + \
                  '&title=' + '생보_주요영업활동_신계약'
    url = url + queryParams

    try:
        #Request & Json_Parser
        result = requests.get(url)
        json_object = json.loads(result.content)
        df=pd.json_normalize(json_object['response']['body']['tableList'][0]['items']['item'])

        # Row Selection (Remove Subsum of xcsmPlnpnDcdNm)
        mask = df['fncoCd'].str.contains('S')
        df = df[~mask]

        #Append
        ResultMonths.append(df)

    except:
        print('Error' + ymtemp)
        continue

#Join
result = pd.concat(ResultMonths)

#Column Rename
#result.columns = ['날짜','법인등록번호','고유번호','기업명','직원수','직급구분','직급']

#To_CSV
result.to_csv('Insurance_Contract_PowerBI.csv',encoding='euc-kr')