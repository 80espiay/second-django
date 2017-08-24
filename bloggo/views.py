from django.shortcuts import render

def post_list(request):
    return render(request, 'bloggo/post_list.html', {})