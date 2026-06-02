import turtle

t = turtle.Turtle()
t.screen.setup(640, 640)
t.shape("square")
t.shapesize(1,1)
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.pu()

board = [["♖","♘","♗","♕","♔","♗","♘","♖"],
         ["♙","♙","♙","♙","♙","♙","♙","♙"],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["","","","","","","",""],
         ["♟","♟","♟","♟","♟","♟","♟","♟"],
         ["♜","♞","♝","♛","♚","♝","♞","♜"]
        ]

screen = t.screen

last_clicked_square = None
def on_click(x,y):
  global last_clicked_square
  col = int((x + 281) // 62)
  row = int((y + 281) // 62)
  if col < 0 or col > 7 or row < 0 or row > 7:
    return
  t.shapesize(3.1, 3.1)
  if last_clicked_square != None:
    piece_col, piece_row = last_clicked_square
    if board[piece_row][piece_col] != "":
      attempted_x = -250 + col * 62
      attempted_y = -250 + row * 62
      piece = board[piece_row][piece_col]
      board[piece_row][piece_col] = ""
      board[row][col] = piece
      prev_y = -250 + piece_row * 62
      prev_x = -250 + piece_col * 62
      t.goto(prev_x, prev_y)
      t.color("chocolate" if (piece_col + piece_row) % 2 == 0 else "wheat")
      t.stamp()
      t.goto(attempted_x, attempted_y)
      t.color("chocolate" if (col + row) % 2 == 0 else "wheat")
      t.stamp()
      t.goto(attempted_x, attempted_y - 21.5)
      t.color("black")
      t.write(piece, align="center", font=("Arial", 25, "normal"))
      last_clicked_square = None
      return
    
    


  print(col + 1, row + 1)  # Find a way so that the highlighted square goes back to its original state when another square is highlighted.
  piece = board[row][col] 
  y = -250 + row * 62
  x = -250 + col * 62
  t.goto(x,y)
  if last_clicked_square != None:
    prev_col, prev_row = last_clicked_square
    prev_y = -250 + prev_row * 62
    prev_x = -250 + prev_col * 62
    t.goto(prev_x, prev_y)
    prev_piece = board[prev_row][prev_col]
    t.color("chocolate" if (prev_col + prev_row) % 2 == 0 else "wheat")
    t.stamp()
    t.goto(prev_x, prev_y -21.5)
    t.color("black")
    t.write(prev_piece, align="center", font=("Arial", 25, "normal"))
    
  last_clicked_square = (col,row)
  t.goto(x,y)
  t.color("light blue") 
  t.stamp()

  y = -271.5 + row * 62
  x = -250 + col * 62

  t.goto(x,y)
  t.color("black")
  t.write(piece, align="center", font=("Arial", 25, "normal"))

  

    

def print_board_rim(): # Prints a big square that traces the board
  t.hideturtle()
  t.goto(-283,-283)
  
  t.color("black")
  t.pensize(2)
  t.pd()
  t.forward(500)
  t.lt(90)
  t.forward(500)
  t.lt(90)
  t.forward(500)
  t.lt(90)
  t.forward(500)


def print_squares():
  
  for row in range(8): #Each time this runs, col runs 8 times. 8 * 8 = 64 squares!
    y = -250 + row * 62
    x = -250 
    for col in range(8):
      if (col + row) % 2 == 0:
        t.color("chocolate")
      else:
        t.color("wheat")
      t.pu()
      t.goto(x, y)
      t.shapesize(3.1,3.1)
      t.stamp() 
      x += 62


def print_pieces():
  # starting positions for black pieces
  
  back_row_white = ["♖","♘","♗","♕","♔","♗","♘","♖"]
  back_row_black = ["♜","♞","♝","♛","♚","♝","♞","♜"]
  pawn_white = ["♙"]
  pawn_black = ["♟"]
  for col in range(8): # Whites Peices
      x = -250 + col * 62
      y = -271.5 + 0 * 62 
      piece = back_row_white[col]
      t.goto(x,y)
      t.color("black") 
      t.write(piece, align="center", font=("Arial", 25, "normal"))
  for col in range(8): # Whites Pawns
    x = -250 + col * 62
    y = -271.5 + 1 * 62 
    piece = pawn_white[0]
    t.goto(x,y)
    t.color("black") 
    t.write(piece, align="center", font=("Arial", 25, "normal"))
  
  for col in range(8): # Blacks Peices
    x = -250 + col * 62
    y = -271.5 + 7 * 62 
    piece = back_row_black[col]
    t.goto(x,y)
    t.color("black") 
    t.write(piece, align="center", font=("Arial", 25, "normal"))
  for col in range(8): # Black's Pawns
    x = -250 + col * 62
    y = -271.5 + 6 * 62 
    piece = pawn_black[0]
    t.goto(x,y)
    t.color("black") 
    t.write(piece, align="center", font=("Arial", 25, "normal"))



screen.tracer(0)
print_board_rim()
print_squares()
print_pieces()
screen.update()
screen.onclick(on_click)
turtle.done()


