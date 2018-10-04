from django.http import HttpResponse

def here(request):
	return HttpResponse('Here is main website')
