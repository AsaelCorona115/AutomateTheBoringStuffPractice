#Board for testing
STARTING_BOARD  = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}



#This function checks if a given chess board configuration is valid.
def isValidChessBoard(board):
    #We start assuming the board is valid
    result = "Congrats! Your board is Valid!"
    
    
    #Creating a separate array for the pieces and squares
    pieces = list(board.values())
    squares = list(board.keys())
    
    
    #First condition we check is if there is exactly one white king and one black king
    if pieces.count("bK") != 1 or pieces.count("wK") != 1:
        result = "I'm sorry, your board doesn't have the correct number of Kings :c"




    #Second condition we check is if each player has at most 16 pieces
    blackPieces = []
    whitePieces = []
    for p in pieces:
        if p[0] == "b":
            blackPieces.append(p)
    
        elif p[0] == "w":
            whitePieces.append(p)

    if len(blackPieces) > 16 or len(whitePieces) > 16:
        result = "Sorry you have more pieces than you can :c"
    
    
    
    #Third condition we check is if there are only 8 pawns at most for each player
    blackPawnCounter = 0
    whitePawnCounter = 0
    for p in blackPieces:
        if p[1] == "P":
            blackPawnCounter +=1 
    
    for p in whitePieces:
        if p[1] == "P":
            whitePawnCounter +=1 
    
    if blackPawnCounter > 8 or whitePawnCounter > 8:
        result = "Sorry you have more pawns than you can :c"
    
    
    
    
    
    #Fourth condition is checking for a valid square
    validNumbers = '12345678'
    validLetters = 'abcdefgh'
    
    for s in squares:
        if s[0] not in validLetters or s[1] not in validNumbers:
            result = "Sorry, you have some invalid squares"
    

    #Fifth condition is checking that the pieces start with eiither w or b and are a valid piece
    validColors = "wb"
    validPieces = "PNRQKB"
    
    for p in pieces:
        if p[0] not in validColors or p[1] not in validPieces:
            result = "Sorry, you have some invalid pieces"
    


    print(result)
    return

    

isValidChessBoard(STARTING_BOARD)