This is a simple flask api which support two urls -> http://127.0.0.1:8000/meter,http://127.0.0.1:8000/meter/number
run the following commands to install necessary libraries
pip install flask
pip install gunicorn
pip install pandas

to run the app simply use the command
 gunicorn app1:app