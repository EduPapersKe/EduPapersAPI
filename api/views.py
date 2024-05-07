from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import Resource
from .serializers import ResourceSerializer


#pylint: disable=no-member
def format_file_size(file_size_bytes):
    if file_size_bytes < 1024:
        return f"{file_size_bytes} B"
    elif file_size_bytes < 1024 * 1024:
        return f"{file_size_bytes / 1024:.1f} KB"
    elif file_size_bytes < 1024 * 1024 * 1024:
        return f"{file_size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{file_size_bytes / (1024 * 1024 * 1024):.1f} GB"
        
        
class ResourceView(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]
    
    @action(methods=['GET'], detail=False)
    def get(self, request):
        queryset = self.get_queryset()
        serializer = ResourceSerializer(queryset, many=True)
        return Response(serializer.data)
        
        
    @action(methods=['GET'], detail=True)
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @action(methods=['POST'], detail=False)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = request.FILES.get('file')
        max_size = 100 * 1024 * 1024  # Sets the max size to 100MB
        allowed_formats = ['PDF', 'DOCX', 'XLSX', 'CSV', 'ODS', 'ZIP', 'TXT', 'EPUB', 'MOBI', 'AZW']

        if file.size > max_size:
            raise ValidationError({'error': 'File size exceeds the maximum allowed size.'})

        file_format = file.name.split('.')[-1].upper()
        if file_format not in allowed_formats:
            raise ValidationError({'error': 'Invalid file format.'})

        self.perform_create(serializer)

        resource = serializer.instance
        resource.publisher = self.request.user
        resource.file_size = file.size
        resource.file_format = file_format
        resource.save()

        resource.readable_size = format_file_size(file.size)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    @action(methods=['PUT'], detail=True)
    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        resource = serializer.instance
        resource.publisher = self.request.user
        resource.save()

        file = request.FILES.get('file', None)
        if file:
            return Response({'error': 'File update is not allowed.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @action(methods=['DELETE'], detail=True)
    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)