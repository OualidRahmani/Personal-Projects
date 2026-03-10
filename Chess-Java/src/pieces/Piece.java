package pieces;

import board.Board;

public abstract class Piece {
    public enum PieceType {
        PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING
    }
    public enum Color {
        WHITE, BLACK
    }

    private PieceType _type;
    private Color _color;

    protected Piece(PieceType type, Color color) {
        _type = type;
        _color = color;
    }

    public PieceType getType() {
        return _type;
    }

    public Color getColor() {
        return _color;
    }

    public abstract boolean isValidMove(int startX, int startY, int endX, int endY, Board board);

    public abstract char getSymbol();
}
