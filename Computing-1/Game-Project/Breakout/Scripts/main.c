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
#include <SDL2/SDL_mixer.h>
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
bool LoadAudio();
SDL_Surface* LoadSurface(char *path);
//Scenes// 
void SceneManager();
void GameScene();
void MenuScene();
void CredScene();
void PrefScene();
void WinScene();
void LoseScene();
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
    	intPoints = 0;
    	pPoints[0] = '\0';
        Creator();
        if(!LoadImages()) 
        {
            printf( "Falha no carregamento de imagem!\n" );
        }
        if(!LoadFonts())
        {
        	printf( "Falha no carregamento de fonte!\n");
        }
        if(!LoadAudio())
        {
        	printf( "Falha no carregamento de audio!\n");
        }
       	Mix_PlayMusic(gameSound1, -1);
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
    if(creation)
    {
    	Creator();
    	creation = false;
    }
    while(SDL_PollEvent(&event)!= 0) 
    {
        switch (event.type) 
        {
            case SDL_QUIT:
                running = false;
            break;
        }
		GameEvents(event);	
    }
    switch(scenes)
    {
        case 0:
            GameScene();
            break;
        case 1:
            MenuScene();
            break;
        case 3:
        	PrefScene();
        	break;
        case 4:
            CredScene();
            break;
        case 5:
        	WinScene();
        	break;
        case 6:
        	LoseScene();
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
    if(updateP)
    {
    	snprintf(pPoints, sizeof(pPoints), "Pontos: %d", intPoints);
    	updateP = false;
    	pMessage = TTF_RenderText_Solid(pFont, pPoints, pTextC);
    }
    if(updateGS)
    {
    	snprintf(showS, sizeof(showS), "Fase: %d", stage);
    	updateGS = false;
    	gameStage = TTF_RenderText_Solid(pMFont, showS, pTextMC);
    }
    if(updateL)
    {
    	snprintf(cpLife, sizeof(cpLife), "Vidas: %d", pLife);
    	updateL = false;
    	pSLife = TTF_RenderText_Solid(pFont, cpLife, pTextC);
    }
    DrawText(25, 565, pMessage, gameScreen);
    DrawText(635, 565, pSLife, gameScreen);
    DrawText(280, 10, gameStage, gameScreen);
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
    if(howManyD == columns*lines)
    {
    	start = false;
    	stage += 1;
    	for(int i = 0; i < columns; i++)
        {
            for(int j = 0; j < lines; j++)
            {
                if(i < columns/2)
                {
                    bricks[i][j] = CreateBlock(((gameScreenW/2) + (gameScreenW/35 + block_w)*i), (gameScreenH/7) + (block_h * j) + (gameScreenH/50 * j), block_w, block_h, stage, false);
                }
                else
                {
                    bricks[i][j] = CreateBlock((gameScreenW/2) - ((gameScreenW/35 + block_w)*(columns - i)), (gameScreenH/7) + (block_h * j) + (gameScreenH/50 * j), block_w, block_h, stage, false);
                }
            }
        }
    	updateGS = true;
    	howManyD = 0;
    }
    if(stage > 4)
    {
    	scenes = 5;
    }
}

