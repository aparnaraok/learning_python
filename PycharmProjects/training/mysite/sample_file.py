#import settings
from django.template import Template, Context

t = Template('Hello, {{name}}')
for name in ('John', 'Julie', 'Par'):
    print(t.render(Context({'name':name})))

#python manage.py shell < sample_file.py

# Hello, John
# Hello, Julie
# Hello, Par