from prefect import Flow, Parameter

with Flow("math") as f:
    x, y = Parameter("x"), Parameter("y")
    a = x + y

f.visualize()