void MenuScene()
{
   	if(SDL_ShowCursor(SDL_QUERY))
    {
        SDL_ShowCursor(SDL_DISABLE);
    }
    
    if(SDL_BlitScaled(gameBackground, NULL, gameScreen, NULL) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }

    menuTitle = TTF_RenderText_Solid(pMFont, "Breakout", pTextMC);
    switch(mOption)
    {
    	case 0:
    		menuPlay = TTF_RenderText_Solid(pMOFont, "Jogar", pTextC);
		    menuConf = TTF_RenderText_Solid(pMOFont, "Preferencias", pTextMC);
		    menuRecord = TTF_RenderText_Solid(pMOFont, "Recordes", pTextMC);
		    menuCred = TTF_RenderText_Solid(pMOFont, "Creditos", pTextMC);
		    menuQuit = TTF_RenderText_Solid(pMOFont, "Sair", pTextMC);
    	break;
    	case 1:
    		menuPlay = TTF_RenderText_Solid(pMOFont, "Jogar", pTextMC);
		    menuConf = TTF_RenderText_Solid(pMOFont, "Preferencias", pTextMC);
		    menuRecord = TTF_RenderText_Solid(pMOFont, "Recordes", pTextC);
		    menuCred = TTF_RenderText_Solid(pMOFont, "Creditos", pTextMC);
		    menuQuit = TTF_RenderText_Solid(pMOFont, "Sair", pTextMC);
    	break;
    	case 2:
    		menuPlay = TTF_RenderText_Solid(pMOFont, "Jogar", pTextMC);
		    menuConf = TTF_RenderText_Solid(pMOFont, "Preferencias", pTextC);
		    menuCred = TTF_RenderText_Solid(pMOFont, "Creditos", pTextMC);
		    menuRecord = TTF_RenderText_Solid(pMOFont, "Recordes", pTextMC);
		    menuQuit = TTF_RenderText_Solid(pMOFont, "Sair", pTextMC);
    	break;
    	case 3: 
    		menuPlay = TTF_RenderText_Solid(pMOFont, "Jogar", pTextMC);
		    menuConf = TTF_RenderText_Solid(pMOFont, "Preferencias", pTextMC);
		    menuCred = TTF_RenderText_Solid(pMOFont, "Creditos", pTextC);
		    menuRecord = TTF_RenderText_Solid(pMOFont, "Recordes", pTextMC);
		    menuQuit = TTF_RenderText_Solid(pMOFont, "Sair", pTextMC);
    	break;
    	case 4:
    		menuPlay = TTF_RenderText_Solid(pMOFont, "Jogar", pTextMC);
		    menuConf = TTF_RenderText_Solid(pMOFont, "Preferencias", pTextMC);
		    menuCred = TTF_RenderText_Solid(pMOFont, "Creditos", pTextMC);
		    menuRecord = TTF_RenderText_Solid(pMOFont, "Recordes", pTextMC);
		    menuQuit = TTF_RenderText_Solid(pMOFont, "Sair", pTextC);
    	break;
    }
    DrawText(215, 100, menuTitle, gameScreen );
    DrawText(325, 300, menuPlay, gameScreen );
    DrawText(285, 350, menuRecord, gameScreen );
    DrawText(230, 400, menuConf, gameScreen );
    DrawText(285, 450, menuCred, gameScreen );
    DrawText(350, 500, menuQuit, gameScreen );
}

