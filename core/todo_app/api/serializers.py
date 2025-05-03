from todo_app.models import AddTodo
from rest_framework import serializers


class TodoTaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField("get_abs_url")

    class Meta:
        model = AddTodo
        fields = ['id','user', 'task', 'is_done', 'absolute_url']
    

    def to_representation(self, instance):
        rep= super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context["kwargs"].get("pk"):
            rep.pop('absolute_url')

        rep['user'] = instance.user.email
        return rep

    # Include the URL in the response
    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)