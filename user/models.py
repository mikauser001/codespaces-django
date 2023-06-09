from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Fügen Sie hier weitere benutzerdefinierte Felder hinzu, wenn erforderlich
    points = models.IntegerField()
    rank = models.IntegerField()
    is_mod = models.BooleanField(default=False)

    def reset(self):
        self.points, self.rank = None * 2 
        self.save(update_fields=["points", "rank"])
