from rest_framework import status, generics, serializers

from pages.models import Frame


class FrameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Frame


class FrameList(generics.ListAPIView):
	queryset = Frame.objects.all()
	serializer_class = FrameSerializer