from django.shortcuts import render


import requests
from django.shortcuts import render

def get_data_from_other_blog(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def blog_data_view(request):
    api_url = 'https://krishnaastute.pythonanywhere.com/api/blogposts/'
    blog_data = get_data_from_other_blog(api_url)
    
    return render(request, 'blog_template.html', {'data': blog_data})
