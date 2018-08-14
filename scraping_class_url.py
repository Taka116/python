from selenium import webdriver
# # Selectタグが扱えるエレメントに変化させる為の関数を呼び出す
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import csv
import re
import json

def acquire_classes():
    result = driver.page_source
    soup = BeautifulSoup(result, "html.parser")
    
    infoOfClasses = []
    blocks = soup.find_all("tr")

    for block in blocks:
        # filtering to prevent blocks that do not contain necessary elements from going on
        texts = block.get_text()
        info = texts.split('\n')[1:-1]
        
        condition1 = len(info[0])==0 # head要素かを判定。falseだったらok。
        condition2 = block.find("a", {"href": "#"})==None #url が含まれているかを判定。falseだったらok。
        if condition1==False and condition2 == False:
            
            # Scraping URL for Each Class
            onclick_element = block.find("a", {"href": "#"}).get("onclick")
            str_list = re.split("[(')']", onclick_element.strip('post_submit'))
            class_url = "https://www.wsl.waseda.jp/syllabus/" +  (".php?pKey=").join([ str.strip('DtlSubCon') for str in str_list if not str.strip() in ["", ","]]) + "&pLng=jp"

            class_detail_driver = webdriver.PhantomJS()
            class_detail_driver.get(class_url)
            class_detail_result = class_detail_driver.page_source
            class_detail_soup = BeautifulSoup(class_detail_result, "html.parser")
            class_detail_texts = [text for text in class_detail_soup.get_text().split('\n') if not text == '']

            level = class_detail_texts[ class_detail_texts.index('科目区分') + 1]
            number_of_credit = class_detail_texts[ class_detail_texts.index('単位数') + 1]
            # class_code = class_detail_texts[ class_detail_texts.index('コース・コード') + 1]
            if '授業概要' in class_detail_texts:
                content_of_class = class_detail_texts[ class_detail_texts.index('授業概要') + 1]
            else:
                content_of_class = None
            # grading_system = {}
            if '評価基準' in class_detail_texts:
                evaluation_system = class_detail_texts[ class_detail_texts.index('評価基準')+1 : class_detail_texts.index('ページの先頭へ戻る') ]
            else:
                evaluation_system = None
            # when all are scraped

            class_detail_driver.quit()

             # -----Scraping Time & Peiord ------
            time = info[6]
            days_and_periods = []

            search = re.search('[月火水木金土]', time)
            if search is None:
                days_and_periods.append(['曜日', '時限'])
            else:
                splitted_time = time.split("時限")
                del splitted_time[-1]
                if len(splitted_time) > 1:
                    formatted_time = [e[3:]for e in splitted_time]
                    for f in formatted_time:
                        days_and_periods.append( [f[0], int(f[1]) ])
                else:
                    days_and_periods.append( [splitted_time[0][0], int(splitted_time[0][1]) ])

            for day_and_period in days_and_periods:
                class_code, name, prof, class_place, day, period = info[1], info[2], info[3],info[7], day_and_period[0], day_and_period[1]
                with open('class.csv', 'a') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    writer.writerow([class_code, name, prof, class_place, day, period, level, number_of_credit, content_of_class, evaluation_system, class_url])

driver = webdriver.PhantomJS()

driver.get("https://www.wsl.waseda.jp/syllabus/JAA101.php")

semester_element = driver.find_element_by_name('p_gakki')
semester = Select(semester_element)
semester.select_by_value('2')

faculty = Select(driver.find_element_by_name('p_gakubu'))
faculty.select_by_value('212004')

firstPage = driver.find_element_by_xpath('//*[@id="cEdit"]/div/div[2]/table/tbody/tr/td[1]/div/div/p/input').click()

searchHundred = driver.find_element_by_xpath('//*[@id="cHeader"]/div[3]/a[3]').click()

acquire_classes()

searchNext = driver.find_element_by_xpath('//*[@id="cHonbun"]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[2]/div/div/p/a').click()

acquire_classes()

searchThirdPage = driver.find_element_by_xpath('//*[@id="cHonbun"]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[3]/div/div/p/a').click()

acquire_classes()

searchFourthPage = driver.find_element_by_xpath('//*[@id="cHonbun"]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[4]/div/div/p/a').click()

acquire_classes()

searchLast = driver.find_element_by_xpath('//*[@id="cHonbun"]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[5]/div/div/p/a').click()

acquire_classes()



# if '試験:' in evaluation_system:
#     exam_index = evaluation_system.index('試験:')
#     end_index = 0
#     for ele in evaluation_system[exam_index+1:]:
#         if re.match('[a-zA-Z0-9_]', ele) == None:
#             end_index = evaluation_system.index(ele)
#     exam = evaluation_system[exam_index:end_index]
# else:
#     exam = None
# if 'レポート:' in evaluation_system:
#     report_index = evaluation_system.index('レポート:')
#     for ele in evaluation_system[report_index+1:]:
#         if re.match('[a-zA-Z0-9_]', ele) == None:
#             end_index = evaluation_system.index(ele)
#     report = evaluation_system[report_index:end_index]
# else:
#     report = None
# if '平常点評価' in evaluation_system:
#     normal_index = evaluation_system.index('平常点評価')
#     for ele in evaluation_system[normal_index+1:]:
#         if re.match('[a-zA-Z0-9_]', ele) == None:
#             end_index = evaluation_system.index(ele)
#     normal = evaluation_system[normal_index:end_index]