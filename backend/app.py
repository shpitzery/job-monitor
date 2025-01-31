from flask import Flask, jsonify
from flask_cors import CORS
from database.db import setup_db, get_all_jobs
from notifications.schedule_manager import scheduler, start_scheduler
import logging
import threading
import time

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Init the db
setup_db()

@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        logger.info("Getting all jobs from db")
        jobs = get_all_jobs()
        logger.info(f"Returned {len(jobs)} jobs")
        return jsonify(jobs)
    
    except Exception as e:
        logger.error(f"Error fetching jobs: {str(e)}")
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    scheduler()

    # Start the scheduler in a separate thread
    t = threading.Thread(target=start_scheduler)
    t.daemon = True
    t.start()
    logger.info("Scheduler started in background thread")

    logger.info("Starting Flask server")
    app.run(debug=True, host='0.0.0.0', port=5001)

    # while True:
    #     time.sleep(1)