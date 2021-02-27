import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):  # 測試前執行
        self.browser = webdriver.Firefox(executable_path='/tmp/geckodriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):  # 測試後執行
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith 聽到一個很酷的新線上待辦事項app
        # 他去查看他的首頁
        self.browser.get('http://localhost:8000')

        # 他發現網頁標題與標題顯示待辦事項清單
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 他馬上受邀輸入一個待辦事項
if __name__ == '__main__':
    unittest.main(warnings='ignore')

browser.quit()
