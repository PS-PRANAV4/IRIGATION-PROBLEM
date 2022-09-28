# IRIGATION-PROBLEM


I HAVE PUT DJANGO SECRET KEY so that no need to look for another key and u can easily setup the app

first install requirment.txt

first of all need to install rabbitmq and run it in your device
then run celery worker by typing -> celery -A scrap  worker -l info
celery will automatically connect to the localhost if u want to connect to certain host define it in the settings file

API
'refresh' -> to start the task of irigation -> method:post -> inputs -> plotarray:array of the plot, motor:array of motor, motor_run_time, motor running time, irigation_cycle:irigation cycle time gap
'getirigation' -> to get the data of all workings

NOTE: there are certain problems in this app the celery worker is running in infinite loop after starting the task so to end the task need to end the celery working or database will be full of data

#this model can't be used in real life and need modification and this is only for my studying purpose
