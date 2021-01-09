import time
from math import ceil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ResponsiveTester:
    def __init__(self, urls):
        self.urls = urls
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.sizes = [
            480, 960, 1024, 1366, 1920,
        ]
        self.COMPUTER_HEIGHT = 1173

    def start(self):
        for url in self.urls:
            self.screenshot(url)

    def screenshot(self, url):
        self.browser.get(url)
        for size in self.sizes:
            self.browser.set_window_size(size, self.COMPUTER_HEIGHT)
            scroll_size = self.browser.execute_script("""
                return document.body.scrollHeight
            """)
            total_sections = ceil(scroll_size / self.COMPUTER_HEIGHT)
            for section in range(total_sections+1):
                self.browser.execute_script(
                    f"window.scrollTo(0, {(section) * self.COMPUTER_HEIGHT})")
                self.browser.save_screenshot(
                    f"screenshots/{size}x{section}.png")
                time.sleep(1)


tester = ResponsiveTester(["https://nomadcoders.co", "https://google.com"])
tester.start()
