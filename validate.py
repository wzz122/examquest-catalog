#!/usr/bin/env python3
"""检查 ExamCatalog.json 能不能被 App 接受。用法：python3 -I validate.py ExamCatalog.json"""
import json, sys

CATEGORIES = {"language", "study_abroad", "accounting_finance", "it",
              "law_realestate", "business", "care", "life"}
REQUIRED = ["id", "nameZh", "nameJa", "category", "studyHoursMin",
            "studyHoursMax", "schedule", "modules"]

def main(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    problems = []
    if not isinstance(data.get("version"), int) or data["version"] < 1:
        problems.append("顶部 version 必须是正整数")
    if not data.get("updatedAt"):
        problems.append("顶部 updatedAt 不能为空")
    ids = set()
    for exam in data.get("exams", []):
        tag = exam.get("id", "<无 id>")
        for key in REQUIRED:
            if key not in exam:
                problems.append(f"{tag}: 缺少 {key}")
        if tag in ids:
            problems.append(f"{tag}: id 重复")
        ids.add(tag)
        if exam.get("category") not in CATEGORIES:
            problems.append(f"{tag}: category 不在允许列表里")
        lo, hi = exam.get("studyHoursMin", 0), exam.get("studyHoursMax", 0)
        if not (isinstance(lo, int) and isinstance(hi, int) and 0 < lo <= hi):
            problems.append(f"{tag}: studyHoursMin/Max 要是正整数且 Min ≤ Max")
        modules = exam.get("modules") or []
        names = [m.get("name") for m in modules]
        if not modules:
            problems.append(f"{tag}: modules 不能为空")
        if len(set(names)) != len(names):
            problems.append(f"{tag}: 模块名重复")
        if any(not isinstance(m.get("weight"), int) or m["weight"] <= 0 for m in modules):
            problems.append(f"{tag}: 每个模块 weight 要是正整数")
        h = exam.get("hensachi")
        if h is not None and not (isinstance(h, int) and 30 <= h <= 80):
            problems.append(f"{tag}: hensachi 要在 30–80 之间或为 null")
    if problems:
        print("\n".join(problems)); sys.exit(1)
    print(f"OK：version {data['version']}，{len(ids)} 个考试")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "ExamCatalog.json")
