import requests
from requests import JSONDecodeError
from pydantic import BaseModel, RootModel, Field, field_validator
from datetime import datetime

# 使用 pydantic 解析資料
class Site(BaseModel):
    site_name:str = Field(alias='sitename')
    county:str
    aqi:int
    status:str
    pm25:float = Field(alias='pm2.5')
    date:str = Field(alias='datacreationdate')

    # 自訂驗證 field_validato
    @field_validator("pm25",mode='before')
    @classmethod
    def check_pm25(cls, value:str) -> str:
        if value == "":
            return "0.0"
        else:
            return value

# RootModel 適用於list
class Records(RootModel):
    root:list[Site]

def download_json() -> dict[any]:
    aqi_url = "	https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON"

    try:
        response = requests.get(aqi_url)
    except Exception as error:
        # 錯誤的訊息在初始化
        raise Exception("連線失敗")
    else:
        if response.status_code == 200:
            try:
                # 這是python的資料結構
                all_data:dict[any] = response.json()
                return all_data
            except JSONDecodeError:
                raise Exception("api_key為測試用,連線已至上限,請稍後再試")
        else:
            raise Exception("下載狀態碼不是200")

def get_data(all_data:dict[any]) -> list[dict]:
    records:Records = Records.model_validate(all_data['records'])
    data:list[dict] = records.model_dump()
    return data

class AQI(object):
    '''
    利用class attribute儲存下載資料
    利用class update_time儲存下載時間
    '''
    aqi_records:list[dict] | None = None
    update_time:datetime | None = None