Timeline of Game SO far
1. Two-Player Platform/Side-Scroller System

Two independently controlled players (P1 + P2)

Ground + platform collision

Individual health, jumping, movement, shooting, and blocking
✔ Implemented effectively — stable movement & consistent collision.

2. Shooting System for Both Players

P1 shoots with Right Ctrl

P2 shoots with Left Shift

Bullet cap + cooldown per player

Bullets deal damage and despawn properly
✔ Works well — balanced, readable, and clean hit detection.

3. Enemy System

Walkers and Shooters

Shooter enemies fire bullets

Enemies scale with score

Enemy HP bars

Enemies drop abilities occasionally
✔ Enemy behavior solid — movement and combat are reliable.

4. Enemy Bullets With Player Blocking Mechanic

Players can activate a temporary shield:

P1 block = Right Shift

P2 block = Q

Bullet collisions check if shield is active

If blocking → bullet is destroyed

If not blocking → damage taken
✔ Very effective — block windows & cooldowns work smoothly.

5. Pink Ability Block (Double Damage Power-Up)

Random spawn rate

Limited lifetime

Pick-up grants double damage for 10 seconds

UI indicator shown
✔ Functional and noticeable — ability timing & effects work.

6. Shared Shop System

Open/close with H

Pauses gameplay while open

Shared upgrades available:

+1 Health

+1 Speed

+1 Damage

Shared score used as currency

Upgrades apply to both players
✔ Effective UI and functionality — simple but clean shop interface.

7. Scoring, High Score Tracking, and Timer

Score increases when enemies are killed

5-minute timer

High score updates when game ends

HUD shows all info clearly
✔ HUD is strong and readable — good at showing game state.

8. Game Over + Restart Flow

Transparent overlay

Options: R = restart, Q = quit

Score and difficulty reset properly
✔ Works as intended — smooth loop for testing and gameplay.

9. Rectangle-Only Graphics (No PNGs)

All characters, enemies, bullets, platforms, and UI are rectangles

100% PyInstaller-compatible
✔ Executed perfectly — simple visuals but ideal for performance
https://drive.google.com/file/d/16pS_qCOKjPzeVGRcb6U_tzk3Gv6k3hM9/view
