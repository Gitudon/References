import datetime

current_time = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")

HEADER = f"## 勉強になったサイトたち\n\nエンジニアとしてのスキルを磨くにあたって参考にしたサイトをまとめています。\n\n## 集計({current_time})\n\n"

with open("README.md", "w") as file:
    file.write(HEADER)
