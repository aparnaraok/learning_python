import settings
from django.template import Template, Context

t = Template('Hello, {{name}}')
for name in ('John', 'Julie', 'Par'):
    print(t.render(Context({'name':name})))
