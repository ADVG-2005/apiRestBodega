from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import Salida
from apps.salida.api.serializer import SalidaSerializer


class SalidaViewSet(ViewSet):
    def list(self,request):
        serializer= SalidaSerializer(Salida.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    
    def retrieve(self,request,pk=int):
        serializer = SalidaSerializer(Salida.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK,data=serializer.data)

    def update(self,request,pk=int):
        try:
            modelo=Salida.objects.get(pk=pk)
            serializer=SalidaSerializer(modelo,data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Salida.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data={"registro no encontrado"})

    def partial_update(self,request,pk=int):
        try:
            modelo=Salida.objects.get(pk=pk)
            serializer=SalidaSerializer(modelo,data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Salida.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data={"registro no encontrado"})

    def destroy(self,request,pk):
        serializer=Salida.objects.get(pk=pk)
        serializer.delete()
        serializer.save()
        return Response(status=status.HTTP_200_OK,data={"Eliminado exitoso"})
    
    def create(self,request):
        serializer=SalidaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK,data=serializer.data)