#here direct variable (person) is passed as a parameter to context
#values can be accessed via dot operator.

from django.template import Template, Context
person = {'name' : 'Sally', 'age' : 43}
t = Template('{{person1.name}} is {{person1.age}} years old.')
c = Context({'person1' : person})
print(t.render(c))

# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/mysite$ python manage.py shell < direct_var_context.py
# Sally is 43 years old.
