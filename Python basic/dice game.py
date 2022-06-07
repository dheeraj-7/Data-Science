import random
t=int(input())
for i in range(t):
  sides=[1,2,3,4,5,6]
  pc_in=random.choice(sides)
  usr_in=int(input())
  if usr_in<=6 and usr_in!=0:
    if usr_in>pc_in:
      print('User wins')
    elif pc_in>usr_in:
      print('PC wins')
    elif usr_in==pc_in:
      print('Tied')
    else:
      print('Roll Again correctly..!')
  else:
    print('Choose input in range : 0<input<7')