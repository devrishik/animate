from rest_framework import status, generics, serializers

from pages.models import Frame


class FrameSerializer(serializers.ModelSerializer):
	image_link = serializers.Field(source='cover_image.url')
	video_link = serializers.Field(source='video.url')

	class Meta:
		model = Frame
		fields = ('id', 'name', 'appStoreLink', 'description', 'image_link', 'video_link')



class FrameList(generics.ListAPIView):
	queryset = Frame.objects.all()
	serializer_class = FrameSerializer
