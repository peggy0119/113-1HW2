# 接收使用者輸入，例如: nums = [3, 0, 1]
num = input("請輸入數組(格式為 nums = [3, 0, 1]): ")
# 解析輸入的數組，只取出等號後的數組部分，並轉換為列表
nums = eval(num.split('=')[1].strip())
# 取得數組的長度
n = len(nums)
# 計算從 0 到 n 的總和
sum1 = n * (n + 1) / 2
# 計算數組中所有數字的總和
sum2 = sum(nums)
# 取得缺少的數字
miss = sum1 - sum2
# 輸出缺少的數字，轉為整數形式
print("缺少的數字為:", int(miss))
