package pieces;

import board.Board;

public class Rook extends Piece {
    public Rook(Color color) {
        super(PieceType.ROOK, color);
    }

    public boolean isValidMove(int startX, int startY, int endX, int endY, Board board) {
        return (startX == endX || startY == endY) && (endX != startX || endY != startY) && !board.isOccupiedByColor(endX, endY, this.getColor()); // Rook-like move and not the same square
    }

    public char getSymbol() {
        return 'R';
    }
    
}
