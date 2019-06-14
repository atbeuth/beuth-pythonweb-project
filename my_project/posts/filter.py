from django import django_filters

class frontFilter(django_filters.FilterSet):
    postID = django_filters.IFilter(lookup_expr='postid')
    tags = django_filters.NumberFilter(field_name='tags')
    content = django_filters.CharFilter(lookup_expr='icontains')
    upvotes = django_filters.NumberFilter(field_name='upvotes')
    downvotes = django_filters.NumberFilter(field_name='downvotes')

    class Meta:
        model = filter
        fields = {
            'postid': ['exact'],
            'tags': ['tags'], 
            'content': ['content'], 
            'upvotes': ['upvotes'], 
            'downvotes': ['downvotes'],
        }

class ArticleFilter(django_filters.FilterSet):

    class Meta:
        model = filter
        fields = [...]

    @property
    def qs(self):
        parent = super(ArticleFilter, self).qs
        postID = getattr(self.request, 'postID', None)

        return parent.filter(is_published=True) \
            | parent.filter(postID=postID)

    