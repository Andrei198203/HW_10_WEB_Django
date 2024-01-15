from django.db import models
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1_000_000:
        raise ValidationError('Maximum size of file is 1Mb')
    return value

# Create your models here.


class Picture(models.Model):
    description = models.CharField(max_length=300)
    path = models.ImageField(upload_to='images', validators=[validate_file_size])


