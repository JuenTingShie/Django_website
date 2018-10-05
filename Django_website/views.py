from django.http import HttpResponse
from django.shortcuts import render_to_response

def main(request):
	return HttpResponse('Here is main website')
def math(request,a,b):
	s = a+b
	d = a-b
	p = a*b
	q = a/b
	return render_to_response('math.html',locals())
def history(request):
	return render_to_response('history.html')
