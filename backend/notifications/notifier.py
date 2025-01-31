import yagmail
import logging

# Set up logging
logger = logging.getLogger(__name__)

def setup_email_sender(sender_email, app_password):
    return yagmail.SMTP(sender_email, app_password)

def send_notifications(yag, recipient_email, num_new_jobs, frontend_url):
    subject = f"Job Tracker: {num_new_jobs} New Jobs Found!"
    
    content = [
        f"""Hello!,
        
        We found {num_new_jobs} new job(s)!,
        You can view all jobs at: {frontend_url},

        Best regards,

        Your Job Tracker"""
    ]
    
    try:
        yag.send(
            to=recipient_email,
            subject=subject,
            contents=content
        )
        logger.info(f"Email notification sent for {num_new_jobs} new jobs")
        return True
    except Exception as e:
        logger.error(f"Failed to send email notification: {str(e)}")
        return False
