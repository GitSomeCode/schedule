#!/usr/bin/env python
import os
import sys
import uuid
import datetime
import random
import arrow
import django

# Clear the database.
def endall():
  # Delete Meetings.
  for obj in Meeting.objects.all():
    obj.delete()
  # Delete Users.
  for obj in get_user_model().objects.all():
    obj.delete()

# Make User object.
def makeUser(n, e, p):
  try:
    usr = get_user_model().objects.get(username = n)
    return usr
  except get_user_model().DoesNotExist:
    return get_user_model().objects.create_user(username = n, email = e, password = p)

# Make a random date.
def randomDate():
  """
  This function will return a random datetime between two datetime objects.
  """
  start = arrow.now().datetime
  end = arrow.get(datetime.datetime(2015, 3, 17, 12, 0, 0))
  delta = end - start
  int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
  random_second = random.randrange(int_delta)
  d = start + datetime.timedelta(seconds=random_second)
  return arrow.get(d).datetime

# Return a random User.s
randomUser = lambda: get_user_model().objects.all()[random.randrange(0, get_user_model().objects.count())]

# Make a random Url.
randomUrl = lambda: str(uuid.uuid4())[:6]

def main():
  
  # Make Users.
  makeUser("Harry", "harry@gmail.com", "harry101")
  makeUser("Natalie", "natalie@gmail.com", "natalie101")
  makeUser("Ramin", "ramin@gmail.com", "ramin101")
  makeUser("Tyler", "tyler@gmail.com", "tyler101")
  makeUser("Bella", "bella@gmail.com", "bella101")
  makeUser("Blossom", "blossom@gmail.com", "blossom101")
  makeUser("Starbuck", "starbuck@gmail.com", "starbuck101")
  makeUser("Chewbacca", "chewbacca@gmail.com", "chewbacca101")
  makeUser("Vader", "vader@gmail.com", "vader101")
  makeUser("Obi-wan", "obiwan@gmail.com", "obiwan101")
  Drogo = get_user_model().objects.create_superuser(username = "drogo", email = "drogo@gmail.com", password = "drogo101")
  Anakin = get_user_model().objects.create_superuser(username = "anakin", email = "anakin@gmail.com", password = "anakin101")
  
  populator = Faker.getPopulator()
  populator.addEntity(Meeting, 5, {
      'user': lambda x: get_user_model().objects.get(pk = populator.generator.randomInt(0, get_user_model().objects.count()))
    })
  addElements = populator.execute()
  

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings.dev")
  django.setup()
  from schedule.models import Meeting
  from django.contrib.auth import get_user_model
  from django_faker import Faker
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()
