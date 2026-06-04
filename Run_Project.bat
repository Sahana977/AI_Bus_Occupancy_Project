@echo off

start cmd /k "cd /d %~dp0backend && ..\venv\Scripts\activate && python -m uvicorn main:app --reload"

timeout /t 3 > nul

start cmd /k "cd /d %~dp0frontend && npm run dev"

timeout /t 5 > nul

start http://127.0.0.1:8000/docs
start http://localhost:5173

exit