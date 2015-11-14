# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from fs_ref.app.references.models import Reference


class RssFeed(Feed):
    title = "Lekang gruppens referanser"
    link = "/rss/"
    #    description = "Updates on changes and additions to chicagocrime.org."
    filter = None

    def items(self):
        if self.filter:
            return Reference.objects.filter(self.filter, is_approved=True, is_published=True).order_by('-date_created')
        else:
            return Reference.objects.filter(is_approved=True, is_published=True).order_by('-date_created')

    def item_link(self, item):
        return reverse('view_reference', args=[item.id])
