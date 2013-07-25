
import json

from ktree.models import *

from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response

def kg_page(request):
	return render_to_response('kg.html')

def kg(request):
	parent = request.REQUEST.get('p', "-1")
	parent = int(parent)
	known_ids = request.REQUEST.get('k', "[]")
	known_ids = json.loads(known_ids)

	ret = {
		'nodes':[], 
		'links':[]
		}

	if parent < 0:
		ret['nodes'] = list(Term.objects.filter(accepted=True, primary = True).order_by('id').distinct().values())
	else:
		ret['nodes'] = list(Term.objects.filter(accepted=True).order_by('id').filter(Q(starts__b__id=parent)|Q(ends__a__id=parent)).distinct().values())

	known_ids.extend([x['id'] for x in ret['nodes']])
	ids = known_ids


	
	ret['links'] = list(Link.objects.filter(Q(a__in=ids),Q(b__in=ids)).distinct().values('name__name', 'a__id', 'b__id', 'id'))

	for x in ret['links']:
		x['source'] = x['a__id']
		x['target'] = x['b__id']
		x['value'] = x['name__name']
		x['weight'] = 1
	return HttpResponse(json.dumps(ret))

def add_term(request):
	name=request.REQUEST.get('n')
	primary = request.REQUEST.get('p') is not None
	accepted = request.REQUEST.get('a') is not None

