<p align="center">
  <img src="files/static/img/fplogo.png" alt="FootPrint Logo" width="200">
</p> 


<h3 align="center">Track - Detect - Protect</h3>

<p align="center">
  A data breach detection and monitoring application that helps users identify if their personal information has been compromised.
</p>

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Security](#security)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## About

FootPrint is a web application designed to help users discover whether their email addresses have been exposed in known data breaches. By leveraging the HaveIBeenPwned API and Ghostery TrackerDB, FootPrint provides real-time breach detection with detailed information about compromised data types, breach dates, and affected services.

The application features a modern, responsive interface with dark/light theme support, secure user authentication with brute force protection, and a personalized dashboard for monitoring your digital footprint.

---

## Features

### Landing Page
- Hero section with service statistics (Files Monitored, Detection Time, Integrations)
- Key features showcase with visual cards
- Step-by-step "How It Works" guide
- Dark/Light theme toggle
- Modal-based authentication (Login/Signup)
- Scroll-to-top button

### Authentication System
- User registration with email validation
- Secure login with session management
- Rate limiting to prevent brute force attacks
- 5-minute account lockout after 3 failed attempts
- Password hashing using PBKDF2:SHA256

### Dashboard
- Personalized greeting for logged-in users
- Email breach checking via HaveIBeenPwned API
- Detailed breach results including:
  - Breach name and date
  - Description of the incident
  - Types of compromised data
- Loading indicators and error handling
- Dark/Light theme toggle
- Responsive two-column layout

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python 3.10+, Flask |
| **Database** | SQLite, SQLAlchemy ORM |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Templating** | Jinja2 |
| **External API** | HaveIBeenPwned API v3, Ghostery TrackerDB |
| **Security** | Werkzeug (password hashing) |

---

## Project Structure

```
footprint/
├── files/
│   ├── app.py                      # Main Flask application
│   ├── security.py                 # Login security & rate limiting
│   ├── instance/
│   │   ├── data.db                 # User database (SQLite)
│   │   └── ratings.db              # Ratings database
│   ├── templates/
│   │   ├── index.html              # Landing page
│   │   ├── dashboard.html          # User dashboard
│   │   ├── login.html              # Login modal
│   │   └── signup.html             # Signup modal
│   ├── static/
│   │   ├── styles.css              # Landing page styles
│   │   ├── dashboardStyles.css     # Dashboard styles
│   │   ├── script.js               # Landing page JavaScript
│   │   ├── dashboardScripts.js     # Dashboard JavaScript
│   │   └── img/
│   │       ├── fplogo.png          # Application logo
│   │       ├── tbg.png             # Landing page background
│   │       └── tbbg.png            # Dark theme background
│   └── venv/                       # Python virtual environment
├── .gitignore
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/footprint.git
   cd footprint
   ```

2. **Navigate to the files directory**
   ```bash
   cd files
   ```

3. **Create and activate a virtual environment**

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy werkzeug
   ```

5. **Configure the secret key (Important for Production)**

   Open `app.py` and replace the placeholder secret key:
   ```python
   # Change this line:
   app.secret_key = 'your_secret_key_here'

   # To use an environment variable:
   import os
   app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the application**

   Open your browser and navigate to: `http://127.0.0.1:5000`

---

## Usage

### Getting Started

1. **Create an Account**
   - Click the "Sign Up" button on the landing page
   - Enter your username, email, and password
   - Submit the registration form

2. **Log In**
   - Click the "Log In" button
   - Enter your credentials
   - You will be redirected to your dashboard

3. **Check for Data Breaches**
   - On the dashboard, enter your email address in the form
   - Click "Check for Breaches"
   - View the results showing any known breaches

4. **Theme Toggle**
   - Use the "Theme Toggle" button to switch between light and dark modes
   - Your preference is applied across the application

---

## Screenshots

> Add your screenshots to the `files/static/img/` directory and update this section.

| Landing Page | Dashboard |
|--------------|-----------|
| *Screenshot coming soon* | *Screenshot coming soon* |

---

## Security

### Authentication Security

- **Password Hashing**: All passwords are hashed using PBKDF2:SHA256 algorithm via Werkzeug
- **Session Management**: Flask sessions are used for maintaining user state
- **Rate Limiting**: Login attempts are limited to prevent brute force attacks
- **Account Lockout**: After 3 failed login attempts, the account is locked for 5 minutes

### Security Recommendations for Production

1. **Environment Variables**: Move the secret key to an environment variable
   ```bash
   export SECRET_KEY='your-secure-random-key'
   ```

2. **HTTPS**: Deploy behind a reverse proxy with SSL/TLS encryption

3. **Database**: Consider migrating to PostgreSQL or MySQL for production

4. **API Key**: The HaveIBeenPwned API may require an API key for certain requests. Consider implementing a backend proxy to handle API calls securely.

### Known Considerations

- The HaveIBeenPwned API is currently called from the client-side, which may encounter CORS restrictions. For production, implement a backend proxy endpoint to handle these requests.

---

## API Reference

### HaveIBeenPwned Integration

FootPrint uses the [HaveIBeenPwned API v3](https://haveibeenpwned.com/API/v3) to check for data breaches.

**Endpoint Used:**
```
GET https://haveibeenpwned.com/api/v3/breachedaccount/{email}
```

**Response Codes:**
| Code | Description |
|------|-------------|
| 200 | Breaches found, returns JSON array |
| 404 | No breaches found for the account |
| 429 | Rate limit exceeded |

**Note:** Some API features may require a paid API key. Visit [HaveIBeenPwned](https://haveibeenpwned.com/API/Key) for more information.

---

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Areas for Contribution

- Backend API proxy for HaveIBeenPwned requests
- Additional breach monitoring features
- UI/UX improvements
- Test coverage
- Documentation improvements

---

## License

This project uses the MIT License.

---

<p align="center">
  Made with care by the FootPrint Team
</p>
