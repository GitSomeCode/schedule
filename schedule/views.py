from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View, FormView
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, Http404, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from schedule.models import Meeting
from schedule.forms import MeetingForm

# Create your views here.
class allMeetings(ListView):
  model = Meeting
  template_name = "schedule/all.html"
  paginate_by = '10'
  context_object_name = "meetings"

class addMeeting(FormView):
  pass