# ============================================
# 番茄学习计时器 - 帮你专注学习
# ============================================

# import 是"导入"的意思，导入其他模块的功能
# time 是 Python 自带的时间模块，可以用来计时
import time


# 定义一个番茄钟函数
# work_minutes 是学习多少分钟，默认 25 分钟
def pomodoro_timer(work_minutes=25, break_minutes=5):
    print("🍅 番茄钟开始！")
    print(f"本次学习时间：{work_minutes} 分钟")
    print(f"休息时间：{break_minutes} 分钟")
    print("-" * 30)
    
    # 把分钟转换成秒，因为 time.sleep 用的是秒
    total_seconds = work_minutes * 60
    
    # 用 for 循环倒计时
    # range 生成一个从 total_seconds 到 0 的序列，每次减 1
    for remaining in range(total_seconds, 0, -1):
        # divmod 同时算出分钟和秒
        # 比如 150 秒，divmod(150, 60) 会返回 (2, 30)，就是 2 分 30 秒
        minutes, seconds = divmod(remaining, 60)
        
        # 用 \r 让光标回到行首，这样数字会原地刷新，不会一直往下刷屏
        print(f"\r专注中... {minutes:02d}:{seconds:02d}", end="")
        
        # 暂停 1 秒
        time.sleep(1)
    
    # 学习结束
    print("\n\n🎉 太棒了！这一轮学习完成！")
    print(f"现在休息 {break_minutes} 分钟吧 ☕")
    
    # 休息倒计时
    break_seconds = break_minutes * 60
    for remaining in range(break_seconds, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        print(f"\r休息中... {minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)
    
    print("\n\n⏰ 休息结束！准备开始下一轮吧！")


# 学习记录功能 - 记录每天学了多久
# 用一个列表来存学习记录
study_log = []

def log_study(session_name, minutes):
    """
    记录一次学习
    session_name: 学习内容，比如"行测资料分析"
    minutes: 学了多少分钟
    """
    # 把这次学习加到列表里
    study_log.append({
        "内容": session_name,
        "时长(分钟)": minutes
    })
    print(f"✅ 已记录：{session_name} - {minutes} 分钟")


def show_summary():
    """显示学习总结"""
    if len(study_log) == 0:
        print("还没有学习记录哦～")
        return
    
    print("\n📊 学习总结")
    print("-" * 30)
    total = 0
    for record in study_log:
        print(f"📚 {record['内容']}：{record['时长(分钟)']} 分钟")
        total += record['时长(分钟)']
    
    print("-" * 30)
    print(f"总学习时长：{total} 分钟 = {total/60:.1f} 小时")


# 主程序
if __name__ == "__main__":
    print("=== 番茄学习助手 ===")
    print("1. 开始番茄钟（25分钟专注 + 5分钟休息）")
    print("2. 记录学习时长")
    print("3. 查看学习总结")
    
    choice = input("\n请选择功能（输入数字）：")
    
    if choice == "1":
        pomodoro_timer()
    elif choice == "2":
        content = input("学了什么？")
        mins = int(input("学了多少分钟？"))
        log_study(content, mins)
    elif choice == "3":
        show_summary()
    else:
        print("输入无效哦～")
