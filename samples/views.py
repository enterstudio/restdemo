from rest_framework import viewsets

from samples.serializers import SampleSerializer, AssaySerializer
from samples.models import Sample, Assay


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class AssayViewSet(viewsets.ModelViewSet):
    queryset = Assay.objects.all()
    serializer_class = AssaySerializer

