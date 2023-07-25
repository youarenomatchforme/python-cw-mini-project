# write your code here
def padel_court_cost(court_type):
    if court_type == ("indoors"):
     return 30
    elif court_type == ("outdoors"):
       return 20
    

def racket_cost(racket_brand):
   if racket_brand == ("Bullpadel"):
    return 100
   elif racket_brand == ("Nox"):
    return 140
   elif racket_brand == ("Siux"):
     return 200
   

def padel_ball_cost(ball_boxes):
  if ball_boxes == 1:
   return 2
  elif ball_boxes == 2:
    return 3.5
  elif ball_boxes == 3:
    return 5
  
 
def padel_game_cost():
    court_type = input("Is the court type indoors or outdoors?")
    racket_brand = input("What racket brand do you need? Bullpadel, Nox, or Siux?")
    ball_boxes = int(input("How many number of ball boxes? 1, 2, or 3?"))
    total_cost = padel_court_cost(court_type) + racket_cost(racket_brand) + padel_ball_cost(ball_boxes)
    


