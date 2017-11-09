from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish'
        ]

post_detail_url = HyperlinkedIdentityField(
    view_name="posts-api:detail",
    lookup_field='slug'
)
class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]


"""

data = {
    "title": "Yeahh buddy",
    "content": "New Content",
    "publish": "2016-2-12",
    "sulg": "yeah-buddy"
}

new_item = PostSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else
    print(new_item.errors)

"""
