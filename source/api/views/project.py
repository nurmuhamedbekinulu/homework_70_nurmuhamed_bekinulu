from api.serializers import ProjectsSerializer
from webapp.models import Project
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ProjectView(APIView):

    def get(self, request, pk):
        object = Project.objects.filter(id=pk)
        if not object.all().first():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectsSerializer(object, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