void CredScene()
{
	if(SDL_BlitScaled(gameBackground, NULL, gameScreen, NULL) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
	credTitle = TTF_RenderText_Solid(pMOFont, "UFRJ", pTextMC);
	credProj = TTF_RenderText_Solid(pFont, "Computacao 1: Projeto de Jogos", pTextMC);
	credStud = TTF_RenderText_Solid(pFont, "Alunos: Arthur Guilherme e Breno Rocha" , pTextMC);
	credProf = TTF_RenderText_Solid(pFont, "Professor: Adriano Cruz", pTextMC);
	credBack = TTF_RenderText_Solid(pFont, "Voltar", pTextC);
	DrawText(325, 100, credTitle, gameScreen );
	DrawText(150, 300, credProf, gameScreen );
    DrawText(100, 350, credProj, gameScreen );
    DrawText(25, 400, credStud, gameScreen );
    DrawText(330, 550, credBack, gameScreen );
}

void PrefScene()
{
	if(SDL_BlitScaled(gameBackground, NULL, gameScreen, NULL) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
    prefTitle = TTF_RenderText_Solid(pMOFont, "Preferencias", pTextMC);
    switch(prefOption)
    {
    	case 0:
    		prefSound = TTF_RenderText_Solid(pFont, "Som:", pTextC);
    		if(soundOn)
    		{
    			prefSOn = TTF_RenderText_Solid(pFont, "Ligado", pTextC);
    		}
    		else
    		{
    			prefSOn = TTF_RenderText_Solid(pFont, "Desligado", pTextC);
    		}
    		prefBack = TTF_RenderText_Solid(pFont, "Voltar", pTextMC);
    	break;
    	case 1:
    		prefSound = TTF_RenderText_Solid(pFont, "Som:", pTextMC);
    		if(soundOn)
    		{
    			prefSOn = TTF_RenderText_Solid(pFont, "Ligado", pTextMC);
    		}
    		else
    		{
    			prefSOn = TTF_RenderText_Solid(pFont, "Desligado", pTextMC);
    		}
    		prefBack = TTF_RenderText_Solid(pFont, "Voltar", pTextC);
    	break;
    }
    DrawText(220, 50, prefTitle, gameScreen );
    DrawText(295, 200, prefSound, gameScreen );
    DrawText(385, 200, prefSOn, gameScreen );
    DrawText(335, 550, prefBack, gameScreen );
}

void WinScene()
{
	if(SDL_BlitScaled(gameBackground, NULL, gameScreen, NULL) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
    wTitle = TTF_RenderText_Solid(pMFont, "Voce Venceu!", pTextMC);
    credBack = TTF_RenderText_Solid(pFont, "Voltar", pTextC);
	DrawText(150, 100, wTitle, gameScreen);
    DrawText(330, 550, credBack, gameScreen);
}

void LoseScene()
{
	if(SDL_BlitScaled(gameBackground, NULL, gameScreen, NULL) < 0)
    {
       printf( "SDL could not blit! SDL Error: %s\n", SDL_GetError() );
       running = false;
    }
    lTitle = TTF_RenderText_Solid(pMFont, "Voce Perdeu!", pTextMC);
   	credProj = TTF_RenderText_Solid(pMFont, "Tente Novamente!", pTextMC);
    credBack = TTF_RenderText_Solid(pFont, "Voltar", pTextC);
    DrawText(150, 100, lTitle, gameScreen );
    DrawText(25, 280, credProj, gameScreen );
    DrawText(330, 550, credBack, gameScreen );
}

//Application Roots//

bool LoadAudio()
{
	bool noBugs = true;
	Mix_OpenAudio( 44100, MIX_DEFAULT_FORMAT, 2, 4096);
	Mix_AllocateChannels(16);
	gameSound1 = Mix_LoadMUS("Sounds/341580__kimp10__dolphin-ride-short.wav");
	if (!gameSound1)
	{
        printf("Wav: SDL error=%s\n", SDL_GetError());
        return false;
    }
    return noBugs;
}

bool LoadFonts()
{
	bool noBugs = true;
	pFont = TTF_OpenFont("Fonts/edgeracerhalf.ttf", 28 );
	pMFont = TTF_OpenFont("Fonts/edgeracerchrome.ttf", 72 );
	pMOFont = TTF_OpenFont("Fonts/edgeracerhalf.ttf", 40 );
    if(pFont == NULL || pMFont == NULL || pMOFont == NULL)
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
        	intPoints = 0;
        	updateP = true;
            player = CreatePaddle(gameScreenW/2 - 50, (gameScreenH - gameScreenH/10) - 15,100,30, 1.5, false, false, 3);
            ball = CreateBall(gameScreenW/2 - 15, gameScreenH/2 - 15, 30, 30, 2, 2, 1.0001);
            howManyD = 0;
            stage = 1;
            howManyD = 0;
            for(int i = 0; i < columns; i++)
            {
                for(int j = 0; j < lines; j++)
                {
                    if(i < columns/2)
                    {
                        bricks[i][j] = CreateBlock(((gameScreenW/2) + (gameScreenW/35 + block_w)*i), (gameScreenH/7) + (block_h * j) + (gameScreenH/50 * j), block_w, block_h, stage, false);
                    }
                    else
                    {
                        bricks[i][j] = CreateBlock((gameScreenW/2) - ((gameScreenW/35 + block_w)*(columns - i)), (gameScreenH/7) + (block_h * j) + (gameScreenH/50 * j), block_w, block_h, stage, false);
                    }
                }
            }
            pLife = player.life;
            updateL = true;
            howManyD = 0;

        break;
        case 1:
			
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
    Mix_CloseAudio();
    IMG_Quit();
    SDL_Quit();
}