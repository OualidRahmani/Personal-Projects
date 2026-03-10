import pieces.Piece;

package board;

public class Square {
    private Piece _piece = null;
    private boolean _isOccupied = false;

    public Square(Piece piece) {
        _piece = piece;
        _isOccupied = true;
    }
}
