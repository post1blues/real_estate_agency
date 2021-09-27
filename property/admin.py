from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = (OwnerInline,)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('full_name', 'owners_phonenumber', 'owner_pure_phone')


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Complaint, ComplaintAdmin)
