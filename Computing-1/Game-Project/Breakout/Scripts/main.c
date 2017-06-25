/*
 * game.c
 *
 * Programmed by Breno Rocha. 
 * Start date: 30/05/2017.
 * End date: 20/06/2017.
 *
 */

//Libraries//
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <SDL2/SDL_ttf.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "global.h"
#include "structures.h"
#include "functions.h"

//Initializing Application Roots
bool Begin();
void Creator();
void Close();
bool LoadImages();
bool LoadFonts();
SDL_Surface* LoadSurface(char *path);
//Scenes// 
void SceneManager();
void GameScene();
void MenuScene();

//Main Function//
int main(int argc, char* args[]) 
{
    if(!Begin())
    {
        printf("Inicializacao Falhou!\n");
    }
    else 
    {
    	scenes = 1;
        Creator();
        if(!LoadImages()) 
        {
            printf( "Falha no carregamento de imagem!\n" );
        }
        if(!LoadFonts())
        {
        	printf( "Falha no carregamento de fonte!\n");
        }
        while(running) 
        {
            
            SceneManager();
        }
    }
    Close();
    return 0;
}

//Scene Manager//
void SceneManager()
{
    SDL_Event event;
    while(SDL_PollEvent(&event)!= 0) 
    {
        switch (event.type) 
        {
            case SDL_QUIT:
                running = false;
            break;
        }
        switch(scenes)
        {
        	case 0:
        		GameEvents(event);
        	break;
        }
    }
    switch(scenes)
    {
        case 0:
            GameScene();
            break;
        case 1:
            MenuScene();
            break;
        default:
            running = false;
            break;
    }
    SDL_UpdateWindowSurface(window);            
    SDL_Delay(5);
}

