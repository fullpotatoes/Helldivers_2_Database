
# Creating a "Hello World" HTML Page in Your Django Project

Based on your project structure, here's how to create a "Hello World" HTML page:

## 1. Create the HTML File

Create your "hello_world.html" file in the existing templates directory:

```
/Helldivers_2_Database/api/templates/hello_world.html
```

Content for hello_world.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>This is my first Django page.</p>
</body>
</html>
```

## 2. Create the View

Add a new view function in your views.py file:

```python
# Add this import at the top of the file
from django.shortcuts import render

# Add this view function
def hello_world(request):
    return render(request, 'hello_world.html')
```

## 3. Configure the URL

Update your API urls.py file to include the new view:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FactionViewSet, SectorViewSet, BiomeViewSet, EnvironmentalViewSet, PlanetViewSet,
    WeaponTypeViewSet, FireModeViewSet, WeaponTraitViewSet, WeaponViewSet,
    ArmorSlotViewSet, ArmorPassiveViewSet, ArmorViewSet, BoosterViewSet, ItemViewSet,
    hello_world  # Add this import
)

# Router configuration remains the same
router = DefaultRouter()
# ... existing router registrations ...

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),  # Add this line
    path('', include(router.urls)),
    path('admin/', include(router.urls))
]
```

After making these changes, you should be able to access your "Hello World" page at:
```
http://localhost:8000/hello/
```

This approach integrates your new page with the existing project structure while keeping it simple for testing purposes.