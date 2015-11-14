# -*- coding: utf-8 -*-
from django.contrib import admin
from fs_ref.app.comments.models import ReferenceComment


class CommentInline(admin.TabularInline):
    model = ReferenceComment
    fields = ('user', 'timestamp', 'content')
    readonly_fields = ('user', 'timestamp', 'content')
    extra = 0


admin.site.register(ReferenceComment)
