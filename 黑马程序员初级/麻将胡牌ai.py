from typing import List, Tuple


class PureSuitMahjong:
    def __init__(self):
        pass

    def is_win(self, hand: List[int]) -> bool:
        """
        判断14张牌是否和牌
        hand: 长度为9的列表，hand[i]表示数字i+1的数量
        """
        total = sum(hand)
        if total != 14:
            return False

        # 递归函数：判断剩余牌是否能组成面子
        def can_form_melds(cnt: List[int]) -> bool:
            if sum(cnt) == 0:
                return True

            # 找到第一个有牌的位置
            first = -1
            for i in range(9):
                if cnt[i] > 0:
                    first = i
                    break
            if first == -1:
                return True

            # 尝试刻子（三张相同的牌）
            if cnt[first] >= 3:
                cnt[first] -= 3
                if can_form_melds(cnt):
                    cnt[first] += 3
                    return True
                cnt[first] += 3

            # 尝试顺子（连续三张牌）
            if first <= 6 and cnt[first] >= 1 and cnt[first + 1] >= 1 and cnt[first + 2] >= 1:
                cnt[first] -= 1
                cnt[first + 1] -= 1
                cnt[first + 2] -= 1
                if can_form_melds(cnt):
                    cnt[first] += 1
                    cnt[first + 1] += 1
                    cnt[first + 2] += 1
                    return True
                cnt[first] += 1
                cnt[first + 1] += 1
                cnt[first + 2] += 1

            return False

        # 尝试所有可能的将牌（对子）
        for i in range(9):
            if hand[i] >= 2:
                hand[i] -= 2
                if can_form_melds(hand):
                    hand[i] += 2
                    return True
                hand[i] += 2

        return False

    def find_listening_tiles(self, hand_13: List[int]) -> List[int]:
        """
        找出听哪些牌
        hand_13: 长度为9的列表，表示13张牌的数量分布
        """
        if sum(hand_13) != 13:
            raise ValueError("手牌必须是13张")

        listening_tiles = []

        # 枚举所有可能摸到的牌
        for tile in range(9):
            if hand_13[tile] < 4:  # 不能超过4张
                # 创建14张牌的副本
                hand_14 = hand_13.copy()
                hand_14[tile] += 1

                if self.is_win(hand_14):
                    listening_tiles.append(tile + 1)  # 返回1-9的数字

        return listening_tiles

    def parse_hand(self, tiles: List[int]) -> List[int]:
        """
        将牌的数字列表转换为数量数组
        例如：[1,1,1,2,3,4,5,6,7,8,9,9,9] -> [3,1,1,1,1,1,1,1,3]
        """
        count = [0] * 9
        for tile in tiles:
            if 1 <= tile <= 9:
                count[tile - 1] += 1
            else:
                raise ValueError(f"无效的牌: {tile}")
        return count

    def check_hand(self, tiles: List[int]) -> Tuple[List[int], List[int]]:
        """
        主函数：输入13张牌，返回听牌列表和详细分析
        """
        # 验证输入
        if len(tiles) != 13:
            raise ValueError("必须是13张牌")

        hand_count = self.parse_hand(tiles)
        listening = self.find_listening_tiles(hand_count)

        return listening, hand_count


# 优化版本：使用记忆化提高性能
class OptimizedPureSuitMahjong(PureSuitMahjong):
    def __init__(self):
        super().__init__()
        self.memo = {}

    def is_win(self, hand: List[int]) -> bool:
        total = sum(hand)
        if total != 14:
            return False

        # 将手牌转换为元组作为缓存键
        hand_tuple = tuple(hand)

        # 递归函数，使用记忆化
        def can_form_melds_memo(cnt_tuple: Tuple[int]) -> bool:
            if cnt_tuple in self.memo:
                return self.memo[cnt_tuple]

            cnt = list(cnt_tuple)
            total_cnt = sum(cnt)

            if total_cnt == 0:
                self.memo[cnt_tuple] = True
                return True

            # 找到第一个有牌的位置
            first = -1
            for i in range(9):
                if cnt[i] > 0:
                    first = i
                    break

            result = False

            # 尝试刻子
            if cnt[first] >= 3:
                cnt[first] -= 3
                if can_form_melds_memo(tuple(cnt)):
                    result = True
                cnt[first] += 3

            # 尝试顺子
            if not result and first <= 6 and cnt[first] >= 1 and cnt[first + 1] >= 1 and cnt[first + 2] >= 1:
                cnt[first] -= 1
                cnt[first + 1] -= 1
                cnt[first + 2] -= 1
                if can_form_melds_memo(tuple(cnt)):
                    result = True
                cnt[first] += 1
                cnt[first + 1] += 1
                cnt[first + 2] += 1

            self.memo[cnt_tuple] = result
            return result

        # 清空记忆缓存（针对当前手牌）
        self.memo = {}

        # 尝试所有可能的将牌
        for i in range(9):
            if hand[i] >= 2:
                hand[i] -= 2
                if can_form_melds_memo(tuple(hand)):
                    hand[i] += 2
                    return True
                hand[i] += 2

        return False


# 测试函数
def test_examples():
    print("清一色听牌检查程序")
    print("=" * 50)

    solver = OptimizedPureSuitMahjong()

    # 测试用例
    test_cases = [
        # (手牌, 预期听牌, 描述)
        (
            [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9],  # 三连刻+顺子
            [2, 5, 8],  # 听2、5、8万
            "标准听三面"
        ),
        (
            [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],  # 多个对子
            [1, 2, 3, 4, 5, 6],  # 七对子听牌
            "七对子听牌"
        ),
        (
            [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9],  # 缺少什么？
            [2, 5, 8, 9],  # 听2、5、8、9
            "复杂听牌"
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4],  # 基本一气
            [1, 2, 3, 4, 5, 6, 7],  # 多面听
            "一气通贯型"
        ),
    ]

    for tiles, expected, description in test_cases:
        print(f"\n测试: {description}")
        print(f"手牌: {sorted(tiles)}")

        try:
            listening, hand_count = solver.check_hand(tiles)
            print(f"听牌: {listening}")
            print(f"预期: {expected}")
            print(f"结果: {'✓' if set(listening) == set(expected) else '✗'}")
            print(f"牌型分布: {hand_count}")
        except Exception as e:
            print(f"错误: {e}")

    # 交互式测试
    print("\n" + "=" * 50)
    print("交互测试（输入13个1-9的数字，空格分隔）:")

    while True:
        try:
            user_input = input("\n输入手牌（或输入q退出）: ").strip()
            if user_input.lower() == 'q':
                break

            tiles = list(map(int, user_input.split()))
            listening, hand_count = solver.check_hand(tiles)

            print(f"手牌分布: {hand_count}")
            print(f"听牌: {listening}")
            print(f"听牌数量: {len(listening)}张")

            # 显示具体的牌
            if listening:
                tile_names = ["一万", "二万", "三万", "四万", "五万", "六万", "七万", "八万", "九万"]
                listening_names = [tile_names[t - 1] for t in listening]
                print(f"听: {', '.join(listening_names)}")
            else:
                print("不听牌")

        except ValueError as e:
            print(f"输入错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")


if __name__ == "__main__":
    test_examples()