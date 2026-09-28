import re
from collections import Counter


def build_vocabulary(filename):
    """从txt文件的文本中生成词频词典。"""
    # TODO 1: 读取文本文件内容，统一大小写，提取单词并生成词频词典 #
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    return Counter(words)


def min_edit_distance(source, target):
    # TODO 2: 动态规划
    m, n = len(source), len(target)
    # 初始化 dp 矩阵
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # 删除
                           dp[i][j - 1] + 1,  # 插入
                           dp[i - 1][j - 1] + cost)  # 替换

    return dp[i][j]


def generate_candidates(word, vocabulary, max_dist=2):
    """从词典中寻找编辑距离不超过 max_dist 的词。"""
    candidates = []
    for candidate in vocabulary:
        # TODO 3: 调用最小编辑距离函数，保留符合距离要求的候选词 #
        distance = min_edit_distance(word, candidate)
        if distance <= max_dist:
            candidates.append((candidate, distance))
    return candidates


def rank_candidates(candidates, vocabulary, max_dist=2):
    """先按编辑距离升序，再按词频降序排列。"""
    return sorted(
        candidates,
        key=lambda item: (
            item[1],  # 第一优先级：编辑距离小的
            -vocabulary[item[0]],  # 第二优先级：词频高的
            item[0]  # 第三优先级：字母顺序靠前的
        )
    )


def suggest(word, vocabulary, top_k=5):
    """返回最多 top_k 个拼写建议。"""
    word = word.lower()

    # 词典中已有的词视为拼写正确
    if word in vocabulary:
        return [(word, 0)]

    # TODO 4: 调用generate和rank函数，生成前5个建议 #
    candidates = generate_candidates(word, vocabulary)
    ranked = rank_candidates(candidates, vocabulary)

    return ranked[:top_k]


if __name__ == "__main__":
    vocabulary = build_vocabulary("data/big.txt")

    test_words = ["aple", "carroot", "implementantation", "becaus"]

    for word in test_words:
        print(word, "→", suggest(word, vocabulary))