def find_max_min(a):
    n = len(a)
    if n == 0:
        return None, None #数组长度为0，则没有最大最小值
    elif n == 1:
        return a, a #数组长度为1，则最大最小相等

    if n % 2 == 0: #先比较前两个数
        if a > a[1]:
            max, min = a, a[1]
        else:
            max, min = a[1], a
        start = 2
    else: #前两个数相等
        max, min = a, a
        start = 1

    for i in range(start, n-1, 2): #从start开始，步长为2
        if a[i] > a[i+1]:
            if a[i] > max: max = a[i]
            if a[i+1] < min: min = a[i+1]
        else:
            if a[i+1] > max: max = a[i+1]
            if a[i] < min: min = a[i] # 如果数组长度为偶数，此步出结果

    
    if n % 2 != 0: #如果数组长度为奇数，单独比较最后一个元素
        if a[n-1] > max: max = a[n-1]
        if a[n-1] < min: min = a[n-1]

    return max, min
#分析：
# 1、最好情况：数组按顺序排列，算法需要从头到尾遍历一次，时间复杂度为O(n);
# 2、最坏情况：数组随意排列，算法还是只需要从头到尾遍历一次，时间复杂度为O(n);
# 3、平均时间复杂度为O(n)。