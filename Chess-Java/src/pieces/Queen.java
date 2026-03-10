package pieces;

import board.Board;

public class Queen extends Piece {
    public Queen(Color color) {
        super(PieceType.QUEEN, color);
    }

    public boolean isValidMove(int startX, int startY, int endX, int endY, Board board) {
        int dx = Math.abs(endX - startX);
        int dy = Math.abs(endY - startY);
        return (startX == endX || startY == endY || dx == dy) && (endX != startX || endY != startY) && !board.isOccupiedByColor(endX, endY, this.getColor()); // Queen-like move and not the same square
    }

    public char getSymbol() {
        return 'Q';
    }
}
