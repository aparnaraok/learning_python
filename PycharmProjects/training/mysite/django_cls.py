from django.template import Template, Context
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name


t = Template('Hello, {{person.first_name.upper}} {{person.last_name}}.')
c = Context({'person' : Person('John', 'Smith')})
print(t.render(c))

# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/mysite$ python manage.py shell < django_cls.py
# Hello, John Smith.