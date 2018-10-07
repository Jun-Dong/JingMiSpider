from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()
# try:
#     browser.get('http://www.baidu.com')
#     input = browser.find_element_by_id('kw')#找到id=kw
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)#等待加载
#     wait.until(EC.presence_of_element_located((By.ID, "content_left")))#等待id=content_left加载处理
#     print(browser.current_url)
#     print("==============")
#     print(browser.get_cookies())
#     print("==============")
#     print(browser.page_source)#网页源码
# finally:
#     browser.close()

# 申明浏览器对象
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()

# 访问网页
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# print(browser.page_source)
# browser.close()

# 查找元素
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first,input_second,input_third)
# browser.close()

# 通用查找方式
# from selenium import webdriver
# from  selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID,'q')#上面的机械,结果一样
# print(input_first)
# browser.close()

# 多个元素
# from selenium import webdriver
# from  selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(type(lis))
# print(lis)
# browser.close()
#
# from selenium import webdriver
# from  selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
# print(type(lis))
# print(lis)
# browser.close()

# 元素交互操作
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# input = browser.find_element_by_id('q')  # 找到id=q
# input.send_keys('IPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

#交互动作 与元素操作不同
# #将动作附加到动作链中串行执行
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url ='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')#切换到id='iframeResult'的frame
# source = browser.find_element_by_css_selector('#draggable')#找到frame中的对象
# target = browser.find_element_by_css_selector('#droppable')#找到frame中的对象
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()

#执行JavaScript
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

#获取元素信息

#获取元素
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
#
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

#获取文本值
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

#获取ID,位置,标签名,大小
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

#Frame 演示怎样切换父元素frame 切换子元素frame
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
#
# browser = webdriver.Chrome()
# url ='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')#切换到id='iframeResult'的frame
# source = browser.find_element_by_css_selector('#draggable')#找到frame中的对象
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No LOGO')
#
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

#隐式等待
#当使用了隐式等待执行测试的时候,如果Webdrive没有在DOM中找到元素,将继续等待(注意是继续等待),
#超出设定时间后会抛出找不到元素的异常,默认为0

# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('http://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

#显式等待

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# wait = WebDriverWait(browser,10)
# #2个等待条件
# input = wait.until(EC.presence_of_all_elements_located(((By.ID,'q'))))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
#
# print(input,button)

#Cookies#设置登录状态
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

#选项卡管理
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
html=browser.page_source
soup=BeautifulSoup(html,"lxml")
print soup.prettify()
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('http://www.taobao.com')
html=browser.page_source
soup=BeautifulSoup(html,"lxml")
print soup.prettify()
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('http://python.org')