import django
from django.template import Template, Context

'''
t = Template("My name is {{name}}.")
c = Context({"name":"Aparna"})
print(t.render(c))
'''

t = Template('Hello, {{name}}')
for name in ('John', 'Julie', 'Par'):
    print(t.render(Context({'name':name})))


#print(django.get_version())

