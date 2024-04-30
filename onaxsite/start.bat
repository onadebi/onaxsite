echo "\n*************RUNNING SHELL SCRIPT*************\n"

@REM # Remove the staticfiles folder
rmdir /s /q staticfiles

@REM # Run the shell script
py manage.py collectstatic

@REM # Run the server
py manage.py runserver

echo "\n*************SHELL SCRIPT EXECUTION COMPLETED*************\n"