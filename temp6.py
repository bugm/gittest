class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        can_reach = {}
        to_search = [(0,0,moveTime[0][0])]
        row_len,col_len = len(moveTime),len(moveTime[0])
        updates = [(0,1),(0,-1),(1,0),(-1,0)]
        while to_search:
            temp_new = []
            for each in to_search:
                row,col,now_time = each
                for update in updates:
                    new_row,new_col = row + update[0],col + update[1]
                    if 0<= new_row < row_len and 0 <=new_col < col_len:
                        temp_time = max(moveTime[new_row][new_col], now_time) + 1
                        if (new_row,new_col) in can_reach and temp_time >= can_reach[(new_row,new_col)]:
                            continue
                        can_reach[(new_row,new_col)] = temp_time
                        temp_new.append((new_row,new_col,temp_time))
        return can_reach[(row_len-1,col_len-1)]