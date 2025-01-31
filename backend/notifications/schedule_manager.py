from scraper_manager import scrape_jobs
from database.db import insert_job
from .notifier import setup_email_sender, send_notifications
from config import EMAIL_CONFIG
import logging
import schedule
import time

logging.basicConfig(level=logging.INFO) # Set the logging level to INFO
logger = logging.getLogger(__name__) # Create a logger object

yag = setup_email_sender(EMAIL_CONFIG['sender'], EMAIL_CONFIG['app_password']) # Initialize the email sender

def scheduler():
    logger.info("Scheduled scraping started")
    print(f"Scheduler triggered at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        scraped_jobs = scrape_jobs()
        if not scraped_jobs:
            logger.warning("No jobs returned from scraper")
            return
        
        saved_count = 0
        for job in scraped_jobs:
            try:
                if insert_job(job): # increment only if a new job inserted
                    saved_count += 1
            except Exception as e:
                logger.error(f"Failed to save job: {str(e)}")

        logger.info(f"Scheduled scraping completed. Found {len(scraped_jobs)} jobs")

        if saved_count > 0:
            send_notifications(
                yag, 
                EMAIL_CONFIG['recipient'], 
                saved_count, 
                EMAIL_CONFIG['frontend_url'])

    except Exception as e:
        logger.error(f"Scraping failed: {str(e)}")

def start_scheduler():
    # schedule.every(1).minutes.do(scheduler) # Run the scraper every 1 minute
    schedule.every(6).hours.do(scheduler) # Run the scraper every 6 hours

    while True:
        schedule.run_pending() 
        time.sleep(1)