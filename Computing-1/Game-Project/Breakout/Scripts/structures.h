#ifndef STRUCTURES_H
#define STRUCTURES_H

#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
typedef int bool;
#define true 1
#define false 0

typedef struct _PADDLE
{
	SDL_Rect position;
	SDL_Rect transform;
	float pV;
	bool right;
	bool left;
	int life;
} PADDLE;

typedef struct _BALL
{
	SDL_Rect position;
	SDL_Rect transform;
	float vX;
	float vY;
	float c;
} BALL;

typedef struct _BLOCK
{
	SDL_Rect position;
	SDL_Rect transform;
	int r;
	bool dead;
} BLOCK;

#endif