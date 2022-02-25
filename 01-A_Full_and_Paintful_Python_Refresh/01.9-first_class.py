
def divide(divided, divisor):
  if divisor == 0:
    raise ZeroDivisionError('No')
  
  return divided / divisor


def calculate(*values,operator):
  return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)
