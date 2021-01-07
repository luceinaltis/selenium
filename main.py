from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenshooter():
    def __init__(self, keyword):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword

    def start(self):
        self.browser.get("https://google.com")

        KEYWORD = "buy domain"

        search_bar = self.browser.find_element_by_class_name("gLFyf")

        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        try:
            trash_element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))

            self.browser.execute_script("""
                const remove_element = arguments[0]
                remove_element.parentElement.removeChild(remove_element)
            """, trash_element)
        except Exception:
            pass

        search_results = self.browser.find_element_by_id(
            "rso").find_elements_by_class_name("g")

        for index, search_result in enumerate(search_results):
            search_result.screenshot(f"screenshots/{self.keyword}_{index}.png")

    def finish(self):
        self.browser.quit()


browser = GoogleKeywordScreenshooter("buy domain")
browser.start()
browser.finish()

py_browser = GoogleKeywordScreenshooter("sell domain")
py_browser.start()
py_browser.finish()

# browser.quit()
