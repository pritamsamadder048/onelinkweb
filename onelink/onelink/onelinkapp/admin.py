from django.contrib import admin

from .models import UserDetail
from .models import UserSession
from .models import UserVerificationSession
from .models import ServiceCategory
from .models import ServiceSubCategory
from .models import ServiceMap
from .models import ItemMap
from .models import ServiceRequest
from .models import ServiceNotification
from .models import FavouriteService
from .models import ProductCategory


from .models import Stock
admin.site.register(Stock)


admin.site.register(UserDetail)
admin.site.register(UserSession)
admin.site.register(UserVerificationSession)
admin.site.register(ServiceCategory)
admin.site.register(ServiceSubCategory)
admin.site.register(ServiceMap)
admin.site.register(ItemMap)
admin.site.register(ServiceRequest)
admin.site.register(ServiceNotification)
admin.site.register(FavouriteService)
admin.site.register(ProductCategory)
