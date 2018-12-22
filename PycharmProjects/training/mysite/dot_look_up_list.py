#List can be accessed using number(indices)
#Negative indices not allowed.

from django.template import Template, Context

t = Template('{{var}} -- {{var.upper}} -- {{var.isdigit}}')
c = Context({'var' : 'hello'})

print(t.render(c))

t = Template('Item 2 is {{items.2}}.')
c = Context({'items':['apples', 'bananas', 'carrots']})
print(t.render(c))