The Python turtle module is a popular way to introduce programming through visual graphics. Here are the most common commands categorized by their function:

1. Movement

    forward(distance) (or fd): Moves the turtle forward by the specified distance.

    backward(distance) (or bk): Moves the turtle backward.

    right(angle) (or rt): Turns the turtle clockwise.

    left(angle) (or lt): Turns the turtle counter-clockwise.

    goto(wx, y): Moves the turtle to an absolute position on the grid.

    home(): Returns the turtle to the center of the screen (0,0).

    circle(radius): Draws a circle with a given radius.

2. Pen Control

    penup() (or pu): Lifts the pen so the turtle doesn't draw while moving.

    pendown() (or pd): Puts the pen down to start drawing again.

    pensize(width): Changes the thickness of the lines.

    pencolor(color): Changes the color of the line (e.g., "red", "blue", or hex codes).

    speed(speed): Sets the animation speed (1 is slow, 10 is fast, 0 is the fastest).

3. Filling Shapes

    fillcolor(color): Sets the color used to fill shapes.

    begin_fill(): Call this before drawing a shape you want to fill.

    end_fill(): Call this after finishing the shape to fill it with color.

4. Turtle State

    shape(name): Changes the turtle icon (e.g., "turtle", "arrow", "circle", "square").

    hideturtle() (or ht): Makes the turtle invisible.

    showturtle() (or st): Makes the turtle visible again.

    clear(): Erases all drawings but leaves the turtle in its current position.

    reset(): Erases everything and returns the turtle to the center.

5. Screen / Window Setup

    screen = turtle.Screen(): Gets the screen object so you can configure it.

    screen.setup(width, height): Sets the window size in pixels (e.g., screen.setup(640, 640)).

    screen.title("My Chess Game"): Sets the window title bar text.

    screen.bgcolor(color): Sets the background color of the entire window.
    
    screen.tracer(0): Turns off auto-animation — the screen won't update until you call

    screen.update(). Essential for performance when drawing the board.

    screen.update(): Manually redraws the screen. Use after tracer(0) to push all drawing at once.

    screen.listen(): Tells the screen to listen for keyboard/mouse events.
    
    screen.mainloop(): Starts the event loop — keeps the window open and responsive. Call at the very 
    end of your program.

6. Writing Text

    t.write(text, align, font): Draws text at the turtle's current position.
        align: "left", "center", or "right"
        font: a tuple like ("Arial", 16, "normal") — can also be "bold" or "italic"
        Example: t.write("♟", align="center", font=("Arial", 32, "normal"))
    
    Note: Chess piece Unicode characters you can write as strings:
        ♙♘♗♖♕♔  (white pieces)
        ♟♞♝♜♛♚  (black pieces)

7. Stamping

    t.shape("square"): Sets the turtle shape to a built-in square (useful for stamping board squares).
    t.shapesize(stretch_wid, stretch_len): Scales the turtle shape. shapesize(3, 3) makes a square 3x the default size.
    t.stamp(): Stamps a copy of the current turtle shape onto the canvas at the current position. Returns a stamp ID.
    t.clearstamp(stamp_id): Removes a specific stamp by its ID. Useful for moving a piece (clear old stamp, stamp at new location).
    t.clearstamps(): Removes all stamps made by this turtle.

8. Coordinates & Positioning

    t.goto(x, y): Moves the turtle to exact screen coordinates. (0, 0) is the center of the screen.
    t.setx(x): Moves the turtle to a specific x coordinate, keeping y the same.
    t.sety(y): Moves the turtle to a specific y coordinate, keeping x the same.
    t.pos() or t.position(): Returns the turtle's current (x, y) position as a tuple.
    t.xcor(): Returns only the x coordinate.
    t.ycor(): Returns only the y coordinate.
    t.setheading(angle): Points the turtle in an absolute direction (0=East, 90=North, 180=West, 270=South).
    t.towards(x, y): Returns the angle the turtle would need to face to point toward (x, y).
    t.distance(x, y): Returns the distance from the turtle to a given point.

    Board coordinate tip — to convert a chess grid column/row (0–7) to screen x/y:
        x = col * square_size - board_offset
        y = row * square_size - board_offset

9. Mouse & Keyboard Events

    screen.onclick(handler): Calls handler(x, y) whenever the user clicks anywhere on the screen.

    t.onclick(handler): Calls handler(x, y) when the user clicks directly on the turtle.

    screen.onkey(handler, key): Calls handler() when a key is pressed (must call screen.listen() first).

    screen.onkeypress(handler, key): Like onkey but fires continuously while the key is held.

    screen.onscreenclick(handler): Alternative to screen.onclick — passes (x, y) of click to handler.

    Example pattern for piece selection:
        def on_click(x, y):
            col = int((x + board_offset) // square_size)
            row = int((y + board_offset) // square_size)
            # use col, row to identify the clicked square
        screen.onclick(on_click)

10. Multiple Turtles

    pen = turtle.Turtle(): Creates an additional turtle. You can have one turtle per piece, or one dedicated drawing turtle and one for UI, etc.
    turtle.Turtle() instances are independent — each has its own position, color, pen state, and stamps.
    Tip: Create a separate "board" turtle and "pieces" turtle so you can redraw pieces without redrawing the board.

11. Performance Tips

    Call screen.tracer(0) at the start, then screen.update() only once after all drawing is done — this avoids watching each square get drawn one by one.
    Use t.penup() before every goto() so the turtle doesn't drag lines across the screen while repositioning.
    hideturtle() on any turtle that's just used for drawing (not visible to the user) speeds up rendering noticeably.
    For moving a piece: use stamp IDs — stamp when placed, clearstamp when moved, stamp at new location.