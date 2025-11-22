● CAR RACING GAME 
● Overview:This Python code is a simple but complete car racing game built using the Pygame library. It creates a 500x500 window simulating a road with three lanes bordered by edge markers with grass on the sides. 
The game features a player-controlled car that can move between three lanes and vertically by using arrow keys.
Enemy vehicles randomly appear in any of the three lanes and move downward, simulating oncoming traffic. The player must avoid collisions with these vehicles by switching lanes or moving vertically. 
The game speeds up progressively after every 5 passed enemy vehicles, and the player's score increases accordingly.
Collision detection is implemented for both side swipe and head-on crashes. When a collision occurs, a crash image is displayed, and the game enters a "game over" state where the player can choose to restart or 
quit using keyboard input. The game also draws lane markers that animate downward, adding to the motion effect.
The code uses sprite groups for organized management of the player and enemy vehicles, scales vehicle images to fit lanes, and manages game timing with a fixed frame rate for smooth animation.
Overall, the program demonstrates the essential aspects of a basic arcade car game including rendering graphics, handling user input, game loop control, collision detection, scoring, and simple visual 
effects — serving as a good introductory example for Pygame game development.

● Features:The key features of this Python Pygame car game code are:
Window and Graphics Setup: Creates a 500x500 game window with a gray road, green grass background, yellow edge road markers, and white lane markers that animate downward to simulate movement.
Lane-based Gameplay: The road has three predefined lanes (left, center, right), and the player’s car is restricted to moving horizontally between these lanes as well as vertically within the lane.
Player Control: Player-controlled car moves left, right, up, and down via arrow keys with boundary checks to keep it within lanes and screen limits.
Vehicle Sprites and Scaling: Uses sprite classes to represent vehicles with images scaled to fit lane width, supporting organized management and collision checking.
Enemy Vehicle Generation: Random enemy vehicles spawn at the top of random lanes (limiting simultaneous vehicles) and move downward, incrementing score and increasing game speed each time player passes 5 vehicles.
Collision Detection: Implements side swipe collision when changing lanes and head-on collision detection, triggering a game over state with crash visuals.
Score Tracking and Display: Keeps count of score based on vehicles successfully avoided, displaying it during gameplay.
Game Over and Replay: When collision occurs, displays crash image and prompts player to press 'Y' to restart or 'N' to quit, resetting necessary variables and clearing enemy vehicles if game restarts.
Smooth Animation: Runs at 120 frames per second with smooth lane marker movement and vehicle motion, optimizing gameplay feel.

● Technologies/tools used:This Python car game code primarily uses the following technologies:
Python Programming Language: The game is written entirely in Python, leveraging its simplicity and readability for game development.
Pygame Library: Core technology for game creation, handling window creation, graphics rendering, sprite management, event handling (keyboard input), collision detection, and timing control with its built-in 
modules and functions.
Pygame Sprites: Utilizes Pygame's built-in Sprite and Group classes for managing game objects like player and enemy vehicles efficiently, enabling collision detection and rendering.
Image Assets: Uses external image files (PNG format) for the player's car, enemy vehicles, and crash animation, loaded and scaled dynamically within the game.
2D Graphics Rendering: The game uses Pygame’s drawing functions for static elements such as road, lane markers, grass, and edge markers, combined with sprite blitting for vehicles.
Keyboard Input Handling: Implements user controls for moving the player’s vehicle with arrow keys detected through Pygame’s event system.
Game Loop and Frame Management: Uses a main game loop with a frame rate capped at 120 fps using Pygame's Clock module for smooth animation and gameplay timing.

● Steps to install & run the project:Steps to install and run the car game project using the given Python Pygame code:
Install Python:
Download and install the latest version of Python from the official website (https://www.python.org/downloads/).
Ensure Python is added to your system's PATH environment variable.
Install Pygame:
Open your command prompt or terminal.
Run the command: pip install pygame
This installs the Pygame library, which is required to run the game code.
Prepare Image Assets:
Ensure you have the following image files in the same directory as the Python script:
car.png (player’s car)
pickup_truck.png, semi_trailer.png, taxi.png, van.png (enemy vehicles)
crash.png (crash effect)
These image files should be appropriately sized or will be scaled by the program.
Save the Python code:
Copy the provided code into a file named (for example) car_game.py in the directory containing the image assets.
Run the Game:
In the command prompt or terminal, navigate to the directory containing car_game.py.
Run the command: python car_game.py
The game window will open, and you can play using the arrow keys.
Gameplay:
Use left/right arrows to move the player’s car between lanes.
Use up/down arrows to move vertically within the lane.
Avoid enemy vehicles that move downward.
After a collision, press 'Y' to restart or 'N' to quit.

● Instructions for testing:
Instructions for testing the car game code:
Setup:
Make sure Python is installed on your system.
Install Pygame via pip install pygame.
Place the Python script and all required image files ('car.png', 'pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png', 'crash.png') in the same folder.
Running the game:
Run the Python script from your terminal or IDE: python car_game.py.
The game window will open with the road and starting player car.
Controls Testing:
Test player movement using arrow keys:
Left and Right arrows: move the car between the three lanes.
Up and Down arrows: move vertically inside the lane, checking boundary limits.
Verify the car stays within lanes and screen limits.
Gameplay Testing:
Observe enemy vehicles spawning randomly in different lanes moving downward.
Verify vehicles are removed when off-screen and the score increments correctly.
Confirm the speed increases after every 5 vehicles passed.
Collision Testing:
Intentionally collide the player car with enemy vehicles to check:
Side swipe collision detection when moving lanes.
Head-on collision detection.
Display of the crash image and game over screen.
Verify the game prompts for replay (Y/N).
Restart and Quit:
Press ‘Y’ on the game over screen to restart and check if the game resets correctly (score, speed, player position, vehicles).
Press ‘N’ to close the game.
Verify quitting via window close button or exit command.
Performance:
Check for smooth animation at 120 fps.
Ensure key inputs are responsive without lag.
● Screenshots (optional but recommended):
Code:
<img width="787" height="908" alt="image" src="https://github.com/user-attachments/assets/738db0e9-0a5d-44d1-bb84-bb5752d533a3" />
<img width="1195" height="937" alt="image" src="https://github.com/user-attachments/assets/a32004ae-cb5f-46c3-a69a-66e13f7207bb" />
<img width="1416" height="893" alt="image" src="https://github.com/user-attachments/assets/d24d8ec1-dafc-474b-8732-831144626191" />
<img width="1490" height="890" alt="image" src="https://github.com/user-attachments/assets/cdb6f06d-f27c-4a27-9f8b-ab042879da85" />
<img width="1887" height="798" alt="image" src="https://github.com/user-attachments/assets/07f71cb5-59de-48d7-a677-7086e4dd4110" />
<img width="1863" height="878" alt="image" src="https://github.com/user-attachments/assets/3dcd133c-951d-4976-b4d0-47719c53489b" />
<img width="1271" height="892" alt="image" src="https://github.com/user-attachments/assets/54e4f230-e1f9-4522-8d8d-0597d4b11619" />
<img width="1301" height="940" alt="image" src="https://github.com/user-attachments/assets/22ebf970-9e88-44c2-92b2-3d70200e3faf" />
<img width="1043" height="507" alt="image" src="https://github.com/user-attachments/assets/f70354b4-b2fb-4d3d-9e78-27950d57e5e1" />
Output:
<img width="645" height="678" alt="Screenshot 2025-11-22 115539" src="https://github.com/user-attachments/assets/c571b3a8-6c58-4881-a354-dceb36698f16" />









