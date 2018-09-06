from django.contrib.sitemaps import Sitemap
#from django.core.urlresolvers import reverse
from django.urls import reverse

# class BlogSitemap(Sitemap):
#     changefreq = "daily"
#     priority = 0.5


#     def items(self):
#         return Post.objects.all()



class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
        'home',
        ]

    def location(self, item):
        return reverse(item)