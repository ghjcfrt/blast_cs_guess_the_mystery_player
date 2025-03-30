import tkinter as tk
from tkinter import ttk


def submit_action():
    message_label.config(text="提交成功！")


# 创建主窗口
root = tk.Tk()
root.title("Blast Guess")

# 消息展示窗口
message_label = tk.Label(root, text="请选择选项并提交", font=("Arial", 12))
message_label.pack(pady=10)

# 年龄下拉选择框
age_label = tk.Label(root, text="年龄:")
age_label.pack()
age_var = tk.StringVar()
age_combobox = ttk.Combobox(root, textvariable=age_var, state="readonly")
age_combobox["values"] = [str(i) for i in range(18, 39)]
age_combobox.pack()

# major次数下拉选择框
major_label = tk.Label(root, text="major次数:")
major_label.pack()
major_var = tk.StringVar()
major_combobox = ttk.Combobox(root, textvariable=major_var, state="readonly")
major_combobox["values"] = [str(i) for i in range(1, 20)]
major_combobox.pack()

# 赛区下拉选择框
region_label = tk.Label(root, text="赛区:")
region_label.pack()
region_var = tk.StringVar()
region_combobox = ttk.Combobox(root, textvariable=region_var, state="readonly")
region_combobox["values"] = ["赛区1", "赛区2", "赛区3", "赛区4"]
region_combobox.pack()

# 位置下拉选择框
position_label = tk.Label(root, text="位置:")
position_label.pack()
position_var = tk.StringVar()
position_combobox = ttk.Combobox(root, textvariable=position_var, state="readonly")
position_combobox["values"] = ["步枪手", "狙击手"]
position_combobox.pack()

# 模式下拉选择框
mode_label = tk.Label(root, text="模式:")
mode_label.pack()
mode_var = tk.StringVar()
mode_combobox = ttk.Combobox(root, textvariable=mode_var, state="readonly")
mode_combobox["values"] = ["noob", "pro"]
mode_combobox.pack()

# 提交按钮
submit_button = tk.Button(root, text="提交", command=submit_action)
submit_button.pack(pady=10)

# 运行主循环
root.mainloop()
root.mainloop()
