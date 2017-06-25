#ifndef GLOBAIS_H
#define GLOBAIS_H
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <SDL2/SDL_ttf.h>
#include "structures.h"

extern int gameScreenW;
extern int gameScreenH;
extern int scenes;
extern int lines;
extern int columns;
extern int intPoints;
extern char pPoints[30];
extern float block_w;
extern float block_h;
extern bool running;
extern bool creation;
extern bool right;
extern bool left;
extern bool updateP;
extern SDL_Surface* gameScreen;
extern SDL_Surface* paddleImage;
extern SDL_Surface* ballImage;
extern SDL_Surface* blockR1Image;
extern SDL_Surface* blockR2Image;
extern SDL_Surface* blockR3Image;
extern SDL_Surface* blockR4Image;
extern SDL_Surface* gameBackground;
extern SDL_Surface *pMessage;
extern SDL_Window* window;
extern TTF_Font *pFont;
extern SDL_Color pTextC;
extern PADDLE player;
extern BALL ball;
extern BLOCK bricks[6][6];

#endif