# Importing necessary modules from Django
from django.db import models


# Defining a Django model named UniversityCampus
class UniversityCampus(models.Model):
    # Define a field for the campus name, a CharField with max length of 20 characters
    Campus_name = models.CharField(max_length=20)
    # Define a field for the state, a CharField with max length of 2 characters
    State = models.CharField(max_length=2)
    # Define a field for the campus ID, an IntegerField
    Campus_Id = models.IntegerField

    # Define a string representation for instances of the model
    def __str__(self):
        # Return the campus name when the instance is converted to a string
        return self.Campus_name

    # Define meta options for the model
    class Meta:
        # Set a custom verbose name for the model in the admin interface
        verbose_name_plural = "University Campus"
