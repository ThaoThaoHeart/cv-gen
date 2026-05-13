from django.shortcuts import render

def save_profile(request):
	return render(request, 'myapp/accept.html')