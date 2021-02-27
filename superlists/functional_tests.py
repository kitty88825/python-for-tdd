import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 他馬上受邀輸入一個待辦事項
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item',
        )

        # 他在文字方塊輸入"購買孔雀羽毛"
        # (Edith 的興趣是綁蒼蠅魚餌)
        inputbox.send_keys('Buy peacock feathers')
        # 當他按下 enter 時，網頁會更新，現在網頁列出
        # "1: 購買孔雀羽毛"，一個待辦事項清單項目
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        # 此時仍然有一個文字方塊，讓他可以加入另一個項目
        # 他輸入 "使用孔雀羽毛來製作一隻蒼蠅" (Edith 非常有條理)
        self.fail('Finish the test!')

        # 網頁再次更新，現在他的清單有這兩個項目
        # Edith 不知道網站能否記得他的清單
        # 接著他看到網站產生一個唯一的 URL 給他
        # 網頁有一些文字說明這個效果
        # 他前往那個 URL 他的待辦事項仍然在那裡
        # 他很滿意地上床睡覺
if __name__ == '__main__':
    unittest.main(warnings='ignore')

browser.quit()
