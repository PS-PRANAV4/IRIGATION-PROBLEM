from __future__ import absolute_import, unicode_literals
from celery import shared_task
from requests_html import HTMLSession
from .models import Plan,Irigation
import asyncio
from datetime import datetime
from asgiref.sync import sync_to_async

index = 0

@shared_task
def add(a,motor_array,motor_run_time,irigation_cycle_interval):
    
    # motor_array = ['m1','m2']
    
    motor = len(motor_array)
    le = len(a)
    
    g = int(le/motor)
    last_iter = le%motor

    print(g)

    async def run_watering(w):
        t = []
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        t.append(current_time)
    
        print("Current Time =", current_time)
        print(f'starte{w}')
        await asyncio.sleep(motor_run_time)
        print(f'ended{w}')
        now2 = datetime.now()

        current_time2 = now2.strftime("%H:%M:%S")
    
        t.append(current_time2)
        return t

    async def main():
        
        global index
        value = []
        func_motor = motor
        b = 1
        for i in range(0,le,func_motor):
            z = i
            for j in range(func_motor):
            
                task = asyncio.create_task(run_watering(a[z]))
            
                z = z+1
            value = await task
            print(value)
            mo = 0
            for d in range(i,i+func_motor):

                try:
                    await Irigation.objects.acreate(index=index,plot=a[d],startTime = value[0],endTime=value[1],Runby = motor_array[mo] )
                    mo = mo+1
                    index = index +1
                except Exception as e:
                    print(e,'welcome')
            if b == g:
                func_motor = last_iter
        
            b = b + 1
    
        await asyncio.sleep(irigation_cycle_interval)
        await main()





    asyncio.run(main()) 
            
            
    return True