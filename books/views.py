#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list_books(request):
	"""
	List the books that have reviews
	"""
	return render(request, "list.html")
	#return HttpResponse("Hello, {}!".format(request.user.username))

