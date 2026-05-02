# Anaconda Snake Game

A Python-based Snake game built using Pygame featuring smooth gameplay, dynamic difficulty, and score tracking.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Structure](#-project-structure)
- [Assets Required](#-assets-required)
- [Troubleshooting](#-troubleshooting)

## Features
- Start screen and game over screen
- Dynamic difficulty (speed increases with score)
- Sound effects for actions
- High score tracking
- Custom visuals and grid system

## Tech Stack
- Python 3.7+
- Pygame

## Installation
- Install pygame:
   ```bash
   pip install pygame


## How to Run
1. Run the Game:
   ```bash
   python game.py
2. Controls:

Arrow Keys - Move the snake
Space - Start game / Pause
ESC - Quit game

3. Objective: Eat food to grow longer while avoiding walls and yourself!

## Project Structure

Snake_game/
├── game.py                          # Main game file
├── assets/
│   ├── python_logo.png             # Game logo/icon
│   ├── eat.wav                     # Sound effect for eating
│   ├── gameover.wav                # Sound effect for game over
│   └── screenshots/
│       ├── start_screen.png        # Start screen screenshot
│       ├── gameplay.png            # Gameplay screenshot
│       └── gameover_screen.png     # Game over screen screenshot
└── README.md                        # This file

## Assets Required

| Asset | Type | Purpose |
|-------|------|---------|
| `python_logo.png` | Image | Game logo/window icon |
| `eat.wav` | Audio | Sound when snake eats food |
| `gameover.wav` | Audio | Sound when game ends |

**Screenshots** :
- `start_screen.png` 
- `gameplay.png` 
- `gameover_screen.png` 

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'pygame'` | Run `pip install pygame` |
| No sound effects playing | Verify `.wav` files are in `assets/` directory and paths are correct |
| Game runs slowly or stutters | Close other applications or reduce screen resolution |
| Assets not loading (black screen) | Check that image and audio files are in correct directory paths |
| Game window won't open | Ensure Pygame is properly installed: `pip install --upgrade pygame` |


























