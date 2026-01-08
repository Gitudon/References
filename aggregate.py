import datetime


def make_header() -> str:
    current_time = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    return f"## 勉強になったサイトたち\n\nエンジニアとしてのスキルを磨くにあたって参考にしたサイトをまとめています。\n\n## 集計({current_time})\n\n"


def aggregate_references_by_topics() -> dict:
    aggregate_result = {}
    current = 0
    with open("references.md", "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("## "):
                target = line[3:-1]
                current = 0
                aggregate_result[target] = current
            elif line.startswith("["):
                aggregate_result[target] += 1
    return aggregate_result


def make_table() -> str:
    contents = aggregate_references_by_topics()
    table = "| トピック | 数 |\n| :--- | ---: |\n"
    for key, value in contents.items():
        table += f"| {key} | {value} |\n"
    return table[:-1]


with open("README.md", "w") as file:
    file.write(make_header())
    file.write(make_table())
