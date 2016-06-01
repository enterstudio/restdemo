from django.db import models

class Sample(models.Model):
    
    sample_id = models.CharField(max_length=255, unique=True)
    sample_name = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return '%s: %s' % (self.sample_id, self.sample_name)

class Assay(models.Model):

    assay_id = models.CharField(max_length=255, unique=True)
    assay_name = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000, null=True)
    sample = models.ForeignKey(Sample)

    def __str__(self):
        return '%s: %s' % (self.assay_id, self.assay_name)
