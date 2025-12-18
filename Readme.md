<div align="center">

# 🎓 QUIZ MASTER V2

### An Interactive Quiz Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-green.svg)](https://flask.palletsprojects.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.2.13-brightgreen.svg)](https://vuejs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

*A full-stack web application for creating, managing, and taking quizzes with real-time scoring and analytics*

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [API Documentation](#-api-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Database Schema](#-database-schema)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## 🌟 Overview

**Quiz Master V2** is a comprehensive quiz management platform that enables educators and students to create, organize, and participate in interactive quizzes. The application features a modern, responsive UI built with Vue.js and a robust Flask backend with SQLAlchemy ORM for efficient data management.

### Key Highlights

- 🎯 **Subject-based Organization**: Organize quizzes by subjects and chapters
- 👥 **Role-based Access**: Separate interfaces for administrators and students
- 📊 **Real-time Analytics**: Track performance with detailed statistics
- 🔒 **Secure Authentication**: Flask-Security integration for user management
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🚀 **RESTful API**: Clean and well-structured API endpoints

---

## ✨ Features

### For Students
- 📝 **Take Quizzes**: Attempt quizzes organized by subjects and chapters
- 📈 **Score Tracking**: View historical scores and performance metrics
- 📊 **Statistics Dashboard**: Analyze performance across different subjects
- 👤 **User Profile**: Manage account and view personal statistics

### For Administrators
- ➕ **Content Management**: Create and manage subjects, chapters, and questions
- ✏️ **Edit & Update**: Modify existing questions and content
- 🗑️ **Delete Content**: Remove outdated or incorrect material
- 👥 **User Management**: Monitor user activity and performance
- 📊 **Admin Dashboard**: Overview of system statistics and usage

### Core Functionality
- 🔐 **User Authentication**: Secure signup and login system
- 🎲 **Multiple Choice Questions**: Support for MCQ format with JSON-based options
- ⏱️ **Instant Scoring**: Automatic grading with immediate results
- 📅 **History Tracking**: Complete quiz attempt history with timestamps
- 🔄 **CRUD Operations**: Full create, read, update, delete support for all entities

---

## 🏗️ Architecture

Quiz Master V2 follows a modern **client-server architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Vue.js 3 (SPA)                          │  │
│  │  • Vue Router (Navigation)                           │  │
│  │  • Vuex (State Management)                           │  │
│  │  • Bootstrap 5 (Styling)                             │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────┬─────────────────────────────────────┘
                        │
                   REST API (HTTP/JSON)
                        │
┌───────────────────────▼─────────────────────────────────────┐
│                         Backend                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Flask 3.1.0                             │  │
│  │  • Flask-SQLAlchemy (ORM)                            │  │
│  │  • Flask-Security (Authentication)                   │  │
│  │  • Flask-CORS (Cross-Origin Support)                 │  │
│  └────────────────────┬─────────────────────────────────┘  │
│                       │                                     │
│  ┌────────────────────▼─────────────────────────────────┐  │
│  │           SQLAlchemy Database                        │  │
│  │  • Users & Roles                                     │  │
│  │  • Subjects & Chapters                               │  │
│  │  • Questions & Scores                                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | 3.8+ | Core programming language |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) | 3.1.0 | Web framework |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white) | 2.0.38 | ORM for database operations |
| ![Flask-Security](https://img.shields.io/badge/Flask--Security-000000?style=flat&logo=flask&logoColor=white) | Latest | Authentication & authorization |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| ![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=flat&logo=vue.js&logoColor=4FC08D) | 3.2.13 | Frontend framework |
| ![Vue Router](https://img.shields.io/badge/Vue_Router-35495E?style=flat&logo=vue.js&logoColor=4FC08D) | 4.0.3 | Client-side routing |
| ![Vuex](https://img.shields.io/badge/Vuex-35495E?style=flat&logo=vue.js&logoColor=4FC08D) | 4.1.0 | State management |
| ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=flat&logo=bootstrap&logoColor=white) | 5.3.3 | UI components & styling |

### Development Tools
- **Node.js** & **npm**: Frontend package management
- **Webpack**: Module bundling via Vue CLI
- **Babel**: JavaScript transpilation

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**: [Download Python](https://www.python.org/downloads/)
- **Node.js 14+ and npm**: [Download Node.js](https://nodejs.org/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Virtual Environment**: (Recommended) `venv` or `virtualenv`

---

## 🚀 Installation

Follow these steps to set up Quiz Master V2 on your local machine:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Gseyal/QUIZ_MASTER_V2.git
cd QUIZ_MASTER_V2
```

### 2️⃣ Backend Setup

#### Create Virtual Environment

**On Windows:**
```bash
python -m venv env
.\env\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

#### Install Backend Dependencies

```bash
cd app_backend
pip install -r requirement.txt
```

#### Initialize Database

The database will be automatically created when you first run the application. Default tables and schema will be set up based on the models defined in `application/model.py`.

### 3️⃣ Frontend Setup

Open a **new terminal** window and navigate to the frontend directory:

```bash
cd app_frontend
npm install
```

---

## ⚙️ Configuration

### Backend Configuration

The backend configuration is managed in `app_backend/application/config.py`. Default settings include:

- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL
- **Secret Key**: Auto-generated for Flask sessions
- **CORS**: Enabled for frontend communication
- **Server Port**: 5000 (default Flask port)

### Frontend Configuration

Frontend configuration is in `app_frontend/vue.config.js`:

- **API Base URL**: Configured to communicate with backend at `http://localhost:5000`
- **Development Server**: Runs on port 8080 by default

---

## 🎮 Usage

### Starting the Application

You need **two separate terminals** to run both backend and frontend:

#### Terminal 1: Start Backend Server

```bash
cd app_backend
python app.py
```

The Flask server will start at: `http://localhost:5000`

✅ You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: off
```

#### Terminal 2: Start Frontend Development Server

```bash
cd app_frontend
npm run serve
```

The Vue.js development server will start at: `http://localhost:8080`

✅ You should see output like:
```
  App running at:
  - Local:   http://localhost:8080/
  - Network: http://192.168.x.x:8080/
```

### Accessing the Application

Open your browser and navigate to:
```
http://localhost:8080
```

### First Time Setup

1. **Create Admin Account**: 
   - Navigate to the signup page
   - Create an account with admin privileges (Role ID: 1)

2. **Add Content**:
   - Login as admin
   - Add subjects from the dashboard
   - Add chapters to subjects
   - Add questions to chapters

3. **Take Quiz**:
   - Login as student (Role ID: 2)
   - Select a subject and chapter
   - Complete the quiz and view results

---

## 📁 Project Structure

```
QUIZ_MASTER_V2/
├── 📂 app_backend/                 # Flask Backend Application
│   ├── 📂 application/             # Application modules
│   │   ├── __init__.py
│   │   ├── config.py               # Configuration settings
│   │   ├── database.py             # Database initialization
│   │   ├── model.py                # SQLAlchemy models
│   │   └── routes.py               # API route definitions
│   ├── 📂 database/                # SQLite database storage
│   ├── 📂 static/                  # Static files (images, etc.)
│   ├── 📂 templates/               # HTML templates (if any)
│   ├── app.py                      # Application entry point
│   ├── requirement.txt             # Python dependencies
│   └── run.sh                      # Shell script to run server
│
├── 📂 app_frontend/                # Vue.js Frontend Application
│   ├── 📂 public/                  # Public static assets
│   ├── 📂 src/                     # Source files
│   │   ├── 📂 assets/              # Images, fonts, etc.
│   │   ├── 📂 components/          # Reusable Vue components
│   │   │   ├── navbar.vue          # Navigation bar
│   │   │   ├── subject_add.vue     # Add subject modal
│   │   │   ├── subject_update.vue  # Update subject modal
│   │   │   ├── chapter_add.vue     # Add chapter modal
│   │   │   ├── chapter_update.vue  # Update chapter modal
│   │   │   ├── question_add.vue    # Add question modal
│   │   │   ├── question_update.vue # Update question modal
│   │   │   ├── search_modal.vue    # Search functionality
│   │   │   └── add_button.vue      # Reusable add button
│   │   ├── 📂 views/               # Page components
│   │   │   ├── Dashboard.vue       # Main dashboard
│   │   │   ├── chapter.vue         # Chapter view
│   │   │   ├── Quiz.vue            # Quiz taking interface
│   │   │   ├── score.vue           # Score history
│   │   │   ├── stat.vue            # Statistics page
│   │   │   ├── login.vue           # Login page
│   │   │   ├── signup.vue          # Registration page
│   │   │   └── admin_summary.vue   # Admin dashboard
│   │   ├── 📂 router/              # Vue Router configuration
│   │   │   └── index.js            # Route definitions
│   │   ├── 📂 store/               # Vuex store
│   │   │   └── store.js            # State management
│   │   ├── App.vue                 # Root component
│   │   └── main.js                 # Application entry point
│   ├── babel.config.js             # Babel configuration
│   ├── vue.config.js               # Vue CLI configuration
│   ├── package.json                # Node dependencies
│   └── package-lock.json           # Locked dependencies
│
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

---

## 🔌 API Documentation

### Authentication Endpoints

#### POST `/signup`
Register a new user account.

**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "msg": "User created Successfully"
}
```

#### POST `/post`
User login and authentication.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "token": "auth_token_here",
  "name": "john_doe",
  "id": 1,
  "role": "student"
}
```

---

### Subject Management

#### GET `/get_sub`
Retrieve all subjects with their chapters.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Mathematics",
    "description": "Basic mathematics concepts",
    "chapters": [
      {
        "id": 1,
        "chapter": "Algebra"
      }
    ]
  }
]
```

#### POST `/add_data`
Add a new subject, chapter, or question.

**Request Body (Subject):**
```json
{
  "type": "Subject",
  "title": "Physics",
  "description": "Introduction to Physics"
}
```

**Request Body (Chapter):**
```json
{
  "type": "Chapter",
  "subject_id": 1,
  "chapter": "Mechanics"
}
```

**Request Body (Question):**
```json
{
  "type": "Question",
  "chapter_id": 1,
  "question": "What is 2+2?",
  "options": {
    "A": "3",
    "B": "4",
    "C": "5",
    "D": "6"
  },
  "correct": "B"
}
```

#### PUT `/update`
Update existing subject, chapter, or question.

**Request Body:**
```json
{
  "type": "Subject",
  "id": 1,
  "title": "Advanced Mathematics",
  "description": "Updated description"
}
```

#### POST `/delete`
Delete a subject, chapter, or question.

**Request Body:**
```json
{
  "type": "Subject",
  "id": 1
}
```

---

### Quiz Operations

#### POST `/get_question`
Get all questions for a specific chapter.

**Request Body:**
```json
{
  "chapter": 1
}
```

**Response:**
```json
[
  {
    "id": 1,
    "question": "What is 2+2?",
    "options": {
      "A": "3",
      "B": "4",
      "C": "5",
      "D": "6"
    }
  }
]
```

#### POST `/score`
Submit quiz answers and receive score.

**Request Body:**
```json
{
  "1": "B",
  "2": "A",
  "id": 1
}
```
*(Keys are question IDs, values are selected answers)*

**Response:**
```json
{
  "score": 2
}
```

---

### Statistics & Analytics

#### POST `/get_score`
Get score history for a user.

**Request Body:**
```json
{
  "user_id": 1
}
```

**Response:**
```json
[
  {
    "date": "2024-01-15T10:30:00",
    "subject": "Mathematics",
    "chapter": "Algebra",
    "score": 8,
    "outof": 10
  }
]
```

#### POST `/stat`
Get detailed statistics for a user.

**Request Body:**
```json
{
  "id": 1
}
```

**Response:**
```json
{
  "name": "john_doe",
  "user_id": 1,
  "current_date": "2024-01-15",
  "subjects": [
    {
      "name": "Mathematics",
      "total_chapters": 5,
      "attempted_chapters": 3,
      "score": 25,
      "outof": 50
    }
  ]
}
```

#### GET `/admin_summary`
Get admin dashboard summary.

**Response:**
```json
{
  "user_count": 150,
  "subjects": [
    {
      "name": "Mathematics",
      "chapter_count": 5
    }
  ]
}
```

---

## 🗃️ Database Schema

### Entity Relationship Diagram

```
┌─────────────┐         ┌──────────────┐
│    User     │         │     Role     │
├─────────────┤         ├──────────────┤
│ id (PK)     │◄───────►│ id (PK)      │
│ username    │  Many   │ name         │
│ email       │   to    │ description  │
│ password    │  Many   │              │
│ active      │         └──────────────┘
│ confirmed_at│
└──────┬──────┘
       │ One
       │ to
       │ Many
       ▼
┌─────────────┐
│    Score    │
├─────────────┤
│ id (PK)     │
│ user_id(FK) │
│ subject     │         ┌──────────────┐
│ chapter     │         │   Subject    │
│ score       │         ├──────────────┤
│ date        │         │ id (PK)      │
└─────────────┘         │ subject      │
                        │ description  │
                        └──────┬───────┘
                               │ One
                               │ to
                               │ Many
                               ▼
                        ┌──────────────┐
                        │   Chapter    │
                        ├──────────────┤
                        │ id (PK)      │
                        │ subject_id   │
                        │ chapter      │
                        └──────┬───────┘
                               │ One
                               │ to
                               │ Many
                               ▼
                        ┌──────────────┐
                        │   Question   │
                        ├──────────────┤
                        │ id (PK)      │
                        │ chapter_id   │
                        │ question     │
                        │ options(JSON)│
                        │ correct      │
                        └──────────────┘
```

### Table Descriptions

**Users Table**: Stores user account information with authentication details

**Roles Table**: Defines user roles (Admin, Student, etc.)

**Subjects Table**: Top-level organization for quiz content

**Chapters Table**: Subdivisions within subjects

**Questions Table**: Individual quiz questions with multiple choice options

**Scores Table**: Historical record of quiz attempts and results

---

## 📸 Screenshots

> **Note**: Add screenshots of your application here to showcase the UI/UX

### Dashboard
![Dashboard](https://via.placeholder.com/800x400/4A90E2/FFFFFF?text=Dashboard+View)
*Main dashboard showing available subjects*

### Quiz Interface
![Quiz](https://via.placeholder.com/800x400/7B68EE/FFFFFF?text=Quiz+Interface)
*Interactive quiz taking experience*

### Statistics
![Statistics](https://via.placeholder.com/800x400/50C878/FFFFFF?text=Statistics+Dashboard)
*Performance analytics and score tracking*

### Admin Panel
![Admin](https://via.placeholder.com/800x400/FF6B6B/FFFFFF?text=Admin+Panel)
*Content management interface*

---

## 🗺️ Roadmap

### Planned Features

- [ ] **Timer Functionality**: Add countdown timer for quizzes
- [ ] **Question Types**: Support for true/false, fill-in-the-blank, and essay questions
- [ ] **Image Support**: Allow images in questions and answers
- [ ] **Export Results**: Download quiz results as PDF/CSV
- [ ] **Email Notifications**: Send score reports via email
- [ ] **Leaderboard**: Global and subject-wise leaderboards
- [ ] **Dark Mode**: Toggle between light and dark themes
- [ ] **Mobile App**: Native mobile applications for iOS/Android
- [ ] **Social Features**: Share results on social media
- [ ] **Advanced Analytics**: ML-based performance insights

### Known Issues

- CORS configuration may need adjustment for production deployment
- Password hashing should be reviewed for security best practices
- Database migration system should be implemented for schema updates

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Getting Started

1. **Fork the repository**
2. **Create your feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Contribution Guidelines

- Follow the existing code style and conventions
- Write clear, descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

✅ Commercial use  
✅ Modification  
✅ Distribution  
✅ Private use  

⚠️ Liability  
⚠️ Warranty  

---

## 💬 Support

Need help? Here are some ways to get support:

### Documentation
- 📖 [Wiki](https://github.com/Gseyal/QUIZ_MASTER_V2/wiki) - Comprehensive guides and tutorials
- 💡 [FAQ](https://github.com/Gseyal/QUIZ_MASTER_V2/wiki/FAQ) - Frequently asked questions

### Community
- 🐛 [Issue Tracker](https://github.com/Gseyal/QUIZ_MASTER_V2/issues) - Report bugs or request features
- 💬 [Discussions](https://github.com/Gseyal/QUIZ_MASTER_V2/discussions) - Ask questions and share ideas

### Contact
- 📧 Email: support@quizmaster.com
- 🐦 Twitter: [@QuizMasterApp](https://twitter.com/QuizMasterApp)
- 💼 LinkedIn: [Quiz Master](https://linkedin.com/company/quizmaster)

---

## 🙏 Acknowledgments

- **Flask Community** - For the excellent web framework
- **Vue.js Team** - For the reactive frontend framework
- **Bootstrap** - For the responsive UI components
- **All Contributors** - For your valuable contributions to this project

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/Gseyal/QUIZ_MASTER_V2?style=social)
![GitHub forks](https://img.shields.io/github/forks/Gseyal/QUIZ_MASTER_V2?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Gseyal/QUIZ_MASTER_V2?style=social)
![GitHub issues](https://img.shields.io/github/issues/Gseyal/QUIZ_MASTER_V2)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Gseyal/QUIZ_MASTER_V2)
![GitHub last commit](https://img.shields.io/github/last-commit/Gseyal/QUIZ_MASTER_V2)

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

Made with ❤️ by [Gseyal](https://github.com/Gseyal)

**[Back to Top](#-quiz-master-v2)**

</div>
