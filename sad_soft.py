
# !/usr/bin/env python
from sqlite3 import Error, OperationalError

import PySimpleGUI as sg
import sqlite3
import os
from selenium.webdriver.common.keys import Keys

import time
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from threading import Thread
from selenium.common import exceptions as exc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import DesiredCapabilities

from selenium.webdriver.common.by import By

from queue import Queue as qe
flag=qe()
vls=qe()
def getDriver(user, headless: bool = False):
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')

    # options.add_argument(r'user-data-dir={}'.format(str(os.path.join(os.getcwd(), 'users'))))
    # options.add_argument('--profile-directory={}'.format(user))
    if headless == True:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option("prefs", prefs)

    options.add_argument('log-level=3')

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    try:
        '''driver = webdriver.Chrome('chromedriver.exe', desired_capabilities=caps, options=options,
                                  service=Service(ChromeDriverManager().install()))'''
        driver = webdriver.Chrome('chromedriver.exe', desired_capabilities=caps, options=options)
    except exc.SessionNotCreatedException as e:
        print(e)
        exit(0)
    return driver


import keyboard


#d={}
#driver=''


replica = ''
c = 0
w=''







def btn(_class, pos=None, chekbox=False):
    for i in range(1, 3):
        try:
            if chekbox != True:
                if pos != None:
                    obj = driver.find_elements(By.XPATH, '//*[contains(@class, "{}")]'.format(_class))
                    obj[pos].click()
                else:
                    obj = driver.find_element(By.XPATH, '//*[contains(@class, "{}")]'.format(_class))
                    obj.click()
                return
            else:
                if pos != None:
                    obj = driver.find_elements(By.XPATH, '//*[contains(@type, "{}")]'.format(_class))
                    obj[pos].click()
                else:
                    obj = driver.find_element(By.XPATH, '//*[contains(@type, "{}")]'.format(_class))
                    obj.click()
                return

        except Exception as e:
            print(e)
            time.sleep(1)
            continue


def btnEx(_class, pos=None):
    for i in range(1, 3):
        try:

            if pos != None:
                obj = driver.find_elements(By.XPATH, '//*[contains(@id, "{}")]'.format(_class))
                obj[pos].click()
            else:
                obj = driver.find_element(By.XPATH, '//*[contains(@id, "{}")]'.format(_class))
                obj.click()
            return

        except Exception as e:
            print(e)
            time.sleep(1)
            continue


def send_key(_class, text, pos=None, timeout=None):
    if _class == 'search-box':
        clear()

    for i in range(1, 3):
        try:
            if _class.find('List') != -1:
                if pos != None:
                    obj = driver.find_elements(By.XPATH, '//*[contains(@class, "{}")]'.format(_class))

                    obj[pos].send_keys(text)
                    if timeout == None:
                        pass
                    else:
                        time.sleep(timeout)
                        obj[pos].send_keys(Keys.RETURN)
                else:
                    obj = driver.find_element(By.XPATH, '//*[contains(@class, "{}")]'.format(_class))

                    obj.send_keys(text)
                    if timeout == None:
                        pass
                    else:
                        time.sleep(timeout)
                        obj.send_keys(Keys.RETURN)
                return
            else:

                if pos != None:
                    obj = driver.find_elements(By.XPATH, '//*[contains(@class, "{}")]'.format(_class))
                    obj[pos].clear()
                    obj[pos].send_keys(text)
                    if timeout == None:
                        pass
                    else:
                        time.sleep(timeout)
                        obj[pos].send_keys(Keys.RETURN)
                else:
                    obj = driver.find_element(By.XPATH, '//*[contains(@class, "{}")]'.format(_class))
                    obj.clear()
                    obj.send_keys(text)
                    if timeout == None:
                        pass
                    else:
                        time.sleep(timeout)
                        obj.send_keys(Keys.RETURN)
                return
        except Exception as e:
            time.sleep(1)
            continue


def input(_class, pos=None):
    pass


def save():
    lists = None
    for i in range(1, 3):
        try:

            lists = driver.find_elements(By.XPATH, '//*[contains(@class, "action-bar-button")]')
            break
        except:
            time.sleep(1)
            continue
    if lists != None:
        for list in lists:
            try:
                if list.text == 'Сохранить':
                    list.click()
                    break
            except:
                continue
        time.sleep(2)


def saveAndClose():
    lists = None
    for i in range(1, 3):
        try:

            lists = driver.find_elements(By.XPATH, '//*[contains(@class, "action-bar-button")]')
            break
        except:
            time.sleep(1)
            continue
    if lists != None:
        for list in lists:
            try:
                if list.text == 'Сохранить и Закрыть':
                    list.click()
                    break
            except:
                continue
        time.sleep(2)


