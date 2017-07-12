#ifndef GLOBAIS_H
#define GLOBAIS_H
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <SDL2/SDL_ttf.h>
#include "structures.h"
#include <SDL2/SDL_mixer.h>

extern int gameScreenW;
extern int gameScreenH;
extern int scenes;
extern int lines;
extern int columns;
extern int intPoints;
extern int mOption;
extern int prefOption;
extern int pLife;
extern int stage;
extern int howManyD;
extern int toNLife;
extern char pPoints[30];
extern char cpLife[30];
extern char showS[30];
extern float block_w;
extern float block_h;
extern bool running;
extern bool creation;
extern bool right;
extern bool updateGS;
extern bool left;
extern bool start;
extern bool updateP;
extern bool updateL;
extern bool soundOn;
extern bool showRec;
extern Mix_Music *gameSound1;
extern SDL_Surface* gameScreen;
extern SDL_Surface* paddleImage;
extern SDL_Surface* ballImage;
extern SDL_Surface* blockR1Image;
extern SDL_Surface* blockR2Image;
extern SDL_Surface* blockR3Image;
extern SDL_Surface* blockR4Image;
extern SDL_Surface* gameBackground;
extern SDL_Surface *gameStage;
extern SDL_Surface *pMessage;
extern SDL_Surface *pSLife;
extern SDL_Surface *menuTitle;
extern SDL_Surface *menuPlay;
extern SDL_Surface *menuConf;
extern SDL_Surface *menuRecord;
extern SDL_Surface *menuCred;
extern SDL_Surface *menuQuit;
extern SDL_Surface *credTitle;
extern SDL_Surface *credProj;
extern SDL_Surface *credStud;
extern SDL_Surface *credProf;
extern SDL_Surface *credBack;
extern SDL_Surface *prefTitle;
extern SDL_Surface *prefBack;
extern SDL_Surface *prefSound;
extern SDL_Surface *prefSOn;
extern SDL_Surface *wTitle;
extern SDL_Surface *lTitle;
extern SDL_Window* window;
extern TTF_Font *pFont;
extern TTF_Font *pMFont;
extern TTF_Font *pMOFont;
extern SDL_Color pTextMC;
extern SDL_Color pTextC;
extern PADDLE player;
extern BALL ball;
extern BLOCK bricks[6][6];

#endif
