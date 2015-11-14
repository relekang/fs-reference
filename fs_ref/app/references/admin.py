from django.contrib import admin
from fs_ref.app.comments.admin import CommentInline
from fs_ref.app.references.models import (Customer, FilterSolution, Manufacturer, Market, Reference,
                                          Type)


class ReferenceAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Manufacturer)
admin.site.register(Customer)

admin.site.register(Market)
admin.site.register(Type)
admin.site.register(FilterSolution)
