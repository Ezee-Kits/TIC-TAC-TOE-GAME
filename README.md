# Tic-Tac-Toe Game in Python

This Python script implements the classic **Tic-Tac-Toe** game, also known as **Noughts and Crosses**. It's a simple two-player game where players take turns marking spaces in a 3x3 grid. The first player to align three of their marks either horizontally, vertically, or diagonally wins the game.

## 🎮 Features

- **2-Player Mode**: Play against a friend on the same device.
- **Command Line Interface**: The game is run through the terminal, providing an interactive experience.
- **Error Handling**: Prevents invalid moves, such as marking already filled spaces.
- **Grid Display**: Shows the current state of the game board after every turn.
- **Win Detection**: Automatically detects and announces the winner or a draw.

## 🚀 How It Works

1. Players take turns to input their moves, choosing an empty spot on the grid.
2. The grid updates after every move, showing the current game state.
3. The game checks for a winner after every move. If no player wins and the grid is full, the game declares a draw.

### Key Components:

- **Game Board**: A 3x3 grid that is updated with each player's move.
- **Player Input**: Players are prompted to choose a position on the grid.
- **Win/Draw Detection**: The game checks if a player has won by forming a horizontal, vertical, or diagonal line, or if the game ends in a draw.

## 🛠️ Requirements

- **Python 3.x**

No additional libraries are required.

## 🏃 How to Run the Script

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/Tic-Tac-Toe-Game.git
   ```

2. **Run the Python Script**:
   ```bash
   python tic_tac_toe.py
   ```

3. **Start Playing**:  
   Follow the instructions on the terminal to input your moves.

## 🎲 Game Rules

- The game is played on a 3x3 grid.
- One player is "X" and the other player is "O".
- Players take turns placing their marks in empty spaces.
- The first player to align three of their marks horizontally, vertically, or diagonally wins the game.
- If all nine spaces are filled without a winner, the game ends in a draw.

## 📝 Example Game

```
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
```

Player 1 (X) chooses position 1:
```
 X | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
```

Player 2 (O) chooses position 5:
```
 X | 2 | 3 
-----------
 4 | O | 6 
-----------
 7 | 8 | 9 
```

The game continues until one player wins or it's a draw.

## 🔧 Future Improvements

- **AI Player**: Implement a single-player mode where you can play against the computer.
- **Graphical Interface**: Build a GUI version of the game using libraries like Tkinter or Pygame.
- **Move Validation**: Add more detailed error messages for invalid inputs.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing

Feel free to contribute by opening issues, suggesting improvements, or submitting pull requests. All feedback is welcome!
