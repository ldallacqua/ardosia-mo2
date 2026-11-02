@echo off
rem Abre o MO2 com o motor de fontes FreeType, que deixa o texto mais suave.
rem Copie este arquivo para a pasta do ModOrganizer.exe e abra o MO2 por ele.
set QT_QPA_PLATFORM=windows:fontengine=freetype
start "" "%~dp0ModOrganizer.exe"
