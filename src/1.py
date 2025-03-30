import json

# 读取 output.json
input_file = "./src/output.json"  # 确保文件在同一目录
output_file = "converted_output.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 解析数据
header = data[0]  # 第一行为字段名
players = data[1:]  # 剩下的是数据

# 目标格式
converted_data = {"age": {}}

for player in players:
    name, team, nationality, district, age, position, majapp = player

    # 仅处理年龄在 18-38 之间，majapp 在 1-19 之间的数据
    age = int(age)
    majapp = int(majapp)
    if not (18 <= age <= 38) or not (1 <= majapp <= 19):
        continue  # 跳过不符合范围的数据

    # 处理 age 和 majapp 数值
    age_key = str(age)
    majapp_key = str(majapp)

    # 初始化结构
    if age_key not in converted_data["age"]:
        converted_data["age"][age_key] = {"majapp": {}}

    if majapp_key not in converted_data["age"][age_key]["majapp"]:
        converted_data["age"][age_key]["majapp"][majapp_key] = []

    # 添加选手数据
    converted_data["age"][age_key]["majapp"][majapp_key].append({
        "name": name,
        "isNoob": False,  # 默认 False
        "position": position,
        "team": team,
        "nationality": nationality,
        "district": district,
    })

# **排序处理**
sorted_data = {
    "age": {
        age: {
            "majapp": {
                majapp: converted_data["age"][age]["majapp"][majapp]
                for majapp in sorted(converted_data["age"][age]["majapp"], key=int)  # 按 majapp 排序
            }
        }
        for age in sorted(converted_data["age"], key=int)  # 按 age 排序
    }
}

# 将排序后的数据写入 JSON 文件
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, indent=2, ensure_ascii=False)

print(f"转换完成！数据已保存至 {output_file}")
