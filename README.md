# Python Turtle Chess

A chessboard + piece renderer built with **Python’s `turtle` graphics**.

This repository currently focuses on drawing an 8×8 chessboard, placing the pieces using Unicode symbols, and letting you **click to move a piece** (basic “select a square, then select a destination” behavior). Move legality, turns, check/checkmate, etc. are not implemented yet.

## What’s in this repo?

- `turts.py` — main script that:
  - Creates a `turtle.Turtle()` configured as a square “stamp” for drawing tiles
  - Draws the board rim and 64 squares
  - Writes pieces on top of squares using Unicode chess characters
  - Handles mouse clicks to select a square and move a piece to another square

## How it works (high level)

- The board is stored as an 8×8 list called `board`.
- Each click is converted into a `(col, row)` index.
- First click: highlights the square.
- Second click: if the first square contained a piece, the piece is moved in `board` and the graphics are updated for the source and destination squares.

## Requirements

- Python 3.x
- No third-party dependencies (uses the standard library `turtle` module)

## Run

```bash
python turts.py
```

A 640×640 window should open with the chessboard.

## Controls

- **Click a square** to select/highlight it.
- **Click another square** to move the selected piece to the new square.

## Notes / Limitations

- No move validation (any piece can move anywhere).
- No turn system.
- Captures, check/checkmate, castling, en passant, and promotion are not implemented.
- Piece rendering uses `t.write(...)` with Unicode symbols; appearance depends on your system font.

## Ideas for next steps

- Add legal move generation per piece.
- Add turn handling (white then black).
- Implement captures and remove captured pieces from the board.
- Redraw from the `board` state each move (instead of partial stamping) to simplify rendering.
- Add UI/status text (whose turn, selected piece, invalid move messages).

## License

No license file is currently included. If you want others to use/modify this code, consider adding a license (MIT, Apache-2.0, GPL, etc.).
