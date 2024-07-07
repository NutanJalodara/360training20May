from django.contrib import admin
from .models import p_name
from .models import p_id
from .models import p_contact
from .models import p_address

# Register your models here.
admin.site.register(p_name)
admin.site.register(p_id)
admin.site.register(p_contact)
admin.site.register(p_address)