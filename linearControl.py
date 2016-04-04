import sys
import time

if __name__ == "__main__":
  EPSILON = 10**0
  SLEEP = 0.5
  MOVEMENT = sys.argv[1]
  disVec = getDis(MOVEMENT)
  while(sum(x**2 for x in disVec) < EPSILON):
    lr_move(disVec[0], MOVEMENT)
    fb_move(disVec[1], MOVEMENT)
    time.sleep(SLEEP)
    disVec = getDis(MOVEMENT)
  print('Got to location')

def disVec(movement):
  """Returns a tuple (x-lr,y-fb) distances."""
  if movement is 'gps':
    print('Empty')
    return (0, 0)
  if movement is 'img':
    print('Empty')
    return (0, 0)
  if movement is 'test':
    print('Insert distance')
    lr = input('lr value: ')
    fb = input('fb value: ')
    return (lr, fb)
    
