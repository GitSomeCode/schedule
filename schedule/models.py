from django.db import models
from django.conf import settings

# Create your models here.
class Meeting(models.Model):
  """
  A model to represent a scheduled meeting.
  Required information to create an Meeting is:
  
  *) Who (Person you are meeting).
  *) When (The date the meeting would take place).
  *) Where (The location the meeting is scheduled to take place).
  """
  PRIORITY_LEVELS = (
    (1, 'Important'),
    (2, 'Standard'),
    (3, 'Casual'),
  )
  DEFAULT_PRIORITY = PRIORITY_LEVELS[1]
  # The User that is creating the meeting.
  user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "meetings", blank = False)
  # 'Who': The person / company the User is scheduled to meet.
  person = models.CharField(max_length = 30, default = "", blank = False)
  company = models.CharField(max_length = 30, default = "", blank = True)
  # 'When': The date / time the meeting is scheduled to begin.
  date = models.DateTimeField(auto_now = False, blank = False)
  # 'Where': The location of the scheduled meeting.
  location = models.CharField(max_length = 100, default = "", blank = False)
  # 
  ended = models.BooleanField(default = True, blank = False)
  priority = models.CharField(max_length = 1, choices = PRIORITY_LEVELS, default = DEFAULT_PRIORITY, blank = False)
  
  def __unicode__(self):
    return "%s : %s" %(self.person, self.date.strftime("%m/%d/%Y, %I:%M %p"))
