import django_tables2 as tables
from django.utils.html import format_html
from .models import Document
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.utils.html import escape


class ImageColumn2(tables.Column):
    def render(self, value):
        return format_html('<img src="/media/img/{}.jpg" />', value)




class ImageColumn(tables.Column):
     def render(self, value):
         return mark_safe('<img src="/media/img/%s.jpg" />'
                          % escape(value))





class DocumentTable(tables.Table):
    delete = tables.LinkColumn('main:delete_item', args=[A('pk')], attrs={'a': {'class': 'btn'}

                                                                          })
    docurl = tables.TemplateColumn('<img src="{{record.docurl}}"> ')
#    attachment = tables.TemplateColumn('<img src="{{record.attachment}}"> ')

#    docurl = ImageColumn()
    class Meta:
        model = Document
