# FC-Mobile Soccer Video Game

## Overview
This project is a simple soccer video game built using Python. It features a game engine, player mechanics, and a basic game loop. The game is designed to be extensible, allowing for the addition of new features and enhancements.

## Project Structure
```
fc-mobile
├── src
│   ├── main.py
│   ├── fc-mobile
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   └── player.py
│   ├── assets
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── requirements.txt
├── README.md
└── setup.py
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fc-mobile
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. (macOS only) Install SDL2 dependencies required by pygame:
   ```
   brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
   ```

4. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the game, execute the following command:
```
python src/main.py
```

## Features
- Game engine that manages the game loop and state.
- Player class with movement and shooting mechanics.
- Modular structure for easy expansion and maintenance.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file