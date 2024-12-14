class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #the logic is to use a set, if != . , check if digit is in set, if so return false, if not continue. 
        # do it for each row
        length=len(board[0])
        #check row
        for r in range(9):
            check=set()

            for c in range(9):

                if board[r][c] != '.':

                    if board[r][c] in check:
                        return False
                    check.add(board[r][c])



        #check col

        for c in range(9):
            check=set()

            for r in range(9):

                if board[r][c] != '.':

                    if board[r][c] in check:
                        return False
                    check.add(board[r][c])

        starts = [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3, 6),
                (6,0), (6,3), (6,6)]

        #check box, done so by adding 
        for row_s,col_s in starts:
            check=set()
            for r in range(row_s,row_s+3):

                for c in range(col_s,col_s+3):

                    if board[r][c] != '.':

                        if board[r][c] in check:
                            return False
                    check.add(board[r][c])
        return True
