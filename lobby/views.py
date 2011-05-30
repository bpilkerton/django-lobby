import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.db.models import Count
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django import forms
from lobby.wholobbiesus.models import *

def index(request):
    return render_to_response('wholob_index.html')

def create_paginate(request,d):
    paginator = Paginator(d, 25)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        out = paginator.page(page)
    except (EmptyPage, InvalidPage):
        out = paginator.page(paginator.num_pages)

    return out

def format_lobby(request,d):
    for lob in d: 
        lob.received = lob.received[0:10]

    return d
    
def registrant_detail(request,registrant_name):
    data = Lobby.objects.filter(registrant_name__iexact=registrant_name).order_by('-received')
    data = format_lobby(request,data)
    items = create_paginate(request,data)
    return render_to_response('detail.html', {'title':'Registrant: ' + registrant_name,'items': items})    

def client_detail(request,client_name):
    data = Lobby.objects.filter(client_name__iexact=client_name).order_by('-received')
    data = format_lobby(request,data)
    items = create_paginate(request,data)
    return render_to_response('detail.html', {'title':'Client: ' + client_name,'items': items})

def issue_detail(request,issue):
    data = Lobby.objects.filter(issue__issue_code__iexact=issue).order_by('-received')
    data = format_lobby(request,data)
    items = create_paginate(request,data)
    return render_to_response('detail.html', {'title':'Issue: ' + issue,'items': items})

def issue_list(request):
    items = Issue.objects.values("issue_code").annotate(num=Count('issue_code'))
    return render_to_response('issue_list.html', {'title':'Issues ','items': items})
    
def lobbyist_detail(request,lobbyist_name):
    data = Lobby.objects.filter(lobbyist__lobbyist_name__iexact=lobbyist_name).order_by('-received')
    items = create_paginate(request,data)
    return render_to_response('detail.html', {'title':'Lobbyist: ' + lobbyist_name,'items': items})

def agency_detail(request,agency_name):
    data = Lobby.objects.filter(agency__gov_entity_name__iexact=agency_name).order_by('-received')
    data = format_lobby(request,data)
    items = create_paginate(request,data)
    return render_to_response('detail.html', {'title':'Agency: ' + agency_name,'items': items})
    
def filing(request,filing_id):
    vars = {}
    vars['filing_id'] =filing_id
    
    #Summary (there are apparently data anomolies, get first record)
    items = Lobby.objects.get(filing_id=filing_id)
    items.received = items.received[0:10]
    vars['items'] = items
    
    #Lobbyists
    lobs = Lobbyist.objects.filter(filing__exact=filing_id)
    vars['lobs'] = lobs
    
    #Issues
    issues = Issue.objects.filter(filing__exact=filing_id)
    vars['issues'] = issues
    
    #Agencies
    agencies = Agency.objects.filter(filing__exact=filing_id)
    vars['agencies'] = agencies
    
    #Foreign Entity
    foreign_entities = ForeignEntity.objects.filter(filing__exact=filing_id)
    vars['foreign_entities'] = foreign_entities
    
    #Affilliated Org
    orgs = AffiliatedOrg.objects.filter(filing__exact=filing_id)
    vars['orgs'] = orgs
    
    vars['title'] = 'Report: ' + filing_id

    return render_to_response('filing_detail.html', vars)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    qtype = forms.CharField(max_length=10)
    date_a = forms.CharField(required=False)
    date_b = forms.CharField(required=False)    

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            qtype = form.cleaned_data['qtype']
            date_a = form.cleaned_data['date_a']
            date_b = form.cleaned_data['date_b']
                
            if qtype == 'Client':
                items = Lobby.objects.values("client_name").filter(client_name__icontains=query).annotate(num=Count('client_name')).order_by();
            elif qtype == 'Registrant':
                items = Lobby.objects.values("registrant_name").filter(registrant_name__icontains=query).annotate(num=Count('registrant_name')).order_by();
            elif qtype == 'Lobbyist':
                items = Lobbyist.objects.values("lobbyist_name").filter(lobbyist_name__icontains=query).annotate(num=Count('lobbyist_name')).order_by();
            elif qtype == 'Date':
                items = Lobby.objects.filter(received__gte=date_a).filter(received__lte=date_b)
                return render_to_response('search_by_date.html', {'date_a':date_a,'date_b':date_b,'items': items,'qtype':qtype})

            if items.count() > 0:
                return render_to_response('search_detail.html', {'query':query,'items': items,'qtype':qtype})
            else:
                return render_to_response('search_detail.html', {'query':query,'nodata':'yes','qtype':qtype})

    else:
        url = '/'
        return HttpResponseRedirect(url) # Redirect after POST

    return render_to_response('wholob_index.html', {'form': form,'title':'Home'})

def about(request):
    return render_to_response('about.html',{'title':'About'})
    
def filing_xml(request,filing_id):
    response = HttpResponse()
    response['Content-type'] = 'text/xml'
    response.content = '<?xml version="1.0" encoding="UTF-8"?><response>Not implemented, yet</response>'
    return response
