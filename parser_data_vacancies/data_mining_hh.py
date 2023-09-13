import pandas as pd  # для работы с таблицами
from bs4 import BeautifulSoup  # для разбора html данных
from natasha import Doc, MorphVocab, NewsEmbedding, NewsMorphTagger, Segmenter
from work_with_json import WorkWithJson
from get_statistics import WorkWithStatistics


if __name__ == '__main__':
    work_with_json = WorkWithJson()
    vacancies = work_with_json.load_json('vacancies_full.json')
    
    work_with_statistics = WorkWithStatistics()
    frequencies = work_with_statistics.get_frequencies(data_dict=vacancies, 
                                                       key_tracking='key_skills', 
                                                       key_adding='name')
    vacancies_df_table = pd.DataFrame(vacancies)
    # print(vacancies_df_table['description'])  # список значений из колонки
    # print(vacancies_df_table['description'][0])  # одно значение из колонки

    soup = BeautifulSoup(vacancies_df_table['description'][0])
    # print(soup)
    text = soup.text  # получаем весь текст из html документа
    # print(text)

    # сегментация - разбиение на слова и предложения
    segmenter = Segmenter()

    # морфологический разбор - генерируются формы слова
    embedding = NewsEmbedding()
    morph_tagger = NewsMorphTagger()
    morph_vocab = MorphVocab()





