#include "global.h"
#include "structures.h"
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <SDL2/SDL_ttf.h>
#include <SDL2/SDL_mixer.h>

//Global Variables//

int gameScreenW = 800;
int gameScreenH = 600;
int scenes = 0;
int lines = 6;
int columns = 6;
int intPoints = 0;
int mOption = 0;
int prefOption = 0;
int pLife = 3;
int stage = 1;
int toNLife = 0;
int howManyD;
char pPoints[30];
char cpLife[30];
char showS[30];
float block_w = 90;
float block_h = 30;
bool updateGS = true;
bool running = true;
bool creation = true;
bool right = false;
bool left = false;
bool start = false;
bool updateP = true;
bool updateL = true;
bool soundOn = true;
bool showRec = false;
Mix_Music *gameSound1;
SDL_Surface* gameScreen = NULL;
SDL_Surface* paddleImage = NULL;
SDL_Surface* ballImage = NULL;
SDL_Surface* blockR1Image = NULL;
SDL_Surface* blockR2Image = NULL;
SDL_Surface* blockR3Image = NULL;
SDL_Surface* blockR4Image = NULL;
SDL_Surface* gameBackground = NULL;
SDL_Surface *gameStage = NULL;
SDL_Surface *pMessage = NULL;
SDL_Surface *pSLife = NULL;
SDL_Surface *menuTitle = NULL;
SDL_Surface *menuPlay = NULL;
SDL_Surface *menuConf = NULL;
SDL_Surface *menuRecord = NULL;
SDL_Surface *menuCred = NULL;
SDL_Surface *menuQuit = NULL;
SDL_Surface *credTitle = NULL;
SDL_Surface *credProj = NULL;
SDL_Surface *credStud = NULL;
SDL_Surface *credProf = NULL;
SDL_Surface *credBack = NULL;
SDL_Surface *prefTitle = NULL;
SDL_Surface *prefBack = NULL;
SDL_Surface *prefSound = NULL; 
SDL_Surface *prefSOn = NULL;
SDL_Surface *wTitle = NULL;
SDL_Surface *lTitle = NULL;
SDL_Window* window = NULL;
SDL_Color pTextC = {255, 255, 255};
SDL_Color pTextMC = {255, 0, 0};
TTF_Font *pFont = NULL;
TTF_Font *pMFont = NULL;
TTF_Font *pMOFont = NULL;
PADDLE player;
BALL ball;
BLOCK bricks[6][6];
