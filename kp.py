from machine import Pin

row_list = [19, 18, 17, 16]  
col_list = [22, 21, 20]

for x in range(0, 4):
  row_list[x] = Pin(row_list[x], Pin.OUT)
  row_list[x].value(1)
   
for x in range(0 ,3):
  col_list[x] = Pin(col_list[x], Pin.IN, Pin.PULL_UP)

key_list = [["1", "2", "3"],\
      ["4", "5", "6"],\
      ["7", "8", "9"],\
      ["*", "0", "#"]]

def keypad(col, row):
  for r in row:
    r.value(0)
    result = [col[0].value(), col[1].value(), col[2].value()]
    if min(result) == 0:
      key = key_list[int(row.index(r))][int(result.index(0))]
      r.value(1)
      return (key)
    r.value(1)