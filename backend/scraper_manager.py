from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import logging
from config import companies

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup():
    try:
        options = webdriver.ChromeOptions()

        options.add_argument('--headless')
        options.add_argument('--disable-cache')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        
        logger.info("Setting up ChromeDriver...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        logger.info("ChromeDriver setup successful")
        return driver
    except WebDriverException as e:
        logger.error(f"Failed to setup ChromeDriver: {str(e)}")
        raise

def positions(driver, company_name: str):
    # driver = None
    try:
        # driver = setup()

        company = companies[company_name]
        base_url = company['BASE_URL']
        locators = company['Locators']

        logger.info(f"Navigating to {company_name} careers page...")
        driver.get(base_url)
        
        # Wait for page load
        wait = WebDriverWait(driver, 20)
        logger.info("Waiting for search input...")
        
        wait.until(
            EC.presence_of_element_located(locators['container'])
        )
        
        # Wait for results to load
        time.sleep(5)
        
        # Look for positions with multiple possible selectors
        logger.info("Looking for position listings...")
        jobs = driver.find_elements(*locators['container'])
        
        print(f"\nFound {len(jobs)} positions:\n")
        
        for job in jobs:
            try:
                title = job.find_element(*locators['title']).text.strip()
                job_url = job.find_element(*locators['url']).get_attribute('href')
                posted = job.find_element(*locators['posted']).text.strip()
                location = job.find_element(*locators['location']).text.strip()

                position = {
                    "Title": title,
                    "URL": job_url,
                    "Posted Date": posted,
                    "Location": location
                }
                # for key, value in position_text.items():
                #     print(f'{key}: {value}')
                # print("-" * 50)

                return position
                
            except Exception as e:
                logger.error(f"Error getting position details: {str(e)}")
                
    except Exception as e:
        logger.error(f"Main error: {str(e)}")
        if driver:
            logger.info("Taking screenshot of error state...")
            driver.save_screenshot("error_screenshot.png")
    finally:
        if driver:
            logger.info("Closing driver...")
            driver.quit()

# if __name__ == "__main__":
#     driver = None
#     driver = setup()
#     for company in companies:
#         positions(driver, company)
    
#     if driver:
#         logger.info("Closing driver...")
#         driver.quit()