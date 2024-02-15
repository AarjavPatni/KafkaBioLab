from django.db import models
from uuid import uuid4


# Create your models here.
class Sequence(models.model):
    input_sequence = models.CharField(max_length=10000)
    operation = (
        models.integerField()
    )  # 1 - reverse, 2 - complement, 3 - reverse complement
    output_sequence = models.CharField(max_length=10000)
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
