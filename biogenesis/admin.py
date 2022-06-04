from django.contrib import admin
from .models import Vid, Entity, Reviews, Family, Book #User
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class EntityAdminForm(forms.ModelForm):
    description = forms.CharField(label = "Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Entity
        fields = '__all__'

@admin.register(Vid)
class VidAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)

class ReviewInline(admin.StackedInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")

# class UserInline(admin.StackedInline):
#     model = User
#     #readonly_fields = ("username")

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('title', 'vid', 'family', 'url', 'draft', 'user')
    list_filter = ('vid', 'family')
    search_fields = ('title', 'vid__name')
    inlines = [ReviewInline]#, UserInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ["publish", "unpublish"]
    form = EntityAdminForm
    readonly_fields = ("get_image",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)



    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="80" height="70"')

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
            """Опубликовать"""
            row_update = queryset.update(draft=False)
            if row_update == 1:
                message_bit = "1 запись была обновлена"
            else:
                message_bit = f"{row_update} записей были обновлены"
            self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Изображение"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'entity')
    readonly_fields = ('name', 'email')
    list_display_links = ('name',)


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.site_title = "Django Biogenesis"
admin.site.site_header = "Django Biogenesis"

