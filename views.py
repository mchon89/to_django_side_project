# returning corresponding htmls by different visuals


from django.shortcuts import render


def home(request):
	return render(request, 'georgetown_domains/home.html')

def python3_default(request):
	return render(request, 'georgetown_domains/python3.html')

def python3(request,number):
	return render(request, 'georgetown_domains/bokeh_{}.html'.format(number))

def tableau_default(request):
	return render(request, 'georgetown_domains/tableau.html')

def tableau(request,number):
	return render(request, 'georgetown_domains/tableau_{}.html'.format(number))

def ggplot2(request):
	return render(request, 'georgetown_domains/ggplot2.html')

def network_default(request):
	return render(request, 'georgetown_domains/network.html')

def network(request,number):
	return render(request, 'georgetown_domains/network_{}.html'.format(number))

def plotly_default(request):
	return render(request, 'georgetown_domains/plotly.html')

def plotly(request,number):
	return render(request, 'georgetown_domains/plotly_{}.html'.format(number))

def leaflet_default(request):
	return render(request, 'georgetown_domains/leaflet.html')

def leaflet(request,number):
	return render(request, 'georgetown_domains/leaflet_{}.html'.format(number))

def wordcloud(request):
	return render(request, 'georgetown_domains/wordcloud.html')

def takehome_default(request):
	return render(request, 'georgetown_domains/takehome.html')

def takehome(request,number):
	return render(request, 'georgetown_domains/takehome_{}.html'.format(number))

