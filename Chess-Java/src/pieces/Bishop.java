package pieces;

import board.Board;

public class Bishop extends Piece {
    public Bishop(Color color) {
        super(PieceType.BISHOP, color);
    }

    public boolean isValidMove(int startX, int startY, int endX, int endY, Board board) {
        int dx = Math.abs(endX - startX);
        int dy = Math.abs(endY - startY);
        return dx == dy && (endX != startX || endY != startY) && !board.isOccupiedByColor(endX, endY, this.getColor()); // Bishop-like move and not the same square
    }

    public char getSymbol() {
        return 'B';
    }
}
