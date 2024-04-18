@echo off

set PYTHON_DOWNLOAD_URL=https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

rem Define download destination
set DOWNLOAD_DESTINATION=python-3.10.0-amd64.exe

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
::--------------------------------------
where python > nul 2>&1
if %errorlevel% == 0 (
    python3 BrutePy.py
) else (
    bitsadmin /transfer "PythonDownload" %PYTHON_DOWNLOAD_URL% %DOWNLOAD_DESTINATION%
    python3 BrutePy.py
)


pause