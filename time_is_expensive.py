"""
    @作者：张家馨
    @功能：计算自出生以来，我已度过多少天
    @目的：告诉自己要珍惜时间
    @时间：2024-06-18
"""


from datetime import datetime


# 自张家馨出生以来，已有多少时日流逝
def zhangjiaxin():
    # 定义开始日期
    start_date = datetime(1992, 6, 25)

    # 获取当前日期
    current_date = datetime.now()

    # 计算两个日期之间的差异
    delta = current_date - start_date

    # 输出差异天数
    days_passed = delta.days
    print(f"  自张家馨出生以来， {days_passed} 个日子已经流逝。")


if __name__ == '__main__':
    print(f"  现在是{datetime.today()}")
    zhangjiaxin()
    print("  今天的下午就是今天上午的未来。————来日并不方长，想做的事情不要一拖再拖")
    print("  许多人说“和自己和解了”的时候，往往说的是“我放弃了”。————不要让所谓“成熟”成为怯懦的借口")
    print("  共勉！")
