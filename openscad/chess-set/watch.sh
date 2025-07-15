PIECE=$1
watchmedo shell-command -c "inv build $PIECE" -p "$PIECE.py;units.py" -w -W
