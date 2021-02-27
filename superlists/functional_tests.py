from selenium import webdriver


browser = webdriver.Firefox(executable_path='/tmp/geckodriver')

# Edith 聽到一個很酷的新線上待辦事項app
# 他去查看他的首頁
browser.get('http://localhost:8000')

# 他發現網頁標題與標題顯示待辦事項清單
assert 'To-Do' in browser.title

# 他馬上受邀輸入一個待辦事項
# 他在文字方塊輸入"購買孔雀羽毛"
# (Edith 的興趣是綁蒼蠅魚餌)

# 當他按下 enter 時，網頁會更新，現在網頁列出
# "1: 購買孔雀羽毛"，一個待辦事項清單項目

# 此時仍然有一個文字方塊，讓他可以加入另一個項目
# 他輸入 "使用孔雀羽毛來製作一隻蒼蠅" (Edith 非常有條理)

# 網頁再次更新，現在他的清單有這兩個項目

# Edith 不知道網站能否記得他的清單
# 接著他看到網站產生一個唯一的 URL 給他
# 網頁有一些文字說明這個效果

# 他前往那個 URL 他的待辦事項仍然在那裡

# 他很滿意地上床睡覺

browser.quit()
