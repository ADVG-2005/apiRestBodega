from rest_framework.viewsets import ModelViewSet
#from rest_framework.response import Response
#from rest_framework import status
from apps.registro.models import Materiales
from apps.registro.api.serializer import RegistroSerializer
#from rest_framework.permissions import IsAuthenticated
from apps.registro.api.permissions import IsAdminOrReadOnly

class ViewSetRegistro(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class= RegistroSerializer
    queryset = Materiales.objects.all()
    #http_method_names = ['GET','PUT']

    #def list(self,request):
    #    serializer = RegistroSerializer(Materiales.objects.all(),many=True)
    #    return Response(status=status.HTTP_200_OK,data=serializer.data)
    #
    #def retrieve(self,request,pk=int):
    #        serializer = RegistroSerializer(Materiales.objects.get(pk=pk))
    #        return Response(status=status.HTTP_200_OK,data=serializer.data)
    #    
    #def update(self,request,pk=int):
    #    try:
    #        serializer = Materiales.objects.get(pk=pk)
    #        serializer= RegistroSerializer(serializer,data=request.data)
    #        serializer.is_valid()
    #        serializer.save()
    #        return Response(status=status.HTTP_200_OK,data=serializer.data)
    #    except Materiales.DoesNotExist:
    #        return Response(status=status.HTTP_404_NOT_FOUND,data={"registro no encontrado"})
    #    
    #def partial_update(self,request,pk=int):
    #    try:
    #        serializer = Materiales.objects.get(pk=pk)
    #        serializer= RegistroSerializer(serializer,data=request.data, partial=True)
    #        serializer.is_valid()
    #        serializer.save()
    #        return Response(status=status.HTTP_200_OK,data=serializer.data)
    #    except Materiales.DoesNotExist:
    #        return Response(status=status.HTTP_404_NOT_FOUND,data={"registro no encontrado"})
    #    
    #def destroy(self,request,pk):
    #    serializer=Materiales.objects.get(pk=pk)
    #    serializer.delete()
    #    serializer.save()
    #    return Response(status=status.HTTP_200_OK,data={"Eliminado exitoso"})
#
    #def create(self,request):
    #    serializer=RegistroSerializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    serializer.save()
    #    return Response(status=status.HTTP_200_OK,data=serializer.data)