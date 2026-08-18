SRC = kinematics.c
EXE = run
CC = gcc
FLAGS = -lm

all: $(EXE)

$(EXE): $(SRC)
	$(CC) $(SRC) -o $(EXE) $(FLAGS)


.PHONY: clean

clean:
	rm -f ./$(EXE)