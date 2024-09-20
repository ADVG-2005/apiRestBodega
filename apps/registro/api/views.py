from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.registro.models import Materiales
from apps.registro.api.serializer import RegistroSerializer


class ViewRegistro(APIView):
    def get(self,request):
        serializer= RegistroSerializer(Materiales.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    def post(self,request):
        serializer=RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK,data=serializer.data)