#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include "structures.h"

//Initializing functions//

int random_int(int min, int max);
PADDLE CreatePaddle(float x, float y, float w, float h, float vP, bool r, bool l);
BALL CreateBall(float x, float y, float w, float h, float xV, float yV, float constant);
BLOCK CreateBlock(float x, float y, float w, float h, int resistance, bool death);
void UpdatePaddle(PADDLE *p);
void UpdateBall(BALL *b, PADDLE *p);
void UpdateBlock(BLOCK *br, BALL *ba);
void GameEvents(SDL_Event e);
void DrawText(int posX, int posY, SDL_Surface* sMessage, SDL_Surface* sScreen);
SDL_Surface* LoadSurface(char *imagePath);


#endif