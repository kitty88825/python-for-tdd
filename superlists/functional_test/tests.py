import time

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):  # 測試前執行
        self.browser = webdriver.Firefox(executable_path='/tmp/geckodriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):  # 測試後執行
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith 聽到一個很酷的新線上待辦事項app
        # 他去查看他的首頁
        self.browser.get(self.live_server_url)

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
        # 當他按下 enter 時，他會被帶到一個新的 URL
        # 現在網頁列出 "1: Buy peacock feathers"
        # 一個待辦事項清單項目
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/list/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 此時仍然有一個文字方塊，讓他可以加入另一個項目
        # 他輸入 "使用孔雀羽毛來製作一隻蒼蠅" (Edith 非常有條理)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 網頁再次更新，現在他的清單有這兩個項目
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly',
        )

        # 在新的使用者 Framcis 來到網站

        ## 我們使用一個新的瀏覽器工作階段來確保
        ## Edith 的任何資訊都不會被 cookies 等機制送出
        self.browser.quit()
        self.browser = webdriver.Firefox(executable_path='/tmp/geckodriver')

        # Francis 造訪首頁。沒有任何 Edith 的清單的跡象
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis 輸入一個新的項目，做出一個新的清單
        # 他比 Edith 無趣...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis 取得他自己的獨一無二 URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/list/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 同樣的，沒有 Edith 的清單的任何跡象
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 他很滿意地上床睡覺
