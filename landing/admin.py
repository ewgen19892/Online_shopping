from django.contrib import admin
# from landing.models import MenuItem, Menu
#
#
# class MenuItemInline(admin.TabularInline):
#     model = MenuItem
#     extra = 0
#
# class MenuAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Menu._meta.fields]
#     inlines = [MenuItemInline]
#
#     class Meta:
#         model = Menu
#
# admin.site.register(Menu, MenuAdmin)
#
#
# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in MenuItem._meta.fields]
#
#     class Meta:
#         model = MenuItem
#
# admin.site.register(MenuItem, MenuItemAdmin)