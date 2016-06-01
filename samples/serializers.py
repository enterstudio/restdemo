from .models import Sample, Assay
from rest_framework import serializers


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = ('url', 'sample_id', 'sample_name', 'notes')


class AssaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assay
        fields = ('url', 'assay_id', 'assay_name', 'sample', 'notes')
