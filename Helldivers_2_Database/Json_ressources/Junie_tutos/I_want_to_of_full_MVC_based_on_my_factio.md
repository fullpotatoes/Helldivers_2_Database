
# Full MVC Implementation for Faction Model

Based on your existing code and the factions.json file, I'll provide a complete MVC (Model-View-Controller) implementation for your Faction model. In Django, this translates to:

- **Model**: Your database model (Faction)
- **View**: Django REST Framework views/viewsets
- **Controller**: URL routing and serializers

## 1. Model (models.py)

First, let's update your model to follow Python naming conventions:

```python
from django.db import models

class Faction(models.Model):
    id = models.IntegerField(primary_key=True)  # Changed from AutoField to IntegerField to match your JSON
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Faction"
        verbose_name_plural = "Factions"
        db_table = "factions"
    
    def __str__(self):
        return self.name
```

## 2. Serializer (serializers.py)

Create a serializer for your Faction model:

```python
from rest_framework import serializers
from .models import Faction  # Updated import to use the renamed model

class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = ['id', 'name']
```

## 3. Views (views.py)

Implement a complete set of views for CRUD operations:

```python
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Faction  # Updated import
from .serializers import FactionSerializer

# Option 1: Using ViewSet (recommended for full CRUD)
class FactionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing faction instances.
    """
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer

# Option 2: Using individual class-based views
class FactionList(generics.ListCreateAPIView):
    """
    List all factions or create a new faction
    """
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer

class FactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a faction instance.
    """
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer

# Option 3: Using function-based views
@api_view(['GET', 'POST'])
def faction_list(request):
    """
    List all factions or create a new faction.
    """
    if request.method == 'GET':
        factions = Faction.objects.all()
        serializer = FactionSerializer(factions, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def faction_detail(request, pk):
    """
    Retrieve, update or delete a faction.
    """
    try:
        faction = Faction.objects.get(pk=pk)
    except Faction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FactionSerializer(faction)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FactionSerializer(faction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        faction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## 4. URLs (urls.py)

Update your URL patterns to use the new views:

### Option 1: Using ViewSet with Router (recommended)

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FactionViewSet

router = DefaultRouter()
router.register(r'factions', FactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### Option 2: Using individual class-based views

```python
from django.urls import path
from .views import FactionList, FactionDetail

urlpatterns = [
    path('factions/', FactionList.as_view(), name='faction-list'),
    path('factions/<int:pk>/', FactionDetail.as_view(), name='faction-detail'),
]
```

### Option 3: Using function-based views

```python
from django.urls import path
from .views import faction_list, faction_detail

urlpatterns = [
    path('factions/', faction_list, name='faction-list'),
    path('factions/<int:pk>/', faction_detail, name='faction-detail'),
]
```

## 5. Update Import Script

Update your import script to use the renamed model:

```python
import os
import json
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Helldivers_2_Database.settings')
django.setup()

# Import Django models
from Helldivers_2_Database.api.models import Faction  # Updated import

def import_factions():
    """Import factions data from JSON file"""
    print("Importing factions data...")
    
    # Path to the JSON file
    json_file_path = 'Ressources/Json/factions.json'
    
    try:
        # Open and read the JSON file
        with open(json_file_path, 'r') as file:
            factions_data = json.load(file)
        
        # Process each faction in the JSON data
        for faction_id, faction_name in factions_data.items():
            # Try to get existing faction or create a new one
            faction, created = Faction.objects.update_or_create(
                id=int(faction_id),  # Convert string ID to integer
                defaults={'name': faction_name}
            )
            
            if created:
                print(f"Created faction: {faction_name}")
            else:
                print(f"Updated faction: {faction_name}")
                
        print("Factions import completed successfully!")
        
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {json_file_path}")
    except Exception as e:
        print(f"Error importing factions: {e}")

if __name__ == "__main__":
    import_factions()
```

## 6. Implementation Steps

1. Update your models.py file with the improved Faction model
2. Run migrations to apply the changes:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Update serializers.py with the new FactionSerializer
4. Update views.py with your preferred view implementation (ViewSet recommended)
5. Update urls.py to match your chosen view implementation
6. Update your import script to use the renamed model
7. Run the import script to populate your database:
   ```
   python import_json_data.py
   ```

## Testing Your API

Once implemented, you can test your API using:

1. Django REST Framework's browsable API (just visit the URL in your browser)
2. Tools like Postman or curl
3. Python requests library

Example API endpoints:
- GET /api/factions/ - List all factions
- POST /api/factions/ - Create a new faction
- GET /api/factions/1/ - Get details for faction with ID 1
- PUT /api/factions/1/ - Update faction with ID 1
- DELETE /api/factions/1/ - Delete faction with ID 1

This implementation gives you a complete MVC structure for your Faction model with full CRUD capabilities.