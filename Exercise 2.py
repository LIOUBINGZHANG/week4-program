# 題目二：社團 T 恤結算（爛命名版：可執行但難讀）
original_price = 180 # 單價
big_size = 20 # XL 以上加價
quick = 150 # 急件加價
discount = 0.95 # 打折(30件以上)
fare = 120 # 運費

n = 28          # 訂購件數
b = 6           # XL 以上的件數
q = True        # 是否急件


total = original_price * n # 代表總價
total = total + (big_size * b) # 算加大尺碼費用
if q == True:
    total = total + quick
if n >= 30:
    total = total * discount
total = total + fare
print(total)