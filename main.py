"""
Tower of Hanoi - Python Turtle Visualization
4 disks, animated with simple graphics.

Algorithm: Recursive
- To move n disks from source to target (using auxiliary):
    1. Recursively move n-1 disks from source to auxiliary
    2. Move the nth (largest) disk from source to target
    3. Recursively move n-1 disks from auxiliary to target
"""

import turtle
import time

# ── Constants ──────────────────────────────────────────────────────────────────
NUM_DISKS   = 4
PEG_X       = [-220, 0, 220]   # x-positions of the three pegs
PEG_BASE_Y  = -140             # y-position of the base
PEG_HEIGHT  = 180
DISK_HEIGHT = 24
DISK_COLORS = ["#E74C3C", "#E67E22", "#2ECC71", "#3498DB"]  # one per disk
MOVE_DELAY  = 0.4              # seconds between moves

# ── State ──────────────────────────────────────────────────────────────────────
# Each peg holds a stack of (disk_size, turtle_object)
pegs = [[], [], []]

# ── Screen setup ───────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Tower of Hanoi — 4 Disks (Recursive)")
screen.bgcolor("#1A1A2E")
screen.setup(width=700, height=500)
screen.tracer(0)  # manual updates for smooth animation

# ── Draw static pegs and base ──────────────────────────────────────────────────
def draw_static():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("#AAAAAA")
    t.pensize(2)

    # Base
    t.penup(); t.goto(-280, PEG_BASE_Y); t.pendown()
    t.goto(280, PEG_BASE_Y)

    # Peg labels
    labels = ["A", "B", "C"]
    for i, x in enumerate(PEG_X):
        # Vertical rod
        t.penup(); t.goto(x, PEG_BASE_Y)
        t.pendown(); t.goto(x, PEG_BASE_Y + PEG_HEIGHT)

        # Label
        t.penup(); t.goto(x, PEG_BASE_Y - 28)
        t.write(labels[i], align="center",
                font=("Courier", 14, "bold"))

# ── Disk turtle factory ────────────────────────────────────────────────────────
def make_disk(size, color):
    """Create a filled rectangle turtle representing one disk."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.shape("square")
    width = 30 + size * 22
    t.shapesize(stretch_wid=DISK_HEIGHT / 20,
                stretch_len=width / 20)
    t.fillcolor(color)
    t.pencolor("#1A1A2E")
    t.showturtle()
    return t, width

# ── Position helpers ───────────────────────────────────────────────────────────
def peg_x(peg_index):
    return PEG_X[peg_index]

def disk_y(peg_index, stack_pos):
    """y-coordinate for a disk at stack_pos (0 = bottom)."""
    return PEG_BASE_Y + DISK_HEIGHT * stack_pos + DISK_HEIGHT // 2

# ── Place all starting disks on peg 0 ─────────────────────────────────────────
def init_disks():
    # Disks numbered 1..NUM_DISKS; 1 = smallest (top), NUM_DISKS = largest (bottom)
    for size in range(NUM_DISKS, 0, -1):   # largest first → bottom of stack
        t, _ = make_disk(size, DISK_COLORS[size - 1])
        stack_pos = NUM_DISKS - size        # 0 = bottom
        t.goto(peg_x(0), disk_y(0, stack_pos))
        pegs[0].append((size, t))
    screen.update()

# ── Animate a single disk move ─────────────────────────────────────────────────
def animate_move(from_peg, to_peg):
    """
    Physically lift the top disk from from_peg,
    slide it across, and drop it onto to_peg.
    """
    size, t = pegs[from_peg].pop()

    lift_y   = PEG_BASE_Y + PEG_HEIGHT + 30   # height to lift above pegs
    target_x = peg_x(to_peg)
    land_y   = disk_y(to_peg, len(pegs[to_peg]))

    # 1. Lift up
    t.goto(t.xcor(), lift_y)
    screen.update(); time.sleep(MOVE_DELAY / 3)

    # 2. Slide across
    t.goto(target_x, lift_y)
    screen.update(); time.sleep(MOVE_DELAY / 3)

    # 3. Drop down
    t.goto(target_x, land_y)
    screen.update(); time.sleep(MOVE_DELAY / 3)

    pegs[to_peg].append((size, t))

# ── Recursive Tower of Hanoi ───────────────────────────────────────────────────
def hanoi(n, source, target, auxiliary):
    """
    Move n disks from source peg to target peg using auxiliary.

    Base case:  n == 1  →  move the single disk directly.
    Inductive:
        1. Move n-1 disks out of the way (source → auxiliary)
        2. Move the nth disk             (source → target)      ← direct move
        3. Move n-1 disks on top         (auxiliary → target)
    """
    if n == 1:
        # BASE CASE: direct move — recursion bottoms out here
        animate_move(source, target)
        return

    # RECURSIVE STEP 1: clear the way by moving n-1 disks to auxiliary
    hanoi(n - 1, source, auxiliary, target)

    # DIRECT MOVE: move the largest remaining disk to target
    animate_move(source, target)

    # RECURSIVE STEP 2: stack the n-1 disks from auxiliary onto target
    hanoi(n - 1, auxiliary, target, source)

# ── Main ───────────────────────────────────────────────────────────────────────
draw_static()
init_disks()

time.sleep(0.8)   # brief pause before solving begins

# Solve: move all 4 disks from peg A (0) to peg C (2) via peg B (1)
hanoi(NUM_DISKS, source=0, target=2, auxiliary=1)

# Done
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.pencolor("#F0F0F0")
label.goto(0, 180)
label.write("Solved!", align="center", font=("Courier", 18, "bold"))
screen.update()

turtle.done()