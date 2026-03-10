package pieces;

import board.Board;

public class Knight extends Piece {
    public Knight(Color color) {
        super(PieceType.KNIGHT, color);
    }

    public boolean isValidMove(int startX, int startY, int endX, int endY, Board board) {
        return (Math.abs(endX - startX) == 2 && Math.abs(endY - startY) == 1) || (Math.abs(endX - startX) == 1 && Math.abs(endY - startY) == 2) && !board.isOccupiedByColor(endX, endY, this.getColor()); // Knight-like move
    }

    public char getSymbol() {
        return 'N';
    }
    
}
