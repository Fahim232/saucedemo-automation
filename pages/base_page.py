from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 90)

    def open(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def elements(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].click()", element)

    def type(self, by, locator, text):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script(
            """
            var el = arguments[0];
            var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(el, arguments[1]);
            el.dispatchEvent(new Event('input', {bubbles: true}));
            """,
            element,
            text,
        )

    def text(self, by, locator):
        return self.find(by, locator).text