#include <stdio.h>
#include "global.h"
#include "structures.h"

int random_int(int min, int max)
{
   return min + rand() % (max+1 - min);
}

PADDLE CreatePaddle(float x, float y, float w, float h, float vP, bool r, bool l, int vida)
{
	PADDLE paddle;
	paddle.position.x = 0;
	paddle.position.y = 0;
	paddle.position.w = 512;
	paddle.position.h = 128;
	paddle.transform.x = x;
	paddle.transform.y = y;
	paddle.transform.w = w;
	paddle.transform.h = h;
	paddle.pV = vP;
	paddle.right = r;
	paddle.left = l;
	paddle.life = vida;
	return paddle;
}

BALL CreateBall(float x, float y, float w, float h, float xV, float yV, float constant)
{
	BALL b;
	b.position.x = 0;
	b.position.y = 0;
	b.position.w = 912;
	b.position.h = 913;
	b.transform.x = x;
	b.transform.y = y;
	b.transform.w = w;
	b.transform.h = h;
	b.vX = xV;
	b.vY = yV;
	b.c = constant;
	return b;
}

BLOCK CreateBlock(float x, float y, float w, float h, int resistance, bool death)
{
	BLOCK k;
	k.position.x = 0;
	k.position.y = 0;
	k.position.w = 400;
	k.position.h = 200;
	k.transform.x = x;
	k.transform.y = y;
	k.transform.w = w;
	k.transform.h = h;
	k.r = resistance;
	k.dead = death;
	return k;
}

void DrawText( int posX, int posY, SDL_Surface* sMessage, SDL_Surface* sScreen)
{
    SDL_Rect position;
    position.x = posX;
    position.y = posY;
    SDL_BlitSurface(sMessage, NULL, sScreen, &position);
}

void UpdatePaddle(PADDLE *p)
{
	if(p->right && p->left)
    {
        p->transform.x = p->transform.x;
    }
    else if(p->right && p->transform.x + p->transform.w < gameScreenW)
    {
        p->transform.x += p->pV;
    }
    else if(p->left && p->transform.x > 0)
    {
        p->transform.x -= p->pV;
    }
}

void UpdateBall(BALL *b, PADDLE *p)
{
	if(start)
	{
		b->transform.x += b->vX;
		b->transform.y += b->vY;
		if(b->transform.x <= 0 && b->vX < 0)
		{
			b->vX *= -1;
			b->transform.x += b->vX;
		}
		else if(b->transform.x >= gameScreenW - 30 && b->vX > 0)
		{
			b->vX *= -1;
			b->transform.x += b->vX;
		}
		if(b->transform.y <= 0 && b->vY < 0)
		{
			b->vY *= -1;
			b->transform.y += b->vY;
		}
		else if(b->transform.y >= gameScreenH && b->vY > 0)
		{
			p->life -= 1;
			pLife = p->life;
			updateL = true;
			if(p->life > 0)
			{
				start = false;
				p->transform.x = gameScreenW/2 - 50;
			}
			else
			{
				scenes = 6;
			}
		}
		if(b->transform.x + b->transform.w >= p->transform.x && b->transform.x < p->transform.x + p->transform.w/2 &&
			b->transform.y + b->transform.h >= p->transform.y && b->transform.y <= p->transform.y + p->transform.h &&
			b->vY > 0)
		{
			if(b->vX < 0)
			{
				b->vX *= b->c;
			}
			else
			{
				b->vX /= b->c;
			}
			b->vY *= -1;
			b->transform.y += b->vY;
		}
		else if(b->transform.x + b->transform.w >= p->transform.x + p->transform.w/2 && b->transform.x <= p->transform.x + p->transform.w &&
			b->transform.y + b->transform.h >= p->transform.y && b->transform.y <= p->transform.y + p->transform.h &&
			b->vY > 0)
		{
			if(b->vX > 0)
			{
				b->vX *= b->c;
			}
			else
			{
				b->vX /= b->c;
			}
			b->vY *= -1;
			b->transform.y += b->vY;
		}
	}
	else
	{
		b->transform.w = 15;
		b->transform.h = 15;
		b->transform.y = p->transform.y - p->transform.h;
		if(b->vY > 0)
		{
			b->vY *= -1;
		}
		b->transform.x = p->transform.x + p->transform.w/2 - b->transform.w/2;
	}
}

