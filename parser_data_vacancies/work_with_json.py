import json  
# библиотека для работы с интернет запросами


class WorkWithJson():
    """Класс для работы с json файлами"""

    @staticmethod
    def dump_json(obj:dict, file_name):
        """Метод класса для сохранения json на диске"""
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(obj, file, ensure_ascii=False, indent=4)
    
    @staticmethod
    def load_json(file_name) -> dict:
        """Метод класса для чтения json файла в виде dict"""
        with open(file_name, 'r', encoding='UTF-8') as file:
            return json.load(file)
    
    @staticmethod
    def loads_json(json_str:str) -> list:
        """Метод класса для чтения строки json"""
        return json.loads(json_str)


if __name__ == '__main__':
    work_width_json = WorkWithJson()
    # load_json = work_width_json.load_json('vacancies.json')
    # print(load_json)
    str_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    loads_json = WorkWithJson.loads_json(str_json)
    print(loads_json)
