from django.db import models

from datetime import date

class Temple (models.Model):
    name = models.CharField (max_length=100)
    desc = models.CharField (max_length=1000)

    # Date the task was modified.
    modified_on = models.DateField(default=date.today)

    class Meta:
        # Set the table name.
        db_table = 'temple'

    def __str__ (self):
        return self.name