void UpdateBlock(BLOCK *br, BALL *ba)
{
	if(!br->dead)
	{
		if(ba->transform.x + ba->transform.w >= br->transform.x && ba->transform.x < br->transform.x + br->transform.w &&
		ba->transform.y + ba->transform.h >= br->transform.y && ba->transform.y <= br->transform.y + br->transform.h)
		{
			br->r -= 1;
			ba->vY *= -1;
			ba->transform.y += ba->vY;
			ba->transform.x += ba->vX;
		}
		if(br->r < 1)
		{
			intPoints += 100;
			toNLife += 100;
			updateP = true;
			if(toNLife >= 10000)
			{
				toNLife = 0;
				player.life += 1;
				pLife = player.life;
				updateL = true;
			}
			br->transform.x = -2000;
			br->dead = true;
			howManyD += 1;
		}
	}
}

void GameEvents(SDL_Event e)
{
	switch (e.type) 
	{
		case SDL_KEYDOWN:
	        switch(scenes)
	        {
	        	case 0:
		        	if(e.key.keysym.sym == SDLK_RIGHT) 
		            {
		                player.right = true;
		            }
		            if(e.key.keysym.sym == SDLK_LEFT) 
		            {
		                player.left = true;
		            }
		            if(e.key.keysym.sym == SDLK_SPACE)
		        	{
		        		if(!start)
		        		{
		        			start = true;
		        		}
		        	}
		        break;
		        case 1:
		        	if(e.key.keysym.sym == SDLK_UP)
		        	{
		        		if(mOption > 0)
		        		{
		        			mOption -= 1;
		        		}
		        	}
		        	else if(e.key.keysym.sym == SDLK_DOWN)
		        	{
		        		if(mOption < 4)
		        		{
		        			mOption += 1;
		        		}
		        	}
		        	else if(e.key.keysym.sym == SDLK_RETURN)
		        	{
		        		switch(mOption)
		        		{
		        			case 0:
		        				scenes = 0;
		        				ball.transform.y = player.transform.y;
		        				start = false;
		        				creation = true;
		        				updateL = true;
		        				showRec = false;
		        			break;
		        			case 1:
		        				showRec = true;
		        			break;
		        			case 2:
		        				scenes = 3;
		        				showRec = false;
		        			break;
		        			case 3:
		        				scenes = 4;
		        				showRec = false;
		        			break;
		        			case 4:
		        				running = false;
		        			break;
		        		}
		        	}
		        break;
		        case 3:
		        	if(e.key.keysym.sym == SDLK_UP)
		        	{
		        		if(prefOption > 0)
		        		{
		        			prefOption -= 1;
		        		}
		        	}
		        	else if(e.key.keysym.sym == SDLK_DOWN)
		        	{
		        		if(prefOption < 1)
		        		{
		        			prefOption += 1;
		        		}
		        	}
		        	else if(e.key.keysym.sym == SDLK_RETURN)
		        	{
		        		switch(prefOption)
		        		{
		        			case 0:
		        				soundOn = !soundOn;
		        				if(soundOn)
		        				{
		        					Mix_PlayMusic(gameSound1, -1);
		        				}
		        				else
		        				{
		        					Mix_PauseMusic();
		        				}
		        			break;
		        			case 1:
		        				scenes = 1;
		        			break;
		        		}
		        	}
		        break;
		        case 4:
		        	if(e.key.keysym.sym == SDLK_RETURN)
		        	{
		        		scenes = 1;
		        	}
		        break;
		        case 5:
		        	if(e.key.keysym.sym == SDLK_RETURN)
		        	{
		        		scenes = 1;
		        	}
		        break;
		        case 6:
		        	if(e.key.keysym.sym == SDLK_RETURN)
		        	{
		        		scenes = 1;
		        	}
		        break;
	        }
	        break;
	    case SDL_KEYUP:
	        switch(scenes)
	        {
	        	case 0:
		            if(e.key.keysym.sym == SDLK_RIGHT) 
		            {
		                player.right = false;
		            }
		            if(e.key.keysym.sym == SDLK_LEFT) 
		            {
		                player.left = false;
		            }
		        break;
	        }
	        break;
	}
}

SDL_Surface* LoadSurface(char *imagePath) 
{
    SDL_Surface* optimized = NULL;
    SDL_Surface* loaded = IMG_Load(imagePath);
    if(loaded == NULL)
    {
        printf("Erro ao carregar a imagem %s! SDL_image Error: %s\n", imagePath, IMG_GetError());
    }
    else 
    {
        optimized = SDL_ConvertSurface(loaded, gameScreen->format, 0);
        if(optimized == NULL)
        {
            printf("Erro ao otimizar a imagem %s! SDL Error: %s\n", imagePath, SDL_GetError());
        }
        SDL_FreeSurface(loaded);
    }
    return optimized;
}
