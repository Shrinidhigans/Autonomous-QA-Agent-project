@echo off
echo ======================================
echo   Starting QA Agent Application
echo ======================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Virtual environment not found!
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo Virtual environment found
    call venv\Scripts\activate.bat
)

REM Check if dependencies are installed
python -c "import fastapi" 2>nul
if errorlevel 1 (
    echo Dependencies not installed
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo Dependencies installed
)

echo.
echo ======================================
echo   Starting Backend Server (Port 8000)
echo ======================================
echo.

REM Start backend in new window
start "QA Agent Backend" cmd /k "venv\Scripts\activate.bat && uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000"

echo Waiting for backend to start...
timeout /t 5 /nobreak >nul

REM Check if backend is running
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo Backend failed to start
    echo Check the backend window for errors
    pause
    exit /b 1
) else (
    echo Backend is running at http://localhost:8000
)

echo.
echo ======================================
echo   Starting Frontend (Streamlit)
echo ======================================
echo.
echo Frontend will open in your browser...
echo.
echo To stop: Close both command windows
echo.

REM Start streamlit
streamlit run frontend\streamlit_app.py

pause