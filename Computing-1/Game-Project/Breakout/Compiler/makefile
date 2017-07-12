CC=gcc
CFLAGS=-g -Wall -pedantic -D_REENTRANT -lm
IMAGE_FLAGS=-lSDL2_image
MIXER_FLAGS=-lSDL2_mixer
TEXT_FLAGS=-lSDL2_ttf
LFLAGS=`sdl2-config --cflags --libs`
SFLAGS=-lSDL2
SOURCES=main.c global.c functions.c 
OBJECTS=main.o global.o functions.o
MOVE=mv Breakout ../
MOVE1=mv main.o ../Objects
MOVE2=mv global.o ../Objects
MOVE3=mv functions.o ../Objects
BINARIES=Breakout

all: $(BINARIES)

Breakout: main.o global.o functions.o 
	$(CC) -o Breakout main.o global.o functions.o $(CFLAGS) $(SFLAGS) $(LFLAGS) $(IMAGE_FLAGS) $(MIXER_FLAGS) $(TEXT_FLAGS)
	$(MOVE)
	$(MOVE1)
	$(MOVE2)
	$(MOVE3)
main.o: ../Scripts/main.c
	$(CC) -c ../Scripts/main.c $(CFLAGS) $(SFLAGS) $(LFLAGS) $(IMAGE_FLAGS) $(MIXER_FLAGS) $(TEXT_FLAGS)	
functions.o: ../Scripts/functions.c
	$(CC) -c ../Scripts/functions.c $(CFLAGS) $(SFLAGS) $(LFLAGS) $(IMAGE_FLAGS) $(MIXER_FLAGS) $(TEXT_FLAGS)
global.o: ../Scripts/global.c
	$(CC) -c ../Scripts/global.c $(CFLAGS) $(SFLAGS) $(LFLAGS) $(IMAGE_FLAGS) $(MIXER_FLAGS) $(TEXT_FLAGS)
clean:
	rm -rf *.o *.exe *.bak *.c~ $(BINARIES) core a.out
limpa:
	del *.o *.exe *.bak *.c~ $(BINARIES) core