key = '5900058312:AAF6-fLpSwJLHrnIJqyt2lrz6ZPmEHtaRzc'




# import re
# st = ['Розовые фламинго (мини-сериал, 2020)', 'Рука бога (сериал, 2023)', 'Сядь за руль моей машины (сериал)', 'Конь', 'Сериал']
# new_st = []
# for i in st:
#     new_st.append(re.sub(r' \((мини-)*сериал(,)*( )*(\d\d\d\d)*\)','',i))
# print(new_st)

# Список просмотренных мной фильмов, спарсенный с Кинопоиска
# read = open('films.txt', 'r', encoding='UTF-8')
# readlist = read.read().strip('\'').split('\', \'')
# print(readlist)

# list1 = [1, 2, 3, 4, 5, 6, 7, 7, 9]
# list2 = []
# count = 0
# for i in list1:
#     if count == len(list1):
#          break
#     if count+1 == len(list1):
#         list2.append([list1[count]])
#         break
#     list2.append([list1[count],list1[count+1]])
#     count +=2
# print(list2)

# list1 = [1, 2, 3, 4, 5, 6, 7]
#
# dict3 = {'Костян': 'Herr', 'Натали': 'Frau', 'Чаки': 'Писюн'}
#
# for i, key, value in zip(list1, dict3.keys(), dict3.values()):
#      print(f'{i} === {key} === {value}')

#     #парсим просмотренные за последний год фильмы с моей странички Кинопоиска
#     driver.get('https://www.kinopoisk.ru/user/4759790/votes/list/year_from/2022/year_to/2023/vs/novote/#list')
#     elements = driver.find_elements(By.CLASS_NAME, 'nameRus')
#     kinopoisk_list = []
#     for i in elements:
#         if 'сериал' not in i.text:
#             kinopoisk_list.append(i.text[0:-7].replace('\xa0',' '))

'''search_film = f'«{random_film}», фильм'
        film_text = wikipedia.summary(wikipedia.search(search_film)[0], sentences=5)
        try:
            driver.get(wikipedia.page(wikipedia.search(search_film)[0]).url)
            driver.find_element(By.CLASS_NAME, 'infobox-image').click()
            driver.implicitly_wait(2)
            driver.find_element(By.CLASS_NAME, 'mw-mmv-stripe-button-container').find_element(By.TAG_NAME, 'a').click()
            driver.implicitly_wait(2)
            driver.find_element(By.CLASS_NAME, 'fullMedia').find_element(By.TAG_NAME, 'a').click()
            lin = driver.current_url
            await bot.send_photo(call.message.chat.id, lin, f'{random_film.upper()}\n\n{film_text}')
        except:
            await bot.send_message(call.message.chat.id,f'{random_film.upper()}\n\n{film_text}')'''

bar_dict = {'horse': 'Конь', 'tequila': 'Текила'}
# print([key for key,value in bar_dict.items() if value == 'tequila'][0])
