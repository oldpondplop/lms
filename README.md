# 🚀 LMS 🚀
Say goodbye to appshit 🏴‍☠️

### Getting started
```bash
./start.sh
```

### Python environment
```bash
cd backend
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

### Backend (FastAPI)
```bash
cd backend
fastapi run app/main.py
```

### NODE environment 
[Install nvm](https://github.com/nvm-sh/nvm)
```bash
nvm install node # "node" is an alias for the latest version
nvm install-latest-npm
```

### Frontend (React + Vite)
```bash
cd frontend
npm install  
npm run dev
```

### Project Structure
```bash
lms/
│── backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py       # Entry point of FastAPI
│   │   ├── models.py     # SQLAlchemy models
│   │   ├── database.py   # Database setup
│   │   ├── routes/       # API endpoints (courses, quizzes, auth, etc.)
│   │   ├── services/     # Business logic
│   │   ├── schemas.py    # Pydantic models
│   │   ├── auth.py       # Authentication & Security (JWT)
│   │   ├── config.py     # Configurations (env variables)
│   ├── requirements.txt  # Backend dependencies
│   ├── Dockerfile        # Backend containerization
│   ├── vercel.json       # Vercel config for backend deployment
│── frontend/             # React frontend (Vite)
│   ├── src/
│   │   ├── api/          # API calls
│   │   ├── components/   # Reusable components
│   │   ├── pages/        # Page-based routing
│   │   ├── hooks/        # Custom hooks
│   │   ├── context/      # State management (Context API)
│   │   ├── App.jsx       # Root component
│   │   ├── main.jsx      # Entry point for React
│   ├── vite.config.js    # Vite configuration
│   ├── package.json      # Frontend dependencies
│   ├── Dockerfile        # Frontend containerization
│   ├── vercel.json       # Vercel config for frontend deployment
│── .gitignore
│── README.md
```