from selenium import webdriver
import time

# use chrome browser, will open a chrome browser when running
# inside () specifies the chromedrive.exe path, if it is in the same directory with this file, can leave it blank
web = webdriver.Chrome('D:/chromedriver.exe')

# go to the link
web.get('https://docs.google.com/forms/d/e/1FAIpQLScPnhXBC-LwIL-4RvBlA17jkA19MehvLrT_MNv1Xb-My-dIpA/viewform')

# give 2 seconds for the url to be loaded up before filling the form
time.sleep(2)

# select the button we want to choose in radio button and will click
radioButtonElement = web.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
radioButtonElement.click()

reason = "You are too ugly"
# find the HTML element by xpath and fill out the form
# three dots -> more tools -> developer tools -> click top left arrow icon -> select the answer box -> right click the respective chunks of HTML -> copy -> copy xpath
reasonElement = web.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
# pass the answer to the element
reasonElement.send_keys(reason)

# submit
submitButtonElement = web.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
submitButtonElement.click()

# right click "Your Response has been Recorded" and select the class by right clicking and say edit as HTML
getConfirmationDivText = web.find_element_by_css_selector(
    '.freebirdFormviewerViewResponseConfirmationMessage')
print(getConfirmationDivText.text)
