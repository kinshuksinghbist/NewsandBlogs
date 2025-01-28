from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .serializers import BlogSerializer
from .forms import BlogForm

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogStandardView(generics.ListAPIView):
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return render(self.request, 'blogs/blog_list.html', {'data': serializer.data})



def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blogs')
    else:
        form = BlogForm()

    return render(request, 'blogs/blog_form.html', {'form': form})


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
    return render(request, 'blogs/blog_confirm_delete.html', {'blog': blog})
