from api.serializers import TasksSerializer
from webapp.models import Task
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class TasktView(APIView):

    def get(self, request, pk):
        object = Task.objects.filter(id=pk)
        if not object.all().first():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TasksSerializer(object, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        object = Task.objects.get(id=pk)
        if not object:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TasksSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        object = Task.objects.get(id=pk)
        if not object:
            return Response(status=status.HTTP_404_NOT_FOUND)
        object.delete()
        return Response({'id': pk}, status=status.HTTP_204_NO_CONTENT)