//Scenes//
void GameScene()
{
    UpdatePaddle(&player);
    UpdateBall(&ball, &player);
    for(int i = 0; i < columns; i++)
    {
        for(int j = 0; j < lines; j++)
        {
            UpdateBlock(&bricks[i][j], &ball);
        }
    }
    if(SDL_ShowCursor(SDL_QUERY))
    {
        SDL_ShowCursor(SDL_DISABLE);
    }
    if(SDL_BlitScaled(gameBackground, NULL, gameScreen, NULL) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
    if(SDL_BlitScaled(paddleImage, &player.position, gameScreen, &player.transform) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
    if(SDL_BlitScaled(ballImage, &ball.position, gameScreen, &ball.transform) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
    for(int i = 0; i < columns; i++)
    {
        for(int j = 0; j < lines; j++)
        {
            if(bricks[i][j].r == 1)
            {
                if(SDL_BlitScaled(blockR1Image, &bricks[i][j].position, gameScreen, &bricks[i][j].transform) < 0)
                {
                    printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
                    running = false;
                }
            }
            else if(bricks[i][j].r == 2)
            {
                if(SDL_BlitScaled(blockR2Image, &bricks[i][j].position, gameScreen, &bricks[i][j].transform) < 0)
                {
                    printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
                    running = false;
                }
            }
            else if(bricks[i][j].r == 3)
            {
                if(SDL_BlitScaled(blockR3Image, &bricks[i][j].position, gameScreen, &bricks[i][j].transform) < 0)
                {
                    printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
                    running = false;
                }
            }
            else if(bricks[i][j].r == 4)
            {
                if(SDL_BlitScaled(blockR4Image, &bricks[i][j].position, gameScreen, &bricks[i][j].transform) < 0)
                {
                    printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
                    running = false;
                }
            }
        }
    }
    if(updateP)
    {
    	snprintf(pPoints, sizeof(pPoints), "Pontos: %d", intPoints);
    	updateP = false;
    	pMessage = TTF_RenderText_Solid(pFont, pPoints, pTextC);
    }
    DrawText( 0, 575, pMessage, gameScreen );
}

void MenuScene()
{
    if(!SDL_ShowCursor(SDL_QUERY))
    {
        SDL_ShowCursor(SDL_ENABLE);
    }
    
    if(SDL_BlitScaled(gameBackground, NULL, gameScreen, NULL) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
}

//Application Roots//
bool LoadFonts()
{
	bool noBugs = true;
	pFont = TTF_OpenFont("./lazy.ttf", 28 );
    if(pFont == NULL )
    {
		printf("Falha no carregamento da fonte: %s \n", TTF_GetError());
		noBugs = false;
    }
    return noBugs;
}

bool LoadImages()
{
    bool noBugs = true;
    paddleImage = LoadSurface("Images/paddle.png");
    ballImage = LoadSurface("Images/ball.png");
    gameBackground = LoadSurface("Images/background.png");
    blockR1Image = LoadSurface("Images/BlockR1.png");
    blockR2Image = LoadSurface("Images/BlockR2.png");
    blockR3Image = LoadSurface("Images/BlockR3.png");
    blockR4Image = LoadSurface("Images/BlockR4.png");
    if(paddleImage == NULL || gameBackground == NULL || ballImage == NULL || blockR1Image == NULL || blockR2Image == NULL || blockR3Image == NULL || blockR4Image == NULL) 
    {
        printf("Falha no carregamento da imagem!\n" );
        noBugs = false;
    }
    SDL_SetColorKey(paddleImage, true, SDL_MapRGB(paddleImage->format, 0, 0, 255));
    SDL_SetColorKey(ballImage, true, SDL_MapRGB(paddleImage->format, 0, 0, 255));
    return noBugs;
}

bool Begin() 
{
    SDL_Init(SDL_INIT_VIDEO);
    bool noBugs = true;
    srand(time(NULL));
    if(SDL_Init(SDL_INIT_VIDEO) < 0)
    {
        printf("Falha na inicializacao do SDL! SDL_Error: %s\n", SDL_GetError());
        noBugs = false;
    }
    else if(TTF_Init() < 0)
    {
    	printf("Falha na inicializacao da FONTE! SDL_Error: %s\n", SDL_GetError());
        noBugs = false;
    }
    else
    {
        window = SDL_CreateWindow("Breakout", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, gameScreenW, gameScreenH, SDL_WINDOW_SHOWN);
        if(window == NULL)
        {
            printf("A janela falhou em ser criada! SDL_Error: %s\n", SDL_GetError());
            noBugs = false;
        }
        else 
        {
            int imageFlags = IMG_INIT_PNG;
            if(!(IMG_Init(imageFlags) & imageFlags)) 
            {
                printf("SDL_image nao pode ser inicializado! SDL_image Error: %s\n", IMG_GetError());
                noBugs = false;
            }
            else 
            {
                gameScreen = SDL_GetWindowSurface(window);
                if (gameScreen == NULL) 
                {
                    printf("A janela nao pode receber a tela do jogo! SDL_Error: %s\n", SDL_GetError());
                    noBugs = false;
                }
            }
        }
    }
    return noBugs;
}

void Creator()
{
    switch(scenes)
    {
        case 0:
            player = CreatePaddle(gameScreenW/2 - 50, (gameScreenH - gameScreenH/10) - 15,100,30, 3, false, false);
            ball = CreateBall(gameScreenW/2 - 15, gameScreenH/2 - 15, 30, 30, 2, 2, 1.0001);
            for(int i = 0; i < columns; i++)
            {
                for(int j = 0; j < lines; j++)
                {
                    if(i < columns/2)
                    {
                        bricks[i][j] = CreateBlock(((gameScreenW/2) + (gameScreenW/35 + block_w)*i), (gameScreenH/50) + (block_h * j) + (gameScreenH/50 * j), block_w, block_h, random_int(1,4), false);
                    }
                    else
                    {
                        bricks[i][j] = CreateBlock((gameScreenW/2) - ((gameScreenW/35 + block_w)*(columns - i)), (gameScreenH/50) + (block_h * j) + (gameScreenH/50 * j), block_w, block_h, random_int(1,4), false);
                    }
                }
            }
        break;
    }
}

void Close()
{
    SDL_FreeSurface(gameBackground);
    gameBackground = NULL;
    SDL_FreeSurface(paddleImage);
    paddleImage = NULL;
    SDL_FreeSurface(ballImage);
    ballImage = NULL;
    SDL_FreeSurface(blockR1Image);
    blockR1Image = NULL;
    SDL_FreeSurface(pMessage);
    TTF_CloseFont(pFont);
    pFont = NULL;
    TTF_Quit();
    SDL_DestroyWindow(window);
    window = NULL;
    IMG_Quit();
    SDL_Quit();
}