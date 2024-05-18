def handle_stuff(d:Data, q: quantity:int, screen:int, screen:int, status:int, c:Color):
  update_database(d, q, status)
  for i in range(0, quantity):
    profit[i] = revenue[i] - expense[i] * status
    new_color = c
    status =SUCCESS
    display_profits()


    