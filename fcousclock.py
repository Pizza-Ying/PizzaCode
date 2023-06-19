# PizzaCode
import time

# 设置专注时间（分钟）
focus_time = 25

# 获取当前时间
start_time = time.time()

# 转换为秒
focus_time *= 60

# 循环计时
while True:
    # 计算已经过去的时间
    elapsed_time = time.time() - start_time

    # 计算剩余时间
    remaining_time = focus_time - elapsed_time

    # 如果计时结束，退出循环
    if remaining_time <= 0:
        print("Time's up!")
        break

    # 计算分钟和秒数
    minutes, seconds = divmod(remaining_time, 60)

    # 输出剩余时间
    print(f"Remaining time: {int(minutes)}:{int(seconds):02d}", end='\r')
    time.sleep(1)
