set PROFILE_NAME=%SSID%
set XML_FILE=%TEMP%\wifi_profile.xml

(
echo ^<?xml version="1.0"?^>
echo ^<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1"^>
echo   ^<name^>%PROFILE_NAME%^</name^>
echo   ^<SSIDConfig^>
echo     ^<SSID^>
echo       ^<name^>%SSID%^</name^>
echo     ^</SSID^>
echo   ^</SSIDConfig^>
echo   ^<connectionType^>ESS^</connectionType^>
echo   ^<connectionMode^>auto^</connectionMode^>
echo   ^<MSM^>
echo     ^<security^>
echo       ^<authEncryption^>
echo         ^<authentication^>WPA2PSK^</authentication^>
echo         ^<encryption^>AES^</encryption^>
echo         ^<useOneX^>false^</useOneX^>
echo       ^</authEncryption^>
echo       ^<sharedKey^>
echo         ^<keyType^>passPhrase^</keyType^>
echo         ^<protected^>false^</protected^>
echo         ^<keyMaterial^>%PASSWORD%^</keyMaterial^>
echo       ^</sharedKey^>
echo     ^</security^>
echo   ^</MSM^>
echo ^</WLANProfile^>
) > "%XML_FILE%"
netsh wlan add profile filename="%XML_FILE%" >nul
netsh wlan connect name="%PROFILE_NAME%"
del "%XML_FILE%"
