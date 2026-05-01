class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        columns = [set() for _ in range(len(board))]
        sub_boxes = [set() for _ in range(len(board))]

        for i_col, col_val in enumerate(board):
            for i_row, row_val in enumerate(col_val):
                if row_val == ".":
                    continue

                if row_val in rows[i_row]:
                    return False
                rows[i_row].add(row_val)
                
                if row_val in columns[i_col]:
                    return False
                columns[i_col].add(row_val)
                
                box_i = 0
                if i_col > 2:
                    box_i += 3
                if i_col > 5:
                    box_i += 3
                sub_index = box_i + i_row // 3
                if row_val in sub_boxes[sub_index]:
                    return False
                sub_boxes[sub_index].add(row_val)
                


        return True