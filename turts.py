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

white_pieces = ["♖","♘","♗","♕","♔","♙"]
black_pieces = ["♜","♞","♝","♛","♚","♟"]

screen = t.screen

last_clicked_square = None
white_turn = True
def restore_square(col,row): 
  x = -250 + col * 62
  y = -250 + row * 62
  t.goto(x,y)
  t.color("chocolate" if (col + row) % 2 == 0 else "wheat")
  t.stamp()
  if board[row][col] != "":
    t.goto(x,y - 21.5)
    t.color("black")
    t.write(board[row][col], align="center", font=("Arial", 25, "normal"))

def highlight_square(col,row):
  x = -250 + col * 62
  y = -250 + row * 62
  t.goto(x,y)
  t.color("light blue")
  t.stamp()
  t.goto(x,y - 21.5)
  t.color("black")
  t.write(board[row][col], align="center", font=("Arial", 25, "normal"))

def is_legal_move(from_col, from_row, to_col, to_row, check_white):
  
  if check_white == True:
    piece_set = white_pieces
  else:
    piece_set = black_pieces
    
  if board[to_row][to_col] in piece_set:
    return False

  piece = board[from_row][from_col]

  if piece == "♙":
      if to_col == from_col and to_row == from_row + 1 and board[to_row][to_col] == "":
          return True
      
      elif to_col == from_col and to_row == from_row + 2 and from_row == 1 and board[to_row][to_col] == "" and board[from_row + 1][from_col] == "":
          return True
      
      elif abs(to_col - from_col) == 1 and to_row == from_row + 1 and board[to_row][to_col] != "":
        return True
      
      else:
          return False
  
  if piece == "♟":
      if to_col == from_col and to_row == from_row - 1 and board[to_row][to_col] == "":
          return True
      
      elif to_col == from_col and to_row == from_row - 2 and from_row == 6 and board[to_row][to_col] == "" and board[from_row - 1][from_col] == "":
          return True
      
      elif abs(to_col - from_col) == 1 and to_row == from_row - 1 and board[to_row][to_col] != "":
        return True
      
      else:
          return False
  
  if piece == "♞" or piece == "♘":
    if abs(to_col - from_col) == 2  and abs(to_row - from_row) == 1:
      return True
    elif abs(to_col - from_col) == 1  and abs(to_row - from_row) == 2:
      return True
    else:
      return False

  if piece == "♚" or piece == "♔":
    if abs(to_col - from_col) <= 1 and abs(to_row - from_row) <= 1:
      return True
    else:
      return False
    
  if piece == "♖" or piece == "♜":
    if to_col == from_col or to_row == from_row:
      # Horizontal Move (Row stays the same)
      if to_row == from_row:
        for c in range(min(from_col, to_col) + 1, max(from_col, to_col)):
          if board[from_row][c] != "":
            return False
        return True
        
      # Vertical Move (Column stays the same)
      elif to_col == from_col:
        for r in range(min(from_row, to_row) + 1, max(from_row, to_row)):
          if board[r][from_col] != "":
            return False
        return True

      
    
    else:
      return False
  
  if piece == "♗" or piece == "♝":
    # 1. Is it a perfect diagonal line?
    if abs(to_col - from_col) == abs(to_row - from_row):
      
      # 2. Figure out the direction of the steps (1 for right/down, -1 for left/up)
      if to_col > from_col:
        col_step = 1
      else:
        col_step = -1
        
      if to_row > from_row:
        row_step = 1
      else:
        row_step = -1
        
      # 3. Check every square along the path
      distance = abs(to_col - from_col)
      for i in range(1, distance):
        c = from_col + (i * col_step)
        r = from_row + (i * row_step)
        if board[r][c] != "":
          return False  # Something is blocking the path!
          
      return True # The path is clear!
      
    else:
      return False # It wasn't a diagonal move

  if piece == "♛" or piece == "♕":
    
    if to_col == from_col or to_row == from_row:
      # Horizontal Move (Row stays the same)
      if to_row == from_row:
        for c in range(min(from_col, to_col) + 1, max(from_col, to_col)):
          if board[from_row][c] != "":
            return False
        return True
        
      # Vertical Move (Column stays the same)
      elif to_col == from_col:
        for r in range(min(from_row, to_row) + 1, max(from_row, to_row)):
          if board[r][from_col] != "":
            return False
        return True
    
    elif abs(to_col - from_col) == abs(to_row - from_row):
      
      # 2. Figure out the direction of the steps (1 for right/down, -1 for left/up)
      if to_col > from_col:
        col_step = 1
      else:
        col_step = -1
        
      if to_row > from_row:
        row_step = 1
      else:
        row_step = -1
        
      # 3. Check every square along the path
      distance = abs(to_col - from_col)
      for i in range(1, distance):
        c = from_col + (i * col_step)
        r = from_row + (i * row_step)
        if board[r][c] != "":
          return False  # Something is blocking the path!
          
      return True # The path is clear!
    
    
    else:
      return False

    
  return True
    
