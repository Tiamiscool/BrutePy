# BrutePy
BrutePy is a python/batch based program that automatically makes a password list depending on the user's choice. 
Using smb, the bruteforce batch file executes made by ebola man with a few configs. it will eventually crack a number password, it always does.

Here is a Rundown of How The Program executes:

1. BrutePy.bat is run, giving administrative privilages and opening BrutePy.py.
if python isn't installed, it will automatically download it

2. BrutePy.py is executed by BrutePy.bat, and first creates the password list according
to the users liking. Then, the SSID and IP address of the client is asked for. The password list is written in
passwords.txt, the SSID in user.txt, and the IP address is written in ipaddr.txt.

3. bruteforce.bat, made by ebola man is executed by BrutePy.py. The Credentials from the
text files are used, and so is the passwords list. Once done, all the text files
are wiped.

Tutorial for making the password list:

Step 1. do Research

![Screenshot (4)](https://github.com/Tiamiscool/BrutePy/assets/107582387/fb0ba60a-83cc-4aaa-8670-ceb06c06d54a)

Step 2. Launch app
![Screenshot (7)](https://github.com/Tiamiscool/BrutePy/assets/107582387/0313acd9-4276-4597-af99-3dad5b6949de)

step 3. Enter 9s until the maximum digit
![Screenshot (6)](https://github.com/Tiamiscool/BrutePy/assets/107582387/e15d41e8-7f42-4caa-b5fa-61f3c9603eb6)

