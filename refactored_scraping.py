from selenium import webdriver
# # Selectタグが扱えるエレメントに変化させる為の関数を呼び出す
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import csv

def acquire_classes():
    result = driver.page_source
    soup = BeautifulSoup(result, "html.parser")
    
    infoOfClasses = []
    blocks = soup.find_all("tr")
    for block in blocks:
        texts = block.get_text()
        info = texts.split('\n')[1:-1]

        if not len(info[0]) == 0:
            class_code, name, prof, class_place, time = info[1], info[2], info[3],info[6],  info[7]
            with open('class.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow([class_code, name, prof, class_place, time])
            
            infoOfClasses.append([class_code, name, prof, time, class_place])

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