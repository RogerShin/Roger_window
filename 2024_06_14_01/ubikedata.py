import requests
from requests import Response
from pydantic import BaseModel, RootModel, Field, field_validator

def __download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res:Response = requests.get(url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data:dict[any] = res.json()
        return all_data

class Info(BaseModel):
    sna:str
    sarea:str
    mday:str
    ar:str
    act:str
    updateTime:str
    total:int
    rent_bikes:int = Field(alias="available_rent_bikes")
    lat:float = Field(alias="latitude")
    lng:float = Field(alias="longitude")
    retuen_bikes:int = Field(alias="available_return_bikes")

    @field_validator("sna", mode='before')
    @classmethod
    def flex_string(cls, value:str) -> str:
        return value.split(sep="_")[1]

class Youbike_Data(RootModel):
    root:list[Info]

def load_data() -> list[dict]:
    all_data:dict[any] = __download_json()
    youbike_data:Youbike_Data = Youbike_Data.model_validate(all_data)
    data = youbike_data.model_dump()
    return data


# def get_selected_site(sna:str, data:list[dict]) -> tuple[float]:
#     print(sna)
#     # print(data)
#     return (0, 0)


class FilterData(object):
    @staticmethod
    def get_selected_site(sna:str, data:list[dict]) -> tuple[float]:
        print(sna)
        # print(data)
        return (0, 0)