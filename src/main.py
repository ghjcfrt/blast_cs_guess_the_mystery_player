import json
import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout

from ui import Ui_MainWindow


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data = self.load_data()
        self.ui.enter_btn.clicked.connect(self.filter_and_display)

    @staticmethod
    def load_data():
        # 加载 JSON 数据
        try:
            with Path("./src/弗一把.json").open(encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("错误: 无法找到 '弗一把.json' 文件，请检查文件路径。")
            sys.exit(1)

    # 过滤和显示结果
    def filter_and_display(self):
        district_mapping_reverse = {
            "亚洲": "Asia",
            "欧洲": "Europe",
            "独联体": "CIS",
            "南美洲": "South America",
            "北美洲": "North America",
            "中东和非洲": "MEA",
            "大洋洲": "Oceania",
        }
        position_mapping_reverse = {
            "步枪手": "Rifler",
            "狙击手": "AWPer",
        }
        age = self.ui.age_combobox.currentText()
        majapp = self.ui.majapp_combobox.currentText()
        position = self.ui.position_combobox.currentText()
        mode = self.ui.mode_combobox.currentText()
        district = self.ui.district_combobox.currentText()

        # 将中文赛区和位置选项转换为英文
        district_en = district_mapping_reverse.get(district, district)
        position_en = position_mapping_reverse.get(position, position)

        results = []
        for age_key, age_data in self.data["age"].items():
            if age not in {"未知", age_key}:
                continue
            for majapp_key, players in age_data["majapp"].items():
                if majapp not in {"未知", majapp_key}:
                    continue
                filtered_players = [
                    {
                        "name": player["name"],
                        "team": player["team"],
                        "nationality": player["nationality"],
                        "district": player["district"],
                        "age": age_key,
                        "position": player["position"],
                        "majapp": majapp_key,
                    }
                    for player in players
                    if (position == "未知" or player["position"] == position_en)
                    and (district == "未知" or player["district"] == district_en)
                    and ((mode == "Pro" and not player["isNoob"]) or (mode == "Noob" and player["isNoob"]))
                ]
                results.extend(filtered_players)

        self.display_results(results)

    # 显示结果
    def display_results(self, results):
        district_mapping = {
            "Asia": "亚洲",
            "Europe": "欧洲",
            "CIS": "独联体",
            "South America": "南美洲",
            "North America": "北美洲",
            "MEA": "中东和非洲",
            "Oceania": "大洋洲",
        }

        # 检查并清除现有布局
        existing_layout = self.ui.scrollAreaWidgetContents.layout()
        if existing_layout is None:
            layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)  # 创建新布局
        else:
            while existing_layout.count():  # 清除现有布局中的所有小部件
                item = existing_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
            layout = existing_layout  # 复用现有布局

        # 添加新内容
        for player in results:
            district_cn = district_mapping.get(player["district"], player["district"])
            text = (
                f"{player['name']} | {player['team']} | {player['nationality']} | {district_cn} | "
                f"{player['age']} | {player['position']} | {player['majapp']}"
            )
            text_edit = QTextEdit(self.ui.scrollAreaWidgetContents)
            text_edit.setText(text)
            text_edit.setReadOnly(True)
            text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            layout.addWidget(text_edit)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