def move_piece(from_col, from_row, to_col, to_row):
  piece = board[from_row][from_col]
  board[from_row][from_col] = ""
  board[to_row][to_col] = piece
  
  if piece ==  "♙" and to_row == 7:
    board[to_row][to_col] = "♕"

  if piece == "♟" and to_row == 0:
    board[to_row][to_col] = "♛"
  
  restore_square(from_col, from_row)
  restore_square(to_col, to_row) 

def is_square_under_attack(target_col, target_row, attacker_is_white):
  for r in range(8):
    for c in range(8):
      piece = board[r][c]

      if piece == "":
        continue

      if attacker_is_white == True and piece in black_pieces:
        continue
      if attacker_is_white == False and piece in white_pieces:
        continue
      if is_legal_move(c,r,target_col,target_row,attacker_is_white):
        return True
  return False

def has_legal_moves(attacker_is_white):
  for r in range(8):
    for c in range(8):
      piece = board[r][c]
      if piece == "":
        continue
      elif attacker_is_white and piece in black_pieces:
        continue
      elif not attacker_is_white and piece in white_pieces:
        continue
      for dest_row in range(8):
        for dest_col in range(8):
          if is_legal_move(c, r, dest_col, dest_row, attacker_is_white):
            hypo_capt_piece = board[dest_row][dest_col]
            board[r][c] = ""
            board[dest_row][dest_col] = piece
            if attacker_is_white:
              target_king = "♔"
            else:
              target_king = "♚"
              
            
            for kr in range(8):
              for kc in range(8):
                if board[kr][kc] == target_king:
                  king_row = kr
                  king_col = kc
            
            king_in_check = is_square_under_attack(king_col, king_row, not attacker_is_white)
            board[r][c] = piece
            board[dest_row][dest_col] = hypo_capt_piece
            if not king_in_check:
              return True
            
  return False
     
def on_click(x,y):
  
  global last_clicked_square
  global white_turn 
  
  col = int((x + 281) // 62)
  row = int((y + 281) // 62)
  

  if col < 0 or col > 7 or row < 0 or row > 7:
    return
  
  t.shapesize(3.1, 3.1)

  if last_clicked_square != None: 
    piece_col, piece_row = last_clicked_square
    
    if board[piece_row][piece_col] != "":
      froms = piece_col, piece_row
      tos = col, row
      if froms == tos:
        restore_square(piece_col, piece_row)
        last_clicked_square = None
        return
      if is_legal_move(piece_col, piece_row, col, row, white_turn):
        piece = board[piece_row][piece_col]
        hypo_capt_piece = board[row][col]
        board[piece_row][piece_col] = ""
        if board[row][col] != "":
          hypo_capt_piece = board[row][col]
          board[row][col] = ""
        board[row][col] = piece

        if white_turn:
          target_king = "♔"
        else:
          target_king = "♚"
        
        for r in range(8):
          for c in range(8):
            square = board[r][c]
            if square == target_king:
              king_row = r
              king_col = c
              king_in_check = is_square_under_attack(king_col, king_row, not white_turn)
        
        board[piece_row][piece_col] = piece
        
        board[row][col] = hypo_capt_piece


        if king_in_check:
          return
        else:

          move_piece(piece_col, piece_row, col, row)

        last_clicked_square = None
        white_turn = not white_turn
        if has_legal_moves(white_turn) == False:
          print("CHEKMATETETTETET")
      else:
        return
      
      
          
      


  print(col , row )  # Find a way so that the highlighted square goes back to its original state when another square is highlighted.
  piece = board[row][col]
  if white_turn == True and piece not in white_pieces:
    return
  if white_turn == False and piece not in black_pieces:
    return

  y = -250 + row * 62
  x = -250 + col * 62
  t.goto(x,y)
  if last_clicked_square != None:
    prev_col, prev_row = last_clicked_square
    restore_square(prev_col, prev_row)
    
  last_clicked_square = (col,row)
  highlight_square(col,row)

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

def print_coordinates():
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
  for col in range(8):
    x = -250 + col * 62
    y = -310
    t.goto(x,y)
    t.color("black")
    t.write(letters[col], align="center", font=("Arial", 10, "normal"))
  for row in range(8):
    x = 240
    y = -250 + row * 62 - 7
    t.goto(x,y)
    t.color("black")
    t.write(int(row + 1), align="center", font=("Arial", 10, "normal"))

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

print_coordinates()

screen.update()

screen.onclick(on_click)

turtle.done()


