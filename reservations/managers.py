from django.db import models

class CustomReservationManager(models.Manager):

    def get_or_not(sefl, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None