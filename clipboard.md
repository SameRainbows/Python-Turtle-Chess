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