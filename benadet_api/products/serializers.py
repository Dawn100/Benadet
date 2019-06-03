from rest_framework import serializersfrom .models import *class ProductPhotoSerializer(serializers.HyperlinkedModelSerializer):    class Meta:        model = ProductPhoto        fields = (            'url',            'product_photo_id',            'product',            'photo'        )class ProductSerializer(serializers.HyperlinkedModelSerializer):    photos = serializers.HyperlinkedRelatedField(        many=True,        read_only=True,        view_name='productphoto-detail'    )    class Meta:        model = Product        fields = (            'product_id',            'name',            'categories',            'photos',            'regular_price',            'discounted_price',            'description',            'stock',            'taxable',            'product_status',            'tags'        )class CategorySerializer(serializers.HyperlinkedModelSerializer):    class Meta:        model = Category        fields = (            'category_id',            'name',            'description',            'parent',            'image'        )class ProductStatusSerializer(serializers.HyperlinkedModelSerializer):    class Meta:        model = ProductStatus        fields = (            'product_status_id',            'status_name'        )class TagSerializer(serializers.HyperlinkedModelSerializer):    class Meta:        model = Tag        fields = (            'url',            'tag_id',            'tag_name'        )