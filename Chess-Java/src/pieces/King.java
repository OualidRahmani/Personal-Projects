package pieces;

import board.Board;

public class King extends Piece {

    public King(Color color) {
        super(PieceType.KING, color);
    }

    public boolean isValidMove(int startX, int startY, int endX, int endY, Board board) {
            int dx = Math.abs(endX - startX);
            int dy = Math.abs(endY - startY);
    
            return ((dx <= 1 && dy <= 1) && !(dx == 0 && dy == 0)) && !board.isOccupiedByColor(endX, endY, this.getColor());
                
    }

    public char getSymbol() {
        return 'K';
    }
}
