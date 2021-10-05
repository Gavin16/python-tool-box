# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

"""
使用 pandas 读取csv 文件,解析输出为json文件
-- from 《内蒙古大屏展示》
"""
import pandas as pd
import json

"""
文件读取与写入 + DataFrame 使用
"""


def read_file(file_path):
    # 文件用的GBK进行编码
    csv_file = pd.read_csv(file_path, encoding="GBK")
    df = pd.DataFrame(csv_file)
    clos = df.columns
    print(clos)

    data = df[1:]
    cell_list = list()
    # iterrows以  (index, Series) 对的形式进行遍历
    for index, row in data.iterrows():
        cell = {"name": row["company_name"]}
        pos = [row["company_gis_lat"], row["company_gis_lon"]]
        cell["value"] = pos
        cell["address"] = row["address"]
        cell_list.append(cell)
    return cell_list


def batch_convert_to_json():
    source_file_paths = [
        "files/to-json/06新兴产业领域企业分布热力图-内蒙-高端装备.csv",
        "files/to-json/06新兴产业领域企业分布热力图-内蒙-蒙中医药.csv",
        "files/to-json/06新兴产业领域企业分布热力图-内蒙-生物科技.csv",
        "files/to-json/06新兴产业领域企业分布热力图-内蒙-新材料.csv",
        "files/to-json/06新兴产业领域企业分布热力图-内蒙-新能源.csv",
        "files/to-json/06新兴产业领域企业分布热力图-内蒙-云计算大数据.csv"
    ]
    dest_file_paths = [
        "files/to-json/地理热力图-内蒙-高端装备.json",
        "files/to-json/地理热力图-内蒙-蒙中医药.json",
        "files/to-json/地理热力图-内蒙-生物科技.json",
        "files/to-json/地理热力图-内蒙-新材料.json",
        "files/to-json/地理热力图-内蒙-新能源.json",
        "files/to-json/地理热力图-内蒙-云计算大数据.json"
    ]

    for index in range(len(source_file_paths)):
        source_path = source_file_paths[index]
        dest_path = dest_file_paths[index]

        data_list = read_file(source_path)
        dest_file = open(dest_path, "w")
        json_str = json.dumps(data_list, ensure_ascii=False)

        dest_file.write(json_str)
        dest_file.close()


if __name__ == '__main__':
    batch_convert_to_json()