def close():
    lists = None
    for i in range(1, 3):
        try:

            lists = driver.find_elements(By.XPATH, '//*[contains(@class, "action-bar-button")]')
            break
        except:
            time.sleep(1)
            continue
    if lists != None:
        for list in lists:
            try:
                if list.text == 'Закрыть':
                    list.click()
                    break
            except:
                continue
        time.sleep(2)


def bar(_class, title):
    print('bar')
    lists = None
    for i in range(1, 3):
        try:

            lists = driver.find_elements(By.XPATH, '//*[contains(@class, "{}")]'.format(_class))
            break
        except:
            time.sleep(1)
            continue
    if lists != None:

        for act in lists:
            try:

                if act.text.find('{}'.format(title)) != -1:
                    act.click()

                    time.sleep(1)
                    return act
            except Exception as e:
                print(e)
                continue


def expand():
    driver.execute_script(
        "for (let elem of document.getElementsByTagName('div')) {elem.style.display = 'block';}")


def clear():
    search = driver.find_elements(By.XPATH, '//*[contains(@class, "{}")]'.format('search-box'))
    try:
        for obj in search:
            obj.clear()
    except:
        pass




class func(Thread):
    def __init__(self,window,steps,d,key):
        Thread.__init__(self)
        self.window=window
        self.steps=steps
        self.d=d
        self.key=key
        self.driver=getDriver('def')
        global driver
        driver=self.driver
        self.driver.maximize_window()


        self.driver.get('http://10.0.25.113:8080/cm5div6/Login.html?targetPage=')



    lines = []
    '''apps_bk = [{'name': 'COK'},
               {'name': 'iDocs Storage'},
               {'name': 'Rendition'},
               {'name': 'WF-Ознакомление'},
               {'name': 'WF-Процессы'},
               {'name': 'Блокировки'},
               {'name': 'Буферное хранилище данных'},
               {'name': 'ВнД 2022', 'str': 'Принято к сведению'},
               {'name': 'ВхД 2022', 'str': 'Принято к сведению'},
               {'name': 'Договоры', 'str': 'Принято к сведению'},
               {'name': 'Документы'},
               {'name': 'ИсхД 2022'},
               {'name': 'Каталог'},
               {'name': 'Классификатор связей'},
               {'name': 'Контроль заданий'},
               {'name': 'Настраиваемые реквизиты'},
               {'name': 'Нумератор {}'.format(d['name'])},
               {'name': 'Обсуждения'},
               {'name': 'ОГ 2022', 'str': 'Принято к сведению'},
               {'name': 'Ознакомление'},
               {'name': 'ОРД 2022', 'str': 'Принято к сведению'},
               {'name': 'Переадресация ссылок'},
               {'name': 'Персональные настройки'},
               {'name': 'Портал'},
               {'name': 'Поручения', 'str': 'Принято к сведению'},
               {'name': 'Согласование'},
               {'name': 'Списки рассылки'},
               {'name': 'СПКД'},
               {'name': 'СпО'},
               {'name': 'Справочник персон'},
               {'name': 'Уведомления'},
               {'name': 'Учет ВхД корр.'},
               {'name': 'ФД {}'.format(d['name'])},
               {'name': 'Центр Отчетов AF5'},
               {'name': "InterTrust's AddressBook"},
               {'name': 'АРМ КИПР'},
               ]'''


    def getKey(self):
        while True:
            if keyboard.is_pressed(self.key):
                return True

            time.sleep(0.1)

    '''places_bk = [{'name': 'Внутренние документы', 'pos': 0},
                 {'name': 'Входящие документы', 'pos': 1},
                 {'name': 'Исходящие документы', 'pos': 3},
                 {'name': 'Обращения граждан', 'pos': 5},
                 {'name': 'Организационно-распорядительные документы', 'pos': 6}]'''


    def update(self):
        flag.put_nowait(True)
        time.sleep(.2)
        val=vls.get_nowait()

        self.d = {'full_name': val['full_name'], 'name': val['name'], 'sys_code': val['sys_code'],
             'code': val['code'],'repa':val['repa'],'adminka':val['adminka']}
        print(self.d)

    def step1(self):
        self.update()
        self.log('Организации')
        bar('non-selected', 'Организация')
        expand()
        bar('tree-label', 'Структура организации')
        bar('treeItemTitle', 'Организации')
        bar('action-bar-button', 'Создать')

        send_key('gwt-TextBox', self.d['full_name'], 0)
        send_key('gwt-TextBox', self.d['name'], 1)
        send_key('gwt-TextBox', self.d['code'], 2)
        send_key('gwt-TextBox', self.d['sys_code'], 3)
        send_key('gwt-SuggestBox', 'NSK', None, 2)
        bar('gwt-Label', 'Настройка СО')

        btn('checkbox', 2, True)
        btn('checkbox', 4, True)
        bar('gwt-Label', 'Уведомления')
        btn('checkbox', 9, True)
        lists = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-Label")]')

        '''for list in lists:

            if list.text=='Настройка СО':
                list.click()
                btn('checkbox',2)
                btn('checkbox', 4)
            if list.text == 'Уведомления':
                list.click()
                btn('checkbox',9)'''
        saveAndClose()
        time.sleep(4)


    def step2(self):
        self.update()
        self.log('Территории')
        bar('non-selected', 'Структура Системы')
        expand()
        bar('treeItemTitle', 'Территории')
        time.sleep(3)
        send_key('search-box', self.d['name'], None, 3)
        btn('GGTKKCKDCG-com-google-gwt-user-cellview-client-DataGrid-Style-dataGridEvenRow')
        time.sleep(1)
        bar('action-bar-button', 'Редактировать')

        time.sleep(3)
        send_key('gwt-TextBox', 'NSK', 0)
        send_key('gwt-TextBox', 'NSK', 1)
        send_key('gwt-TextBox', self.d['sys_code'], 2)
        btn('bookmarks-link-non-active')

        time.sleep(1)
        send_key('gwt-TextBox', '07:00', 4)
        time.sleep(1)

        send_key('gwt-ListBox', 'к востоку от Гринвича')

        save()
        close()
        bar('treeItemTitle', 'Экземпляры системы')
        bar('action-bar-button', 'Редактировать')

        time.sleep(3)
        btn('common-widget-button-style', 0)

        time.sleep(2)
        send_key('search-box', self.d['name'], None, 1)

        time.sleep(3)
        btn('checkbox', 1, True)
        btn('darkButton buttons-fixed', 0)
        save()
        close()
        time.sleep(3)


    def step3(self):
        self.update()

        self.log('Приложения')
        bar('non-selected', 'Структура Системы')
        expand()
        bar('treeItemTitle', 'Приложения')
        bar('action-bar-button', 'Создать')

        send_key('gwt-SuggestBox', 'Формирование Дел', 0, 2)
        send_key('gwt-SuggestBox', 'AF5', 4, 2)
        # btn('checkbox', 1, True)
        send_key('gwt-TextBox', 'ФД {}'.format(self.d['name']), 0)

        save()
        time.sleep(5)
        fields = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-TextBox")]')
        replica = fields[2].get_attribute('value')
        send_key('gwt-TextBox', '{}.nsf'.format(replica), 3)

        saveAndClose()
        time.sleep(4)
        bar('action-bar-button', 'Создать')

        send_key('gwt-SuggestBox', 'Нумератор', 0, 2)
        send_key('gwt-SuggestBox', 'AF5', 4, 2)
        # btn('checkbox', 1, True)
        send_key('gwt-TextBox', 'Нумератор {}'.format(self.d['name']), 0)

        save()
        time.sleep(4)
        fields = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-TextBox")]')
        replica = fields[2].get_attribute('value')
        send_key('gwt-TextBox', '{}.nsf'.format(replica), 3)
        saveAndClose()
        time.sleep(4)
        send_key('search-box', 'СО ' + self.d['name'], None, 3)
        btn('GGTKKCKDCG-com-google-gwt-user-cellview-client-DataGrid-Style-dataGridEvenRow')
        time.sleep(1)
        bar('action-bar-button', 'Редактировать')
        fields = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-TextBox")]')
        replica = fields[2].get_attribute('value')
        self.window['repa'].update(replica)

        time.sleep(2)
        send_key('gwt-TextBox', '{}.nsf'.format(replica), 3)
        saveAndClose()
        time.sleep(4)


    def step4(self):
        self.update()
        self.log('Приложения организаций')
        apps = [{'name': 'COK'},
                {'name': 'iDocs Storage'},
                {'name': 'Rendition'},
                {'name': 'WF-Ознакомление'},
                {'name': 'WF-Процессы'},
                {'name': 'Блокировки'},
                {'name': 'Буферное хранилище данных'},
                {'name': 'ВнД 2022', 'str': 'Принято к сведению'},
                {'name': 'ВхД 2022', 'str': 'Принято к сведению'},
                {'name': 'Договоры', 'str': 'Принято к сведению'},
                {'name': 'Документы'},
                {'name': 'ИсхД 2022'},
                {'name': 'Каталог'},
                {'name': 'Классификатор связей'},
                {'name': 'Контроль заданий'},
                {'name': 'Настраиваемые реквизиты'},
                {'name': 'Нумератор {}'.format(self.d['name'])},
                {'name': 'Обсуждения'},  # ne sozdaet
                {'name': 'ОГ 2022', 'str': 'Принято к сведению'},
                {'name': 'Ознакомление'},
                {'name': 'ОРД 2022', 'str': 'Принято к сведению'},
                {'name': 'Переадресация ссылок'},
                {'name': 'Персональные настройки'},
                {'name': 'Портал'},
                {'name': 'Поручения', 'str': 'Принято к сведению'},
                {'name': 'Согласование'},
                {'name': 'Списки рассылки'},
                {'name': 'СПКД'},
                {'name': 'СпО'},
                {'name': 'Справочник персон'},
                {'name': 'Уведомления'},
                {'name': 'Учет ВхД корр.'},
                {'name': 'ФД {}'.format(self.d['name'])},
                {'name': 'Центр Отчетов AF5'},
                {'name': "InterTrust's AddressBook"},
                {'name': 'АРМ КИПР'},
                ]
        bar('non-selected', 'Структура Системы')
        expand()
        bar('treeItemTitle', 'Приложения организаций')
        time.sleep(2)
        for app in apps:
            bar('action-bar-button', 'Создать')

            time.sleep(2)
            send_key('gwt-SuggestBox', self.d['name'], 0, 2)
            send_key('gwt-SuggestBox', app['name'], 1, 2)

            if 'str' in app:
                save()
                bar('gwt-Label', 'Дополнительно')
                labels = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-Label")]')
                for label in labels:
                    if label.text == 'Дополнительно':
                        label.click()
                        time.sleep(1.5)
                btn('facebook-label facebook-clickable-label')

                time.sleep(2)
                btnEx('IsEnExecutionService')

                time.sleep(2)
                try:
                    rkkn = driver.find_elements(By.XPATH, '//*[contains(@id, "RkkNoteReportName")]')
                    if len(rkkn) == 0:
                        rkkn = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-TextBox")]')[1]
                    else:
                        rkkn = driver.find_elements(By.XPATH, '//*[contains(@id, "RkkNoteReportName")]')[1]
                    ActionChains(driver).send_keys_to_element(rkkn, app['str']).perform()
                except:
                    pass
                try:
                    rkkt = driver.find_elements(By.XPATH, '//*[contains(@id, "RkkNoteReportText")]')[1]
                    ActionChains(driver).send_keys_to_element(rkkt, app['str']).perform()
                except:
                    pass
                resn = driver.find_elements(By.XPATH, '//*[contains(@id, "ResNoteReportName")]')[1]
                rest = driver.find_elements(By.XPATH, '//*[contains(@id, "ResNoteReportText")]')[1]

                ActionChains(driver).send_keys_to_element(resn, app['str']).perform()
                ActionChains(driver).send_keys_to_element(rest, app['str']).perform()

                save()
                close()
                time.sleep(1)
                close()
            else:
                saveAndClose()
        time.sleep(1.5)


    def step5(self):
        self.update()
        self.log('Настройки печати штампов')
        stamps = ['Входящие документы',
                  'Исходящие документы',
                  'Внутренние документы']
        bar('non-selected', 'Структура Системы')
        expand()
        bar('tree-label', 'Прочее')
        bar('treeItemTitle', 'Настройки печати штампов')
        for stamp in stamps:
            bar('action-bar-button', 'Создать')

            time.sleep(1)
            btn('checkbox', 0, True)
            send_key('gwt-TextBox', self.d['name'], 0)
            send_key('gwt-SuggestBox', self.d['name'], 0, 2)
            send_key('gwt-SuggestBox', stamp, 1, 2)

            lists = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-Label")]')
            for list in lists:

                if list.text == 'Универсальные настройки':
                    list.click()
                    time.sleep(1)
                    send_key('gwt-ListBox', 'Регистрационный номер и ЭП')
                    send_key('gwt-TextBox', 'Times New Roman', 1)
                    send_key('gwt-TextBox', '12', 2)

                if list.text == 'Настройки Word':
                    list.click()
                    time.sleep(1)

                    send_key('gwt-ListBox', 'На первую', 1, .5)
                    send_key('gwt-ListBox', 'Влево', 2, .5)
                    send_key('gwt-ListBox', 'Вниз', 3, .5)
                    send_key('gwt-TextBox', '60', 4)
                    send_key('gwt-TextBox', '0', 5)
                    send_key('gwt-TextBox', '80', 6)
                    send_key('gwt-TextBox', '7', 7)
                    send_key('gwt-TextBox', 'Times New Roman', 8)
                    send_key('gwt-TextBox', '12', 8)

                    area = driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-TextArea")]')
                    if stamp == 'Входящие документы':
                        send_key('gwt-TextArea',
                                 '''var result; var RDate = ctx.get('OutDate'); RDate = RDate.size() > 0 ? RDate.get(0).toString() : ''; var rprist = ctx.get('rprist'); rprist = rprist.size() > 0 ? rprist.get(0) : ''; var RNumber = ctx.get('OutNumber'); RNumber = RNumber.size() > 0 ? RNumber.get(0) : ''; var rfin = ctx.get('rfin'); rfin = rfin.size() > 0 ? rfin.get(0) : ''; var listRes = session.createArray('№ ' + RNumber +' от '+RDate); result = listRes; ctx.setResult(result);''',
                                 1)

                    if stamp == 'Исходящие документы':
                        send_key('gwt-TextArea',
                                 '''var result; var RDate = ctx.get('RDate'); RDate = RDate.size() > 0 ? RDate.get(0).toString() : ''; var rprist = ctx.get('rprist'); rprist = rprist.size() > 0 ? rprist.get(0) : ''; var RNumber = ctx.get('RNumber'); RNumber = RNumber.size() > 0 ? RNumber.get(0) : ''; var rfin = ctx.get('rfin'); rfin = rfin.size() > 0 ? rfin.get(0) : ''; var listRes = session.createArray('№ ' + rprist + RNumber + rfin+' от '+RDate); result = listRes; ctx.setResult(result);''',
                                 1)

                    if stamp == 'Внутренние документы':
                        send_key('gwt-TextArea',
                                 '''var result; var rdvec = ctx.get('RegistrationD'); var rd = rdvec.size() > 0 ? rdvec.get(0) : ''; var RDate = rd.getClass().getName().endsWith("DateTimeAdapter") ? rd.getDateOnly() : ''; var rprist = ctx.get('rprist'); rprist = rprist.size() > 0 ? rprist.get(0) : ''; var RNumber = ctx.get('RNumber'); RNumber = RNumber.size() > 0 ? RNumber.get(0) : ''; var rfin = ctx.get('rfin'); rfin = rfin.size() > 0 ? rfin.get(0) : ''; var listRes = session.createArray('№ ' + rprist + RNumber + rfin+' от ' + RDate); result = listRes; ctx.setResult(result);''',
                                 1)

                if list.text == 'Настройки печати Штампа ЭП':
                    list.click()
                    time.sleep(1)
                    btn('checkbox', 1, True)

                    send_key('gwt-ListBox', 'последняя', 4, .5)
                    send_key('gwt-ListBox', 'Вправо', 5, .5)
                    send_key('gwt-ListBox', 'Вверх', 6, .5)
                    send_key('gwt-TextBox', '70', 10)
                    send_key('gwt-TextBox', '50', 11)
                    send_key('gwt-TextBox', '90', 12)
                    send_key('gwt-TextBox', '38', 13)

                    saveAndClose()
        time.sleep(1)


    def step6(self):
        self.update()
        self.log('Нумератор')
        nums = [{'name': 'вхд 2022', 'formula': 'ctx.setResult(session.counterFormulas().programPlusIds(ctx));',
                 'num': "ctx.setResult('/{}-Вх')".format(self.d['code'])},
                {'name': 'внд 2022', 'formula': 'ctx.setResult(session.counterFormulas().programPlusIds(ctx));',
                 'num': "ctx.setResult('/{}-Вн')".format(self.d['code'])},
                {'name': 'исхд 2022', 'formula': 'ctx.setResult(session.counterFormulas().programPlusIds(ctx));',
                 'num': "ctx.setResult('/{}-Исх')".format(self.d['code'])},
                {'name': 'ОГ 2022',
                 'formula': "session.func().concat(session.counterFormulas().programPlusIds(ctx),'[Письменное обращение]')",
                 'num': "ctx.setResult('/{}-ПГ')".format(self.d['code'])},
                {'name': 'ОГ 2022',
                 'formula': "session.func().concat(session.counterFormulas().programPlusIds(ctx),'[Устное обращение]')",
                 'num': "ctx.setResult('/{}-УП')".format(self.d['code'])},
                {'name': 'ОГ 2022',
                 'formula': "session.func().concat(session.counterFormulas().programPlusIds(ctx),'[Личный прием]')",
                 'num': "ctx.setResult('/{}-ЛП')".format(self.d['code'])},
                {'name': 'ОГ 2022',
                 'formula': "session.func().concat(session.counterFormulas().programPlusIds(ctx),'[Прием специалиста]')",
                 'num': "ctx.setResult('/{}-Пр')".format(self.d['code'])},
                {'name': 'ОРД 2022', 'formula': "ctx.setResult(session.counterFormulas().programPlusIds(ctx));",
                 'num': "ctx.setResult('/{}')".format(self.d['code'])}]
        bar('non-selected', 'Структура Системы')
        expand()
        bar('tree-label', 'Прочее')
        bar('treeItemTitle', 'Нумератор')
        for num in nums:
            bar('action-bar-button', 'Создать')

            time.sleep(1)
            send_key('gwt-SuggestBox', 'Нумератор {}'.format(self.d['name']), 0, 2)
            send_key('gwt-SuggestBox', num['name'], 1, 2)
            btn('lightButton ldotCreate', 0)

            time.sleep(1)

            send_key('gwt-TextBox', '1', 3)
            send_key('gwt-SuggestBox', self.d['name'], 2, 1)

            btn('lnfm-save-button darkButton', 0)

            time.sleep(2)

            send_key('gwt-TextBox', '0', 1)
            send_key('gwt-TextArea', num['formula'], 0)
            btn('lightButton ldotCreate', 1)

            time.sleep(2)

            send_key('gwt-TextArea', num['num'], 1)
            send_key('gwt-ListBox', 'По формуле', 0)
            send_key('gwt-TextBox', '1', 3)
            btn('lnfm-save-button darkButton', 0)

            saveAndClose()
        time.sleep(1)


    def step7(self):
        self.update()
        self.log('Места регистрации')
        places = [{'name': 'Внутренние документы', 'pos': 0},
                  {'name': 'Входящие документы', 'pos': 1},
                  {'name': 'Исходящие документы', 'pos': 3},
                  {'name': 'Обращения граждан', 'pos': 5},
                  {'name': 'Организационно-распорядительные документы', 'pos': 6}]
        bar('non-selected', 'Организация')
        expand()

        bar('tree-label', 'Настройки делопроизводств...')
        bar('treeItemTitle', 'Места регистрации')
        for place in places:
            btn('expand-arrow', place['pos'])
            time.sleep(.5)
            bar('action-bar-button', 'Создать')
            send_key('gwt-SuggestBox', place['name'], 0, 2)
            send_key('gwt-SuggestBox', self.d['name'], 1, 2)
            bar("gwt-Label", 'Делопроизводители')

            time.sleep(1)
            btn('checkbox', 0, True)
            saveAndClose()
            time.sleep(.2)
            bar('gwt-Hyperlink', 'Места регистрации')


    def integrator(self):
        self.update()
        self.log('integrator')
        bar('non-selected', 'Настройки ИР')
        expand()
        bar('tree-label', 'Участники')
        bar('treeItemTitle', 'Иерархия')
        time.sleep(.5)
        bar('action-bar-button', 'Создать')
        time.sleep(.5)
        bar('action-bar-button', 'Корреспондент')
        send_key('gwt-TextBox', self.d['name'], 0)

        send_key('gwt-TextBox', self.d['repa'], 1)
        save()
        time.sleep(.5)
        close()
        bar('non-selected', 'Настройки ИР')
        expand()
        bar('tree-label', 'Участники')
        bar('treeItemTitle', 'Участники интеграции')
        ind = int(
            driver.find_elements(By.XPATH, '//*[contains(@class, "GNMSARGBG-com-google-gwt-user-cellview")]')[
                2].text) + 1
        bar('action-bar-button', 'Создать')
        time.sleep(.5)
        bar('action-bar-button', 'Участник интеграции')
        send_key('gwt-TextBox', 'СО ' + self.d['name'], 0)
        send_key('gwt-TextBox', ind, 1)
        send_key('gwt-SuggestBox', 'Система 10.0.25.113', 0, 1)
        send_key('gwt-SuggestBox', self.d['name'], 1, 2)
        save()
        time.sleep(.5)
        close()
        bar('non-selected', 'Настройки ИР')
        expand()
        bar('tree-label', 'Корреспонденты')
        bar('treeItemTitle', 'Учетные записи')
        bar('action-bar-button', 'Создать')
        time.sleep(.5)
        bar('action-bar-button', 'Учетная запись')
        send_key('gwt-SuggestBox', 'СО ' + self.d['name'], 0, 2)
        expand()
        btn('suggest-container-arrow-btn', 1)
        time.sleep(1)
        bar('item', 'Система 10.0.25.113 - CMJ-REST/HTTP')
        send_key('gwt-TextBox', self.d['adminka'], 0)
        send_key('gwt-TextBox', '12345', 1)
        save()
        time.sleep(.5)
        close()


    def agent(self):
        self.update()
        self.log('agent')
        agents1 = ['CMJ-Approving-Interrupt',
                   'CMJ-Approving-UpdateByAnswer',
                   'CMJ-Approving-UpdateByVisa',
                   'CMJ-Review-Interrupt',
                   'CMJ-Review-UpdateByAnswer',
                   'CMJ-Review-UpdateByChlogVisa',
                   'CMJ-Meetings-PointsProcedures']
        agents2 = [{"name": 'Группа агентов Ночные - По расписанию – Ознакомление', 'agents': ["CMJ-Review-Archivate",
                                                                                               "CMJ-Review-InterruptByTime",
                                                                                               "CMJ-Review-Remind"]},
                   {"name": 'Группа агентов Ночные - По расписанию - Согласование',
                    'agents': ["CMJ-Approving-Archivate",
                               "CMJ-Approving-InterruptByTime",
                               "CMJ-Approving-RemindFreez",
                               "CMJ-Approving-RemindParallel",
                               "CMJ-Approving-RemindSerialAndComb"]}]

        bar('non-selected', 'Настройки')

        bar('treeItemTitle', 'Настройки запуска')
        time.sleep(1)
        for agent in agents1:
            bar('action-bar-button', 'Создать')
            time.sleep(.5)
            bar('action-bar-button', 'Настройка запуска ASAP - на всех серверах')
            time.sleep(.5)
            btn('checkbox', 0, True)
            send_key('gwt-TextBox', '{} {}'.format(agent, self.d['name']), 0)

            sel = Select(driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-ListBox")]')[0]).select_by_index(1)
            sel = Select(driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-ListBox")]')[1]).select_by_index(1)

            send_key('gwt-TextBox', '-1', 2)
            btn('lightButton ldotCreate')
            time.sleep(.5)

            btn('suggest-container-arrow-btn', 0)
            time.sleep(1)
            bar('item', agent)
            sel = Select(driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-ListBox")]')[3]).select_by_index(1)
            btn('lnfm-save-button darkButton')
            time.sleep(.5)
            save()
            time.sleep(1)
            btn('GNMSARGNI-ru-intertrust-cm-core-gui-impl-client-themes-CommonCssResource-editButton editActionStyle',
                0)
            time.sleep(.5)
            btn('GNMSARGNI-ru-intertrust-cm-core-gui-impl-client-themes-CommonCssResource-editButton editActionStyle',
                1)
            time.sleep(.5)
            send_key('gwt-TextBox', self.d['repa'], 6)
            btn('lnfm-save-button darkButton', 1)
            time.sleep(1)
            btn('lnfm-save-button darkButton', 0)
            time.sleep(1)
            save()
            time.sleep(.5)
            close()
            time.sleep(1)
        for agent in agents2:
            bar('action-bar-button', 'Создать')
            time.sleep(.5)
            bar('action-bar-button', 'Настройка запуска по расписанию - на всех серверах')
            time.sleep(.5)
            btn('checkbox', 0, True)
            send_key('gwt-TextBox', '{} {}'.format(agent['name'], self.d['name']), 0)

            sel = Select(driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-ListBox")]')[0]).select_by_index(1)
            sel = Select(driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-ListBox")]')[1]).select_by_index(1)

            send_key('gwt-TextBox', '-1', 2)
            btn('lightButton ldotCreate', 1)
            time.sleep(.5)

            ActionChains(driver).move_to_element(
                driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-TextBox")]')[10]).perform()
            if agents2.index(agent) == 1:
                send_key('gwt-TextBox', '2', 10)
            else:
                send_key('gwt-TextBox', '3', 10)
            ActionChains(driver).move_to_element(
                driver.find_elements(By.XPATH, '//*[contains(@class, "gwt-TextBox")]')[11]).perform()

            send_key('gwt-TextBox', '0', 11)
            ActionChains(driver).move_to_element(
                driver.find_element(By.XPATH, '//*[contains(@class, "lnfm-save-button darkButton")]')).perform()
            btn('lnfm-save-button darkButton')
            time.sleep(1)

            for i in agent['agents']:
                ind = agent['agents'].index(i)
                btn('lightButton ldotCreate')
                time.sleep(.5)
                bar('gwt-Label', 'Конфигурация самостоятельного агента')
                time.sleep(.5)

                btn('suggest-container-arrow-btn', 0)
                time.sleep(1)
                bar('item', i)

                btn('lnfm-save-button darkButton')
                time.sleep(1)
            save()
            time.sleep(.5)

            obj = driver.find_elements(By.XPATH,
                                       '//*[contains(@class, "GNMSARGNI-ru-intertrust-cm-core-gui-impl-client-themes-CommonCssResource-editButton editActionStyle")]')
            print(len(obj))
            for i in obj[0:-1]:
                i.click()
                time.sleep(.5)
                for edit in driver.find_elements(By.XPATH,
                                                 '//*[contains(@class, "GNMSARGNI-ru-intertrust-cm-core-gui-impl-client-themes-CommonCssResource-editButton editActionStyle")]'):
                    if edit.is_enabled():
                        edit.click()

                time.sleep(.5)
                send_key('gwt-TextBox', self.d['repa'], 7)
                btn('lnfm-save-button darkButton', 1)
                time.sleep(1)
                btn('lnfm-save-button darkButton', 0)
                time.sleep(1)
            save()
            time.sleep(.5)
            close()
            time.sleep(1)
    def run(self):
        try:
            for i, step in enumerate(self.steps):
                print(step)
                if step==True and i==0:
                    if self.getKey():
                        print('222')
                        self.step1()
                        self.step2()
                        self.step3()
                        self.step4()
                        self.step5()
                        self.step6()
                        self.step7()


                    break
                else:
                    if step and i==1:

                        if self.getKey():

                            self.step1()
                    if step and i==2:
                        if self.getKey():
                            self.step2()
                    if step and i==3:
                        if self.getKey():
                            self.step3()
                    if step and i==4:
                        if self.getKey():
                            self.step4()
                    if step and i==5:
                        if self.getKey():
                            self.step5()
                    if step and i==6:
                        if self.getKey():
                            self.step6()
                    if step and i==7:
                        if self.getKey():
                            self.step7()
                    if step and i==8:
                        driver.get(
                            'http://10.0.25.95:8080/cm-integrator/BusinessUniverse.html#link=lnk_cmi_credentials;ids=5091000000002056;')  # integrator
                        if self.getKey():

                            self.integrator()
                    if step and i==9:
                        driver.get(
                            'http://10.0.25.124:8080/agent-manager-war/BusinessUniverse.html#link=settings-run;ids=5078000000014349;')
                        if self.getKey():

                            self.agent()
        except Exception as e:
            self.log(e)
    def log(self,text):
        self.window['mline'].write(str(text)+'\n')



def connDB():
    try:
        conn = sqlite3.connect('db.db', isolation_level=None)
        cursor = conn.cursor()

        return conn, cursor
    except Error as e:
        print('Error db')
def executeSql(sql,commit:bool=False):
    try:
        conn, cursor = connDB()
        cursor.execute(sql)
        if commit == True:
            conn.commit()
        # conn.close()

        return cursor.fetchall()
    except OperationalError as s:
        print('operation error')
        print(s)
def make_window(theme):
    sg.theme(theme)
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']]]
    right_click_menu_def = [[], ['Обновить']]




    input_layout = [
        [sg.Text('Название Организации'),sg.Input(key='full_name')],
        [sg.Text('Название(короткое) Организации'), sg.Input(key='name')],
        [sg.Text('Код Организации'), sg.Input(key='code')],
        [sg.Text('Системный Код Организации'), sg.Input(key='sys_code')],
        [sg.Text('Админка'), sg.Input(key='adminka')],
        [sg.Text('Реплика'), sg.Input(key='repa')],
        [sg.Combo(['shift','insert','pause break'],key='k'), sg.Text('Клавиша для запуска')],
        [sg.Text('Выбор шагов')],
        [sg.Checkbox('Все',key='chbtn_1'),sg.Checkbox('Организации',key='chbtn_2'),sg.Checkbox('Территории',key='chbtn_3'),sg.Checkbox('Приложения',key='chbtn_4')],
        [sg.Checkbox('Приложения организаций',key='chbtn_5'), sg.Checkbox('Настройки печати штампов',key='chbtn_6'), sg.Checkbox('Нумератор',key='chbtn_7'), sg.Checkbox('Места регистрации',key='chbtn_8')],
        [sg.Checkbox('Интегратор',key='chbtn_9'), sg.Checkbox('Агенты',key='chbtn_10')],
        [sg.Multiline(
            '======log======\n',
            size=(20, 5), expand_x=True, expand_y=True, k='mline')],
        [sg.Button('Запустить',key='enter')]]




    window = sg.Window('СЭД', input_layout, right_click_menu=right_click_menu_def,
                       right_click_menu_tearoff=True, grab_anywhere=True, resizable=False, margins=(0, 0),
                       use_custom_titlebar=True, finalize=True, keep_on_top=True,
                       # scaling=2.0,
                       )
    window.set_min_size(window.size)
    return window

def grab(values):

    return values
def main():

    window = make_window(sg.theme())


    while True:
        event, values = window.read(timeout=100)

        if not flag.empty():
            if flag.get_nowait():
                vls.put_nowait(values)



        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break



        elif event == 'enter':
            a = window.ReturnValues[1]['repa']
            b=''
            global driver


            step=[values['chbtn_'+str(k)] for k in range(1,10,1)]
            if values['full_name']=='':
                sg.Popup(f'Нет имени организации',
                         auto_close=True, auto_close_duration=2, keep_on_top=True)
            elif values['name'] == '':
                sg.Popup(f'Нет короткого имени организации',
                         auto_close=True, auto_close_duration=2, keep_on_top=True)

            elif values['sys_code'] == '':
                sg.Popup(f'Нет системного кода',
                         auto_close=True, auto_close_duration=2, keep_on_top=True)
                pass
            elif values['code'] == '':
                sg.Popup(f'Нет кода организации',
                         auto_close=True, auto_close_duration=2, keep_on_top=True)
            elif values['k']=='':
                sg.Popup(f'Не выбрана клавиша запуска',
                         auto_close=True, auto_close_duration=2, keep_on_top=True)
            elif not True in step:

                sg.Popup(f'Выберите шаги',
                         auto_close=True, auto_close_duration=2, keep_on_top=True)
            else:
                d={'full_name':values['full_name'],'name':values['name'],'sys_code':values['sys_code'],'code':values['code']}





                sg.Popup(f'Сейчас запустится браузер, после авторизации нажмите клавишу "{values["k"]}" ',auto_close=True,auto_close_duration=2,keep_on_top=True)
                window.keep_on_top_clear()
                b=func(window,step,d,values["k"])
                b.start()








    window.close()



if __name__ == '__main__':


    sg.theme('DarkAmber')
    main()
