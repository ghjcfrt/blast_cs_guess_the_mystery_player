import json
import sys
from pathlib import Path

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
            # 获取运行时路径
            base_path = getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
            json_path = Path(base_path) / "弗一把.json"
            with json_path.open(encoding="utf-8") as file:
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
        position_mapping_reverse = {"步枪手": "Rifler", "狙击手": "AWPer"}

        filters = {
            "age": self.ui.age_combobox.currentText(),
            "majapp": self.ui.majapp_combobox.currentText(),
            "position": position_mapping_reverse.get(self.ui.position_combobox.currentText(), "未知"),
            "district": district_mapping_reverse.get(self.ui.district_combobox.currentText(), "未知"),
            "mode": self.ui.mode_combobox.currentText(),
        }

        results = self.get_filtered_results(filters)
        self.display_results(results)

    def get_filtered_results(self, filters):
        results = []
        for age_key, age_data in self.data["age"].items():
            if filters["age"] not in {"未知", age_key}:
                continue
            for majapp_key, players in age_data["majapp"].items():
                if filters["majapp"] not in {"未知", majapp_key}:
                    continue
                results.extend([
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
                    if (filters["position"] == "未知" or player["position"] == filters["position"])
                    and (filters["district"] == "未知" or player["district"] == filters["district"])
                    and (
                        (filters["mode"] == "Pro" and not player["isNoob"])
                        or (filters["mode"] == "Noob" and player["isNoob"])
                    )
                ])
        return results

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

        layout = self.ui.scrollAreaWidgetContents.layout() or QVBoxLayout(self.ui.scrollAreaWidgetContents)
        while layout.count():
            item = layout.takeAt(0)
            if widget := item.widget():
                widget.deleteLater()

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
            layout.addWidget(text_edit)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
