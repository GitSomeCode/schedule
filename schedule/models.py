from django.db import models

# Create your models here.
class Meeting(models.Model):
  priority_levels = (
    (1, 'Important'),
    (2, 'Standard'),
    (3, 'Casual'),
  )
  company = models.CharField(max_length = 30, default = "", blank = True)
  person = models.CharField(max_length = 30, default = "", blank = False)
  date = models.DateTimeField(auto_now = False)
  location = models.CharField(max_length = 100, default = "", blank = False)
  ended = models.BooleanField(default = True, blank = False)
  
  