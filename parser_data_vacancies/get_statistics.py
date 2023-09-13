# Counter - класс для подсчёта хэшируемых данных.
from collections import Counter
# collections - предоставляет альтернативные структуры данных деки, сдеки и тд.
# Counter - класс для подсчёта хэшируемых данных.
from collections import Counter
# wordcloud - для  визуализации картинки слов из блока слов где размер и цвет
# пропорциогнален их частоте встречаемости
from wordcloud import WordCloud
from work_with_json import WorkWithJson
from work_with_json import WorkWithJson


class WorkWithStatistics():
    """Класс для работы со статистикой данных"""

    @staticmethod
    def get_frequencies(data_dict, key_tracking, key_adding):
        """Метод класса для возрата частотности встречаемости"""

        all_data = list()
        
        for entry in data_dict:
            for skill in entry[key_tracking]:
                all_data.append(skill[key_adding])
        
        return Counter(all_data)
    
    @staticmethod
    def gen_img_statistics(color, frequencies):
        """Метод класса для создании img со статистикой встречаемости"""

        cloud = WordCloud(background_color=color)
        cloud.generate_from_frequencies(frequencies=frequencies).to_image().show()
    

if __name__ == '__main__':
    work_with_statistics = WorkWithStatistics()
    load_json = WorkWithJson().load_json('vacancies_full.json')
    statistics = work_with_statistics.get_frequencies(data_dict=load_json, 
                                                      key_tracking='key_skills',
                                                      key_adding='name')
    # print(statistics)

    print('Топ навыков Python-разработчика:')
    work_with_statistics.gen_img_statistics(color='white', frequencies=statistics)
