# coding=utf-8
import uuid
from django.db import models


class Questionnaire(models.Model):
    """Model for questionnaire"""

    question = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    unique_id = models.CharField(
        max_length=100,
        default=uuid.uuid4().hex[:8],
        editable=False,
        unique=True
    )

    answers = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['question']

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Questionnaire, self).save(*args, **kwargs)
            id = str(self.unique_id) + str(self.pk)
            self.unique_id = id
            self.save()
        else:
            super(Questionnaire, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'{}'.format(self.question)
