# How to Use Views Data in HTML Templates

This guide explains how to pass data from Django views to HTML templates and how to use that data in your templates.

## 1. Passing Data from Views to Templates

In your view function, create a context dictionary containing the data you want to pass to the template:

```python
def hello_world(request):
    # Create a context dictionary with data to pass to the template
    context = {
        'title': 'Hello Helldivers',
        'message': 'Welcome to the Helldivers 2 Database!',
        'items': ['Liberty', 'Democracy', 'Freedom'],
    }
    return render(request, 'planets.html', context)
```

The `render` function takes three arguments:
- The request object
- The template name
- The context dictionary (optional)

## 2. Using Data in Templates

In your HTML template, you can access the context variables using double curly braces `{{ variable }}`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    
    <h2>Core Values:</h2>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## 3. Template Tags and Filters

Django templates support various tags and filters:

### Common Template Tags:

- `{% for %}` ... `{% endfor %}`: For looping through lists
- `{% if %}` ... `{% elif %}` ... `{% else %}` ... `{% endif %}`: For conditional rendering
- `{% block %}` ... `{% endblock %}`: For template inheritance
- `{% include %}`: For including other templates

### Example of Conditional Rendering:

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

### Template Filters:

Filters modify the values of variables. They are applied using the pipe character `|`:

```html
<p>{{ message|upper }}</p>  <!-- Converts to uppercase -->
<p>{{ message|length }}</p>  <!-- Displays the length of the string -->
<p>{{ message|default:"No message" }}</p>  <!-- Provides a default value if message is empty -->
```

## 4. Accessing Model Data

You can also pass model instances or querysets to templates:

```python
def planet_list(request):
    planets = Planet.objects.all()
    return render(request, 'planet_list.html', {'planets': planets})
```

Then in your template:

```html
<h1>Planets</h1>
<ul>
    {% for planet in planets %}
        <li>{{ planet.name }} - {{ planet.biome.name }}</li>
    {% endfor %}
</ul>
```

## 5. Working with Complex Data

For more complex data structures, you can access nested attributes:

```html
<!-- Accessing dictionary keys -->
<p>{{ data.key }}</p>

<!-- Accessing object attributes -->
<p>{{ object.attribute }}</p>

<!-- Accessing list items -->
<p>{{ list.0 }}</p>  <!-- Accesses the first item in the list -->
```

## Summary

1. Create a context dictionary in your view function
2. Pass the context to the template using the render function
3. Access the context variables in your template using {{ variable }}
4. Use template tags like {% for %} and {% if %} for more complex logic