from selenium.webdriver.common.by import By

# Companies configuration
companies = {
    "Apple": {
        "BASE_URL": "https://jobs.apple.com/en-il/search?sort=relevance&key=student&location=israel-ISR",
        "Locators": 
        {
            'container': (By.CSS_SELECTOR, 'tbody[id*=accordion]'),
            'title': (By.CSS_SELECTOR, 'td.table-col-1 a'),
            'url': (By.CSS_SELECTOR, 'td.table-col-1 a'),
            'posted': (By.CSS_SELECTOR, 'td.table-col-1 span[id*="posted"]'),
            'location': (By.CSS_SELECTOR, 'td.table-col-2')
        }
    },
    "Amazon": {
        "BASE_URL": "https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&business_category%5B%5D=student-programs&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=Israel&base_query=&city=&country=ISR&region=&county=&query_options=&",
        "Locators": 
        {
        'container': (By.CLASS_NAME, 'job'),
        'title': (By.CSS_SELECTOR, "h3[class*='job-title'] a"),
        'url': (By.CSS_SELECTOR, "h3[class*='job-title'] a"),
        'posted': (By.CSS_SELECTOR, 'h2.posting-date'),
        'location': (By.CSS_SELECTOR, 'li')
        },
    },
}