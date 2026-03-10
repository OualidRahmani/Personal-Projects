package board;

import pieces.Piece;

public class Square {
    private Piece _piece = null;
    private boolean _occupied = false;

    public Square(Piece piece) {
        _piece = piece;
        _occupied = true;
    }

    public Square() {
        _piece = null;
        _occupied = false;
    }

    public Piece getPiece() {
        return _piece;
    }

    public boolean isOccupied() {
        return _occupied;
    }
}
