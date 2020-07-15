class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        # 统计a、b的个数
        count_a = sum(1 for item in pattern if item == "a")
        count_b = len(pattern) - count_a
        # 若a的个数小于b的个数，调换a、b以保证a最少出现1次，继而枚举a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = "".join("a" if item == "b" else "b" for item in pattern)
        # 若value为空,则要求pattern 中要么为空，要么只有a,等价于b的个数为0
        if not value: return count_b == 0
        # 若pattern为空而value不为空，则无法匹配
        if not pattern and value: return False
        # 对于pattern和value都不为空时，遍历
        for len_a in range(len(value) // count_a + 1):
            leftForb = len(value) - count_a * len_a  # 可能的b的总长度
            # 看当前的分法是否满足要求（len(b)为大于等于0的整数）
            if (count_b == 0 and leftForb == 0) or (count_b != 0 and leftForb % count_b == 0):
                len_b = 0 if count_b == 0 else leftForb // count_b
                idx, Judge = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == "a":  # 对模式a的判断
                        subChr = value[idx:idx + len_a]
                        if not value_a:
                            value_a = subChr
                        elif value_a != subChr:
                            Judge = False
                            break
                        idx += len_a
                    else:  # 对模式b的判断
                        subChr = value[idx:idx + len_b]
                        if not value_b:
                            value_b = subChr
                        elif value_b != subChr:
                            Judge = False
                            break
                        idx += len_b
                if Judge and value_a != value_b:  # 找到满足的value_a,value_b且两者不相等，返回T
                    return True
        return False  # 遍历完都没找到，返回F


if __name__ == '__main__':
    pattern = "abba"
    value = "dogdogdogdog"
    solution = Solution()
    print(solution.patternMatching(pattern, value))
