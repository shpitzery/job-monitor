# Job Monitor

A web scraping program for tracking R&D student and intern job opportunities across major tech companies.

## Project Information

This project provides an automated job tracking system that monitors and aggregates job postings from multiple tech companies' career pages. Currently, the tracker scrapes positions from Apple, Amazon, and Nvidia, with the capability to expand to additional sources.

## Libraries/Frameworks/Modules

This project leverages several powerful technologies:

- React (Frontend)
- Flask (Backend API)
- Selenium (Web Scraping)
- SQLite (Data Storage)
- Chrome WebDriver (Browser Automation)
- Schedule (Task Automation)
- Yagmail (Email Notifications)

## Setting Up the Project

### Backend Setup

1. Navigate to the backend directory
2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python app.py
   ```
   The server will run on `http://localhost:5001`

### Frontend Setup

1. Navigate to the frontend directory
2. Install dependencies:
   
   ```bash
   npm install
   ```
4. Start the React application:
   
   ```bash
   npm start
   ```
   The application will run on `http://localhost:3001`

## Email Notifications

The system includes an automated email notification service. To configure:

1. Update the email configuration in `config.py`:
   
   ```python
   EMAIL_CONFIG = {
       "sender": "your-email@gmail.com",
       "recipient": "recipient-email@gmail.com",
       "app_password": "your-app-password",
       "frontend_url": "http://localhost:3001"
   }
   ```
3. Enable notifications by ensuring the scheduler is running

## Automated Job Tracking

The system automatically checks for new job postings every 6 hours. When new positions are found, it:
- Saves them to the SQLite database
- Sends email notifications to configured recipients
- Updates the frontend display

## Legal Disclaimer

This project employs web scraping to extract publicly available data from websites. We adhere to the following practices:

1. All scraped data is publicly accessible and not behind any authentication barriers
2. The scraping process complies with applicable laws and regulations
3. We respect robots.txt guidelines and implement reasonable request rates

If you represent any of the tracked companies and have concerns about your site's data being scraped, please contact us for prompt resolution.

## Contributing

Contributions are welcome! Feel free to:
- Add support for additional companies
- Enhance the frontend interface
- Improve scraping reliability
- Add new features

Please ensure your contributions maintain the project's commitment to ethical web scraping practices.
