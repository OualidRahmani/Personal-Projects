package pieces;

import board.Board;

public class Pawn extends Piece {
    public Pawn(Color color) {
        super(PieceType.PAWN, color);
    }

    public boolean isValidMove(int startX, int startY, int endX, int endY, Board board) {
        int direction = (this.getColor() == Color.WHITE) ? -1 : 1;
        int startRow = (this.getColor() == Color.WHITE) ? 6 : 1;
        Color enemyColor = (this.getColor() == Color.WHITE) ? Color.BLACK : Color.WHITE;

        if (endX == startX + direction && startY == endY && !board.getSquare(endX, endY).isOccupied()) {
            return true;
        }

        if (startX == startRow && endX == startX + (2 * direction) && startY == endY 
            && !board.getSquare(endX, endY).isOccupied() 
            && !board.getSquare(startX + direction, startY).isOccupied()) {
            return true;
        }

        return (endX == startX + direction && Math.abs(endY - startY) == 1 
            && board.isOccupiedByColor(endX, endY, enemyColor));
    }

    public char getSymbol() {
        return 'P';
    }
}