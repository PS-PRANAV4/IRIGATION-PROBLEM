from django.shortcuts import render


from rest_framework.views import APIView,Response

from logics.task import add
from .models import Plan,PlanSerializer,Irigation,IrigationSerializer



class GetScrapedData(APIView):
    # url = 'https://www.airtel.in/myplan-infinity/'
    def post(self,request):
        data = request.data
        plotArray = data['plotarray']
        motorArray = data['motor']
        # irigation_start_time = data['irigation s']
        motor_run_time = data['motor_run_time']
        irigation_cycle_interval = data['irigation_cycle']
        try:
            add.delay(plotArray,motorArray,motor_run_time,irigation_cycle_interval)
        except:
            pass
        return Response({"status":"success"},status=200) 
   
class GetData(APIView):

    def get(self,request):
        try:
            data = Plan.objects.all()[:4]
        except:
            Response({},status=400)
        
        plan = PlanSerializer(data, many = True)
        return Response(plan.data,status=200)

class GetDataIrigation(APIView):
    def get(self,request):
        try:

            irigation_data =  Irigation.objects.all()
            serializer = IrigationSerializer(irigation_data,many = True)
            return Response(serializer.data,status = 400)
        except:
            return Response({},status = 404)

