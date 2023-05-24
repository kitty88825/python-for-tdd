from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
browser.get('http://localhost:8000')

assert 'Django' in browser.title
