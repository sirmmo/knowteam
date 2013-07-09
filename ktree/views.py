# Create your views here.
def kg(request):
	parent = request.REQUEST.get('parent')

	if parent is None:
