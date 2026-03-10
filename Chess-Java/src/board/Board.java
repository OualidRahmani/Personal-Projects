package board;

import pieces.Piece;

public class Board {
    private Square[][] _board;

    public Board() {
        _board = new Square[8][8];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                _board[i][j] = new Square();
            }
        }
    }

    public Square getSquare(int x, int y) {
        return _board[x][y];
    }

    public void setSquare(int x, int y, Square square) {
        _board[x][y] = square;
    }

    public void printBoard() {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (!_board[i][j].isOccupied()) {
                    System.out.print("- ");
                } else {
                    System.out.print(_board[i][j].getPiece().getSymbol() + " ");
                }
            }
            System.out.println();
        }
    }

    public Boolean isOccupiedByColor(int x, int y, Piece.Color color) {
        if (_board[x][y].isOccupied()) {
            return _board[x][y].getPiece().getColor() == color;
        }
        return false;
    }
}
