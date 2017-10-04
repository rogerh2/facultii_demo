from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from time import sleep

class HomePageView(TemplateView):
    template_name = 'index.html'


class MembersPageView(TemplateView):
    template_name = 'members.html'


class LabMembersPageView(TemplateView):
    template_name = 'emailmembers.html'


class UnreadIcon(TemplateView):
    template_name = 'unreadicon.html'


    def post(self, request):
        number = int(request.POST.get('number'))
        template = loader.get_template(self.template_name)
        if number < 1005:
            number += 1
            sequence_isgoing = True
            sleep(0.0025)
        else:
            number += 1347
            sequence_isgoing = True
            sleep(0.0025)

        context = {
            'sequence_isgoing' : sequence_isgoing,
            'number' : number,
        }
        template.render(context, request)
        return HttpResponse(template.render(context, request))