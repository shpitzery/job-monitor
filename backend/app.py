from database.db import setup_db
from notifications.schedule_manager import scheduler, start_scheduler
import threading
import time

# Init the db
setup_db()

if __name__ == '__main__':
    scheduler()

    # Start the scheduler in a separate thread
    t = threading.Thread(target=start_scheduler)
    t.daemon = True
    t.start()

    while True:
        time.sleep(1)