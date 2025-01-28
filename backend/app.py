from flask import Flask, jsonify
from flask_cors import CORS
from jobs.scraper import scrape_jobs
from database.db import setup_db, insert_job, get_all_jobs, delete_job
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO) # Set the logging level to INFO
logger = logging.getLogger(__name__) # Create a logger object

CORS(app, resources={r"/*": {"origins": "*"}})

# Init the db
setup_db()


# Scrape jobs and save new ones to the db
@app.route('/jobs', methods=['POST'])
def scrapeNsave():
    try:
        scraped_jobs = scrape_jobs()
        if not scraped_jobs:
            logger.warning("No jobs returned from scraper")
            return jsonify({'message': 'No jobs found'}), 404
        
        logger.info(f"Scraped {len(scraped_jobs)} jobs")
        saved_count = 0
        for job in scraped_jobs:
            try:
                insert_job(job)
                saved_count += 1
            except Exception as e:
                logger.error(f"Failed to save job: {str(e)}")

        return jsonify({
            'message': f"{saved_count} jobs saved",
            'total': len(scraped_jobs),
            'saved': saved_count
        })
    except Exception as e:
        logger.error(f"Scraping failed: {str(e)}")
        return jsonify({'Error': 'Scraping failed'}), 500

# Fetch all jobs from the db
@app.route('/jobs', methods=['GET'])
def fetch_jobs():
    try:
        jobs = get_all_jobs()

        logger.info(f"Retrieved {len(jobs)} jobs from the db")

        return jsonify(jobs)
    
    except Exception as e:
        logger.error(f"Failed to fetch jobs: {str(e)}")

        return jsonify({'Error': 'Failed to fetch jobs'}), 500
    
@app.route('/jobs/<int:id>', methods=['DELETE'])
def remove_job(id):
    try:
        to_delete = delete_job(id)
        if to_delete:
            return jsonify({
                'message': f'Job with id {id} deleted',
                'deleted': to_delete
            }), 200
        else:
            return jsonify({
                'error': f'Job with id {id} not found'
            }), 404
    except Exception as e:
        return jsonify({
            'error': f'Failed to delete job: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001) # Run the app in debug mode and allow connections from any device on the network