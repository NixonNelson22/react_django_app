from rest_framework.views import APIView
from rest_framework.response import Response
from .models import tasks
from .serializer import taskSerializer

# Create your views here.


class tasksView(APIView):
    serializer_class = taskSerializer

    def get(self, request):
        description = [
            {"task_name": obj.task_name, "task_description": obj.task_description}
            for obj in tasks.objects.all()
        ]
        return Response(description)

    def post(self, request):
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
