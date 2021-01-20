from django.shortcuts import render

def post_list(request) :
    return render(request, 'jaewooblog/post_list.html',{})