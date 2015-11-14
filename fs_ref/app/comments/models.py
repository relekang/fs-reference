# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import date
from fs_ref.app.references.models import Reference


class ReferenceComment(models.Model):
    reference = models.ForeignKey(Reference, related_name='comments')
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(editable=False)
    content = models.TextField()

    class Meta:
        ordering = ('-timestamp',)

    def save(self, *args, **kwargs):
        self.timestamp = datetime.now()
        super(ReferenceComment, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s: %s..." % (self.user.username, self.content[:100])

    def to_dict(self):
        return {
            'reference_id': self.reference.id,
            'user': "%s %s" % (self.user.first_name, self.user.last_name),
            'timestamp': date(self.timestamp, arg='d.m.y H.i'),
            'content': self.content,
        }
