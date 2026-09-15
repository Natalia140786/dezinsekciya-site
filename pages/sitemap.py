from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return ['home', 'contacts', 'about', 'faq']

    def location(self, item):
        return reverse(item)