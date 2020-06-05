from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Job(models.Model):

    class JobStatus(models.TextChoices):
        DRAFT = 'DR', _('Draft')
        PUBLISHED = 'PU', _('Published')
        CLOSED = 'CL', _('Closed')

    class EmploymentType(models.TextChoices):
        FULL_TIME = 'FT', _('Full Time')
        PART_TIME = 'PT', _('Pull Time')

    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='jobs')
    job_status = models.CharField(max_length=2,
                                  choices=JobStatus.choices,
                                  default=JobStatus.DRAFT)
    employment_type = models.CharField(max_length=2,
                                       choices=EmploymentType.choices,
                                       default=EmploymentType.FULL_TIME)                               
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
