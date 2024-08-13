![BANNER](https://github.com/user-attachments/assets/24ccb4bc-caf8-4947-9904-99a626b1ae88)

## Basic Overview

This is a simple Tic-Tac-Toe game but you play it using `real life board`.

![2024-08-1308-56-49-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/c27ffa58-82df-4ae6-a1a1-ee57fab270ce)

## How does this work 
It uses Arduino Uno and pygame python library. On Arduino we defined 9 pins as `INPUT` (it doesn't have to be 9, continue reading) and we just wait for digital one (1) then we update the string that represents the game. After that we send that string to the python. Python reads that information and construct the gameplay out of it.

We don't necceserally need to use 9 pins we can use something that people use when constructing chess boards, we can define notation, numbers and letters for every column and row so when we want to access some cell we just type the notation of that cell, for example: `a1`, `c3`, `b2` and check if there is digital one or digital zero. I didn't do that because 9 pins isn't that much, but if you want to build bigger boards you should do that.

String has 11 characters, 9 for the cells and 2 more for the game results, if player one wins last 2 characters change to `p1` and same for the second player (`p2`) or a draw (`dr`).
Python just reads what Arduino is printing in Serial Monitor and then uses that information.

Electric circuit is just cables from pins and cables from 3.3V on Arduino waiting for piece to connect them.

## How the board was created
Using CNC machine and some hand sanding after it. Models for CNC machine are made in `FreeCAD` software.

![iks](https://github.com/user-attachments/assets/05bae522-f92d-4b0a-8104-e5acb1dc0b8c)
![ox](https://github.com/user-attachments/assets/98a9fe30-0820-48b8-9e02-c5b603530af4)
![btm (3)](https://github.com/user-attachments/assets/c38c10f0-106f-42f9-a4a7-0c014dd1c6c9)

![gif2](https://github.com/user-attachments/assets/2e34fcd0-2c6a-4ad5-ae22-f526b73a7e59)

I wanted to use magnets but I didn't have enough materials so I ended up using thumbtacks as conductors. At the bottom of the pieces is aluminium foil that 
makes contact between pin and 3.3V.

## What are some improvements
 - Finding automatically on which port Arduino is;
 - Using Arduino Nano instead of Arduino Uno;
 - Adding more components like buzzers so it has sound effects;
 - Adding a bluetooth module so it doesn't need to be connect via use cable;
 - Improving the looks using magnets (this was the first idea actually but I didn't have enough material);
 - Adding led diods to indicate players turn;
 - Changing the appearance of a game;
 - ...and anything that your mind come up with;

## Just to be clear
  This is a side project and it was very fun building it, I always wanted to build something like this, but I will not work
  on this project again. I may build the better version of this like `Ultimate TicTacToe`.


## Libraries used
- `serial`
- `pygame`
- `time`
## Software used
- `Visual Studio Code`
- `Arduino IDE`
- `FreeCAD`
