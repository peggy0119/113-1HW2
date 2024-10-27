from typing import List
def getResult():
    alphabet1: List[List[str]] = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
    ]
    alphabet2: List[List[str]] = [
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
    ]
    n = int(input("輸入資料組數: "))
    repeat = set()
    def find_and_print(value, direction, alphabet):
        for j in range(len(alphabet)):
            if value in alphabet[j]:
                k = alphabet[j].index(value)
                new_j, new_k = j, k
                if direction == 1 and j > 0:
                    new_j -= 1
                elif direction == 2 and j < len(alphabet) - 1:
                    new_j += 1
                elif direction == 3 and k < len(alphabet[j]) - 1:
                    new_k += 1
                elif direction == 4 and k > 0:
                    new_k -= 1
                else:
                    continue  # 若移動超出邊界則跳過
                ans = alphabet[new_j][new_k]
                if ans not in repeat:
                    print(ans)
                    repeat.add(ans)
                break
    for _ in range(n):
        value, direction = input("輸入按鍵與方向: ").split()
        direction = int(direction)
        find_and_print(value, direction, alphabet1)
        find_and_print(value, direction, alphabet2)
getResult()
