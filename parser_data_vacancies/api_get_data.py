# библиотека, для работы с временем
from time import sleep 
# библиотека для работы с файлами json
from requests import get
# IPython нужен для расширения возможностей интерпритатора в сфере визуализации 
# данных.
# display - для отображения графиков и картинок и тд.
# clear_output - для очищения вывода
from IPython.display import display, clear_output
# tqdm - для удобного отображения индикатора прогресса
from tqdm import trange, tqdm
# pandas - для работы с табличными данными
import pandas as pd


class WorkDataApi():
    """Класс для работы с api данными"""

    @staticmethod
    def get_data_json_params(params, link):
        """Метод класса для получения данных по api в виде json с параметрами"""

        res = get(link, params=params)
        if not res.ok:
            print('Error', res)
        data = res.json()["items"]
        pages = res.json()['pages']

        for page in trange(1, pages):
            params['page'] = page
            res = get(link, params=params)
            if res.ok:
                response_json = res.json()
                data.extend(response_json["items"])
            else:
                print(res)
        
        return data
    
    @staticmethod
    def get_full_data_json(data_json, link):
        """Метод для скачивания всех данных в виде json (медленно)"""
        
        data_full = list()
        for entry in tqdm(data_json):
            page_id = entry['id']
            description = get(f'{link}/{page_id}')
            data_full.append(description.json())
            sleep(0.2) # обход ограничения на колличество запросов и ошибку 403
            clear_output()
        
        return data_full
    
    @staticmethod
    def get_data_json(file_id, link):
        """Метод класса для скачивания json файла по id"""

        url = f'{link}{file_id}'
        res = get(url)
        data = res.json()
        return data


if __name__ == '__main__':
    work_data_api = WorkDataApi()
    text = 'python'
    link = 'https://api.hh.ru/vacancies'
    params = {
        "per_page": 100,
        "page": 0,
        "period": 30,
        "text": text,
        "experience": None,
        "employment": None,
        "schedule": None
    }

    data = work_data_api.get_data_json_params(params=params, link=link)
    # print(len(data))
    #WorkWithJson().dump_json(data, 'vacancies.json')
    # data_full = work_data_api.get_full_data_json(data_json=data, link=link)
    # WorkWithJson().dump_json(data, 'vacancies_full.json')
    data_full = work_data_api.get_data_json(file_id='1d2NfxfM2n48m5WS6oCCc3rcQ4hdnTQ1v',
                                            link='https://drive.google.com/uc?export=view&id=')
    # WorkWithJson().dump_json(obj=data_full, file_name='vacancies_full.json')
    # pd.DataFrame(data).to_excel('Cписок вакансий.xlsx')
    # pd.DataFrame(data_full).to_excel('Подробное описание вакансий.xlsx')
