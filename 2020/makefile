CC = g++
CFLAGS = -std=c++11 -pedantic -Wall
DAY = 17
OBJECTS = $(DAY).o
APP_NAME = aoc

all: $(APP_NAME)
	rm -f *.o

$(DAY).o: $(DAY).cpp
	$(CC) $(CFLAGS) -c $(DAY).cpp

$(APP_NAME): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(APP_NAME)

clean:
	rm -f *.o $(APP_NAME)
