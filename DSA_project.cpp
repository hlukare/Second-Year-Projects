#include <graphics.h>
#include <conio.h>
#include <iostream>
#include <vector>
#include <algorithm>

const int BOARD_SIZE = 8;
const int CELL_SIZE = 80;
const int DELAY = 1000;

int board[BOARD_SIZE][BOARD_SIZE];
int currentRow = 0;
int currentCol = 0;
int moveNumber = 1;

int rowMove[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int colMove[8] = {1, 2, 2, 1, -1, -2, -2, -1};

int cellColors[BOARD_SIZE][BOARD_SIZE];

void initializeColors() {
    for (int i = 0; i < BOARD_SIZE; i++) {
        for (int j = 0; j < BOARD_SIZE; j++) {
            cellColors[i][j] = WHITE;
        }
    }
}

void drawBoard() {
    for (int i = 0; i < BOARD_SIZE; i++) {
        for (int j = 0; j < BOARD_SIZE; j++) {
            setcolor(cellColors[i][j]);
            rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE);
            int value = board[i][j];
            if (value > 0) {
                char str[2];
                str[0] = '0' + value;
                str[1] = '\0';
                setcolor(BLACK);
                outtextxy(j * CELL_SIZE + CELL_SIZE / 2, i * CELL_SIZE + CELL_SIZE / 2, str);
            }
        }
    }
}

bool canMove(int row, int col) {
    return row >= 0 && col >= 0 && row < BOARD_SIZE && col < BOARD_SIZE && board[row][col] == 0;
}

int countMoves(int row, int col) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        int nextRow = row + rowMove[i];
        int nextCol = col + colMove[i];
        if (canMove(nextRow, nextCol)) {
            count++;
        }
    }
    return count;
}

void makeNextMove() {
    std::vector<std::pair<int, int>> possibleMoves;

    for (int i = 0; i < 8; i++) {
        int nextRow = currentRow + rowMove[i];
        int nextCol = currentCol + colMove[i];

        if (canMove(nextRow, nextCol)) {
            int count = countMoves(nextRow, nextCol);
            possibleMoves.push_back(std::make_pair(count, i));
        }
    }

    if (possibleMoves.empty()) {
        std::cerr << "No solution found." << std::endl;
        return;
    }

    std::sort(possibleMoves.begin(), possibleMoves.end());

    int nextMoveIndex = possibleMoves.front().second;
    int nextRow = currentRow + rowMove[nextMoveIndex];
    int nextCol = currentCol + colMove[nextMoveIndex];

    moveNumber++;
    board[nextRow][nextCol] = moveNumber;
    currentRow = nextRow;
    currentCol = nextCol;
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    initializeColors();
    board[currentRow][currentCol] = moveNumber;

    while (!kbhit()) {
        if (moveNumber == BOARD_SIZE * BOARD_SIZE) {
            drawBoard();
            std::cout << "Knight's Tour Completed in " << (moveNumber - 1) << " steps!" << std::endl;
            break;
        }

        makeNextMove();
        drawBoard();
        delay(DELAY);
    }

    closegraph();
    return 0;
}
