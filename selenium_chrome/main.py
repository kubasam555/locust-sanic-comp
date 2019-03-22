import time

from selenium import webdriver


FRAMEWORKS = {
    'sanic': 'https://sanic-start-project.herokuapp.com/',
    'django': 'https://django-sanic-comp.herokuapp.com/',
    'flask': 'https://flask-sanic-comp.herokuapp.com/'
}

LOCUST_PORTS = {
    'sanic': '8089',
    'django': '8090',
    'flask': '8091',
}

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

LOCUST_HOST = 'http://127.0.0.1'

CHROMEDRIVER_URL = '/Users/jakubsamsel/Pliki/chromedriver_73'


KEYS = (
    ('locust_count', 1000),
    ('hatch_rate', 10)
)


class TestCases:
    drivers = []

    def __init__(self):
        self.get_drivers()
        self.fill_form()
        self.submit()

    def get_drivers(self):
        for name, port in LOCUST_PORTS.items():
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option('detach', True) #prevent before closing
            url = f'{LOCUST_HOST}:{port}'
            driver = webdriver.Chrome(CHROMEDRIVER_URL, chrome_options=chrome_options)
            driver.get(url)
            self.drivers.append(driver)

    def fill_form(self):
        for driver in self.drivers:
            for item in KEYS:
                driver.find_element_by_id(item[0]).send_keys(item[1])

    def submit(self):
        input("Press Enter to start...")
        for driver in self.drivers:
            locust_form = driver.find_element_by_id('swarm_form')
            locust_form.submit()


if __name__ == '__main__':
    start = time.perf_counter()
    TestCases()
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
