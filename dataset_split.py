import os
import random

dataset_dir = "zhubo_preprocessed"
train_ratio = 0.8
val_ratio = 0.2
test_ratio = 0.1

# 获取所有日期目录的路径
date_dirs = [os.path.join(dataset_dir, date_dir) for date_dir in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, date_dir))]

# 存储所有的section目录路径
section_dirs = []

# 遍历日期目录，获取所有section目录的路径
for date_dir in date_dirs:
    section_dirs.extend([os.path.join(date_dir, section_dir) for section_dir in os.listdir(date_dir) if os.path.isdir(os.path.join(date_dir, section_dir))])

# 随机打乱section目录列表
random.shuffle(section_dirs)

# 计算划分的索引位置
total_sections = len(section_dirs)
train_end = int(total_sections * train_ratio)
val_end = int(total_sections * (train_ratio + val_ratio))

# 创建并写入train.txt文件
with open(os.path.join("filelists", "train.txt"), "w") as train_file:
    for section_dir in section_dirs[:train_end]:
        rel_path = os.path.relpath(section_dir, dataset_dir)
        train_file.write(rel_path + "\n")

# 创建并写入val.txt文件
with open(os.path.join("filelists", "val.txt"), "w") as val_file:
    for section_dir in section_dirs[train_end:val_end]:
        rel_path = os.path.relpath(section_dir, dataset_dir)
        val_file.write(rel_path + "\n")

# 创建并写入test.txt文件
with open(os.path.join("filelists", "test.txt"), "w") as test_file:
    for section_dir in section_dirs[val_end:]:
        rel_path = os.path.relpath(section_dir, dataset_dir)
        test_file.write(rel_path + "\n")