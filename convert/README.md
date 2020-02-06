# 6. Z字形变换
题目描述：https://leetcode-cn.com/problems/zigzag-conversion/

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

解析：
1. 构建numRows行的list用来存储数据, 这里每一列都是一个字符串形式。

2. 假设 numRows为3, 则我们需要从res[0]到res[1]到res[2]再到1再res[0]到res[1]到res[2]的来存储字符串数据

3. 定义flag，我们每访问完一次res[start]后，对行数进行一次判断，
如果此时的start为第一行或者最后一行，则对flag取相反数，转换顺序。
（从0-2的访问时，可以先设置默认的flag为-1，当访问完res[0]后，取相反数，就是正方向了）


