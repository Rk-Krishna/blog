from django.shortcuts import render
import requests

def get_data_from_other_blog(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # Returns the JSON data (a list of blog posts, typically)
    else:
        return None

def blog_data_view(request, title):
    api_url = 'https://krishnaastute.pythonanywhere.com/api/blogposts/'
    blog_data = get_data_from_other_blog(api_url)

    # If blog_data is not None and is a list of blog posts, filter the data based on the title
    if blog_data:
        # Assuming each item in the blog_data is a dictionary with a 'title' key
        blog_post = next((item for item in blog_data if item.get('title') == title), None)

        # If a blog post with the matching title is found, pass it to the template
        if blog_post:
            return render(request, 'blog_template.html', {'data': blog_post})
        else:
            # Handle case where the title is not found
            return render(request, 'blog_template.html', {'error': 'Blog post not found'})
    else:
        return render(request, 'blog_template.html', {'error': 'Failed to retrieve blog data'})
