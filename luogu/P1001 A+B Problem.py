'''
题目描述:
输入两个整数a,b, 输出它们的和（∣a∣,∣b∣≤10^9）

输入：30 20
输出：50
'''
n = input().split()  # n是列表，不能加int()
print(int(n[0])+int(n[1]))

'''
C语言：
#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", a+b);
    return 0;
}
'''
