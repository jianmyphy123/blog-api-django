from rest_framework.serializers import ModelSerializer

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

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish'
        ]

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'slug',
            'content',
            'publish'
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
