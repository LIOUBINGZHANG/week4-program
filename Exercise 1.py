# 題目一：新生名單統計（刻意放入 6 個錯誤）
# 目標：
# 1) 讀入以逗號分隔的姓名
# 2) 印出每個姓名及其長度
# 3) 統計名字長度 >= 3 的人數

raw_input = input("請輸入以逗號分隔的新生姓名：)  # 例如：Ann,Bob,李華,阿明:") # 錯誤1： 少了結尾的引號 

names = raw_input.split(",")
count = 0

for i in range(len(names)):  # 錯誤5： 應該是 len(names) 而不是 len(names)+1這樣會超出array 
    n = names[i].strip() # 錯誤2： 應該是 strip()作用是去除字串前後空白 而不是用 trim()這個是java的函數         
    l = len(n)
    print(f"姓名：{n}，長度 {l}")   # 錯誤3： len(n) 是整數，不能直接與字串連接
    if l >= 3:         # 錯誤4： 3應該是整數，不是字串            
        count = count + 1

print("符合條件的人數為：", count)  #錯誤6: 名稱錯誤


