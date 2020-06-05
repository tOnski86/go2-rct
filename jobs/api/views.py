from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from jobs.models import Job
from jobs.api.serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)