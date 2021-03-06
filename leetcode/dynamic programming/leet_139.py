"""
139. 单词拆分
链接：https://leetcode-cn.com/problems/word-break
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

class Solution:

    def wordBreak(self, s: str, wordDict) -> bool:
        self.words = wordDict
        self.not_breakable = set()
        return self.is_breakable(s)

    def is_breakable(self, s):
        if len(s) == 0:
            return True
        for i in range(1, len(s)+1):
            if s[:i] in self.words:
                if i not in self.not_breakable and self.is_breakable(s[i:]):
                    return True
                else:
                    self.not_breakable.add(i)

        return False


if __name__ == '__main__':
    print(Solution().wordBreak("leetcode", ["leet", "code"]))

