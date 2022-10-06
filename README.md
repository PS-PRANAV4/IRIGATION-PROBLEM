# IRIGATION-PROBLEM
#PROBLEM
### **Objective →**

Write a tiny web app that allow users to create/view Irrigation cycle for the crops

### **Description →**

A lot of our web platforms are about solving complex problems in various disciplines and presenting the solution to the user in an effortless way.

Here, let’s automate the irrigation cycle of the Modern IoT Farms.

The application accepts five inputs:

1. Number of Plots to be irrigated - Say 4 (D1, D2, ... D4)
2. How many motors can be run in parallel? - Say 2 (M1, M2)
3. Irrigation Start Time and End Time - Eg: 060000, 190000 (Time in military format)
4. Motor Runtime - Say 5 minutes
5. Irrigation Cycle Interval - Say 20 minutes (Rest time between irrigation cycles)










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
