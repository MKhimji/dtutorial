from home.models import BlogPost
from datetime import date

def blogposts_processor(request):
    blogposts = BlogPost.objects.all()
    q=blogposts.dates('date', 'month')
    s = [(i.strftime('%b'),i.strftime('%Y')) for i in q]

    return {'blogposts': blogposts,'s':s, 'q':q} 
