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
from .models import ItemNotification
from .models import FavouriteService
from .models import ProductCategory
from .models import OrderHistory
from .models import ItemOrderHistory
from .models import ItemRequest
from .models import RequestMessage
from .models import Review



# from .models import Stock
# admin.site.register(Stock)






class UserAdmin(admin.ModelAdmin):
    
    list_display=('id','full_name', 'email', 'mobile' )

    search_fields = ('id','full_name', 'email', 'mobile' )
admin.site.register(UserDetail,UserAdmin)


class UserSessionAdmin(admin.ModelAdmin):
    
    list_display=("UserDetail_id",'full_name', 'email', 'mobile' )
    search_fields = ('UserDetail_id','full_name', 'email', 'mobile' )
admin.site.register(UserSession,UserSessionAdmin)

admin.site.register(UserVerificationSession)

class ServiceCategoryAdmin(admin.ModelAdmin):
    
    list_display=('id','service_name' )
    search_fields = ('id','service_name' )
admin.site.register(ServiceCategory,ServiceCategoryAdmin)


admin.site.register(ServiceSubCategory)

class ProductCategoryAdmin(admin.ModelAdmin):
    
    list_display=('id','product_name' )
    search_fields = ('id','product_name' )
admin.site.register(ProductCategory,ProductCategoryAdmin)

class ServiceMapAdmin(admin.ModelAdmin):
    
    list_display=('id','serviceprovider_id','service_name','license_no','under_gov','serviceprovider_email','mobile','service_category_id','areapincode','ratings' )
    search_fields = ('id','serviceprovider_id','service_name','license_no','under_gov','serviceprovider_email','mobile','service_category_id','areapincode','ratings' )
admin.site.register(ServiceMap,ServiceMapAdmin)

class ItemMapAdmin(admin.ModelAdmin):
    
    list_display=('id','serviceprovider_id','item_name','product_category_id','item_MRP','serviceprovider_email','mobile','item_SLP','ratings' )
    search_fields = ('id','serviceprovider_id','item_name','product_category_id','item_MRP','serviceprovider_email','mobile','item_SLP','ratings' )
admin.site.register(ItemMap,ItemMapAdmin)

class ServiceRequestAdmin(admin.ModelAdmin):
    
    list_display=('id','serviceprovider_id','user_id','service_map_id','areapincode','request_type' )
    search_fields = ('id','serviceprovider_id','service_map_id','areapincode' )
admin.site.register(ServiceRequest,ServiceRequestAdmin)

class ItemRequestAdmin(admin.ModelAdmin):
    
    list_display=('id','serviceprovider_id','user_id','item_map_id','areapincode','request_type' )
    search_fields = ('id','serviceprovider_id','item_map_id','areapincode' )
admin.site.register(ItemRequest)


# admin.site.register(ServiceNotification)
# admin.site.register(ItemNotification)
admin.site.register(FavouriteService)


class OrderHistoryAdmin(admin.ModelAdmin):
    
    list_display=('id','confirmation_id','serviceprovider_id','user_id','service_map_id','service_request_id','service_status' )
    search_fields = ('id','confirmation_id','serviceprovider_id','user_id','service_map_id','service_request_id' )
admin.site.register(OrderHistory,OrderHistoryAdmin)

class ItemOrderHistoryAdmin(admin.ModelAdmin):
    
    list_display=('id','confirmation_id','serviceprovider_id','user_id','item_map_id','item_request_id','item_status' )
    search_fields = ('id','confirmation_id','serviceprovider_id','user_id','item_map_id','item_request_id' )
admin.site.register(ItemOrderHistory,ItemOrderHistoryAdmin)

admin.site.register(RequestMessage)
admin.site.register(Review)


