# break：当某些条件成立，退出整个循环
# 循环吃5个苹果，吃完第3个吃饱了，第4 和 5 不吃了（不执行） -- == 4 或 >3
i = 1
while i <= 5:
    # 条件：如果吃到4 或 > 3 打印吃饱了不吃了
    if i == 4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
