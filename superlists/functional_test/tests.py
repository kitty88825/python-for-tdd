import time

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys


MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):  # 測試前執行
        self.browser = webdriver.Firefox(executable_path='/tmp/geckodriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):  # 測試後執行
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
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

        # 當他按下 enter 時，網頁會更新，現在網頁列出
        # "1: 購買孔雀羽毛"，一個待辦事項清單項目
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # 此時仍然有一個文字方塊，讓他可以加入另一個項目
        # 他輸入 "使用孔雀羽毛來製作一隻蒼蠅" (Edith 非常有條理)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 網頁再次更新，現在他的清單有這兩個項目
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table(
            '2: Use peacock feathers to make a fly',
        )

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
