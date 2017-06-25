#include "global.h"
#include "structures.h"
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <SDL2/SDL_ttf.h>
//Global Variables//

int gameScreenW = 800;
int gameScreenH = 600;
int scenes = 0;
int lines = 6;
int columns = 6;
int intPoints = 0;
char pPoints[30];
float block_w = 90;
float block_h = 30;
bool running = true;
bool creation = true;
bool right = false;
bool left = false;
bool updateP = true;
SDL_Surface* gameScreen = NULL;
SDL_Surface* paddleImage = NULL;
SDL_Surface* ballImage = NULL;
SDL_Surface* blockR1Image = NULL;
SDL_Surface* blockR2Image = NULL;
SDL_Surface* blockR3Image = NULL;
SDL_Surface* blockR4Image = NULL;
SDL_Surface* gameBackground = NULL;
SDL_Surface *pMessage = NULL;
SDL_Window* window = NULL;
SDL_Color pTextC = {255, 255, 255};
TTF_Font *pFont = NULL;
PADDLE player;
BALL ball;
BLOCK bricks[6][6];
