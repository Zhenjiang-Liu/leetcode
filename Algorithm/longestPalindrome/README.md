# 5. 最长回文子串
题目描述：https://leetcode-cn.com/problems/longest-palindromic-substring/

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

解析：

(1) 暴力法

(2) 动态规划(中心扩散法)

如果子串S_i和S_j是回文字符串则P(i,j)为ture.

其他情况，P(i,j)为false.

因此 P(i,j)=(P(i+1,j−1) and S_i==S_j)

基本示例如下：

P(i, i) = true

P(i, i+1) = ( S_i == S_{i+1} )
