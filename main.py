from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import telebot

browser = webdriver.Chrome()

browser.get('https://www.banki.ru/products/currency/cb/')

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

# xpath = '/html/body/div[1]/div[1]/aside/div/section[1]/div[2]/div[1]/div/input[1]'
# element = browser.find_element(By.XPATH, xpath)
@bot.message_handler(commands=["py_questions"])
def test_value(message):

    numbers = [i for i in range(2, 36)]

    values = [
        'AUD',
        'AZN',
        'AMD',
        'THB',
        'BYN',
        'BGN',
        'BRL',
        'HUF',
        'KRW',
        'HKD',
        'DKK',
        'AED',
        'INR',
        'KZT',
        'CAD',
        'KGS',
        'CNY',
        'MDL',
        'RON',
        'TMT',
        'NOK',
        'PLN',
        'RUB',
        'SGD',
        'TJS',
        'TRY',
        'UZS',
        'UAH',
        'GBP',
        'CZK',
        'SEK',
        'CHF',
        'ZAR',
        'JPY'
            ]

    currency_dict = dict(zip(values, numbers))

    field_to_fill = '/html/body/div[1]/div[1]/aside/div/section[1]/div[2]/div[1]/div/input[1]'
    select_currency_list = '/html/body/div[1]/div[1]/aside/div/section[1]/div[2]/div[1]/div/div[1]'
    select_currency = '/html/body/div[1]/div[1]/aside/div/section[1]/div[2]/div[1]/div/div[2]/div/div/div[4]/div[1]/div/div[31]'
    input_field = '/html/body/div[1]/div[1]/aside/div/section[1]/div[2]/div[3]/div/input[1]'
    choose_currency = browser.find_element(By.XPATH, field_to_fill)
    choose_currency.clear()
    choose_currency.send_keys('12')
    browser.find_element(By.XPATH, select_currency_list).click()
    browser.find_element(By.XPATH, select_currency).click()
    time.sleep(1)
    # browser.save_screenshot('screenshot.png')
    bot.send_message(message.chat.id, (browser.find_element(By.XPATH, input_field).get_attribute('value')))
    browser.quit()



bot.polling(none_stop=True)