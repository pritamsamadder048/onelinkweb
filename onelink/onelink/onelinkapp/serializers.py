from rest_framework import serializers


from  .models import UserDetail
from .models import UserSession
from .models import Stock
from .models import ServiceCategory
from .models import ProductCategory
from .models import ServiceSubCategory
from  .models import ServiceMap
from .models import ItemMap
from .models import ServiceRequest
from .models import ServiceNotification





class StockSerializer(serializers.ModelSerializer):


    class Meta:
        model=Stock
        fields='__all__'






#User Detail serializer
class UserDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model=UserDetail
        fields=("id","full_name","email","mobile","pincode","country","city","district","building","street","user_type")



class ServiceCategorySerializer(serializers.ModelSerializer):


    class Meta:
        model=ServiceCategory
        fields=('id','service_name','service_detail','service_image')




class ProductCategorySerializer(serializers.ModelSerializer):


    class Meta:
        model=ProductCategory
        fields=('id','product_name','product_detail','product_image')




class ServiceSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSubCategory
        fields = ('id', 'sub_service_name', 'sub_service_detail', 'service_categorgy_id')


class ServiceMapSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceMap
        fields=('id','serviceprovider_id',"license_no","under_gov",'service_name',"service_details", 'serviceprovider_email','service_category_id','areapincode')


class ItemMapSerializer(serializers.Serializer):


    class Meta:
        model=ItemMap
        fields=('id','serviceprovider_id','serviceprovider_email','product_category_id','item_name','item_details','item_features','item_MRP','item_SLP','iteme_image')






class ServiceRequestSerializer(serializers.Serializer):

    class Meta:

        model=ServiceRequest
        fields=("id","serviceprovider_id","user_id","service_category_id","service_map_id","areapincode","service_request_address")







class ProviderNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceNotification
        fields="__all__"#("id","serviceprovider_id","servicerequest_id","request_time","read","notification")



#
# from .models import ServiceRequestChat
#
# class ServiceRequestChatSerializer(serializers.Serializer):
#     class Meta:
#         model=ServiceRequestChat
#         fields="__all__"



from .models import FavouriteService
class FavouriteServiceSerializer(serializers.Serializer):
    class Meta:
        model=FavouriteService
        fields="__all__"


from .models import OrderHistory
class OrderHistorySerializer(serializers.Serializer):
    class Meta:
        model=OrderHistory
        fileds="__all__"