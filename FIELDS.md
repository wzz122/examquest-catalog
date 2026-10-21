# 字段说明

## 新增一个考试

在 `exams` 数组里复制一段，改成新考试的内容：

```json
{
  "id": "kanken2",
  "nameZh": "汉检 2 级",
  "nameJa": "日本漢字能力検定 2級",
  "category": "language",
  "hensachi": 49,
  "hensachiSource": "資格の取り方",
  "studyHoursMin": 100,
  "studyHoursMax": 150,
  "studyHoursNote": "已有常用汉字基础时的参考",
  "passRate": "约25%（2024）",
  "schedule": "每年 6 月、10 月、2 月；另有 CBT",
  "modules": [
    { "name": "读音", "weight": 20 },
    { "name": "书写", "weight": 30 },
    { "name": "部首・熟语", "weight": 25 },
    { "name": "四字熟语・对义语", "weight": 25 }
  ],
  "officialURL": "https://www.kanken.or.jp/",
  "keywords": ["漢検", "汉字", "kanken"]
}
```

## 字段说明

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | 英文小写短名，**一旦发布不要改**。已建计划靠它找到偏差值。 |
| `nameZh` | 是 | 列表里显示的中文名，也是新计划的默认名称。 |
| `nameJa` | 是 | 日文正式名称，显示在中文名下面，也参与搜索。 |
| `category` | 是 | 只能是：`language` 语言、`study_abroad` 留学升学、`accounting_finance` 会计金融、`it` IT、`law_realestate` 法律不动产、`business` 职场商务、`care` 介护医疗、`life` 生活。 |
| `hensachi` | 否 | 资格偏差值（整数）。查不到可靠数字就写 `null`，界面显示「—」。不要编数字。 |
| `hensachiSource` | 否 | 偏差值出处网站名。 |
| `studyHoursMin` / `studyHoursMax` | 是 | 参考总学习小时。默认目标取两者中间并四舍五入到 10 小时。 |
| `studyHoursNote` | 否 | 时长的前提，例如「已过 N2」「中文母语者通常更少」。 |
| `passRate` | 否 | 合格率文字，建议带年份。 |
| `schedule` | 是 | 考试时间的文字说明，显示在日期选择旁边。 |
| `modules` | 是 | 学习模块。`name` 会变成计划里的章节；`weight` 是占学习时间的比重（正整数，总和建议 100）。 |
| `officialURL` | 否 | 官网。 |
| `keywords` | 否 | 额外搜索词：简称、英文、别名。 |

## 规则

- 数组顺序就是列表顺序。同一分类的考试请放在一起。
- `modules` 为空、`weight` 不是正数、或 `studyHoursMax < studyHoursMin` 的条目会被自动跳过，不会让 App 崩溃。
- 修改后请运行测试：`ExamCatalogTests` 会检查 id 不重复、模块名不重复、偏差值在 30–80 之间。
- 每次大改，请把文件顶部的 `updatedAt` 改成当天日期，并把 `version` 加 1。

## 数字从哪里来

- 偏差值：主要参考「資格の取り方」的资格偏差值。这是民间的难度参考，不是官方数据，App 里已经写明。
- 备考时长、合格率：来自主办方公开数据或常见的备考经验值，会随年份变化，建议每年核对一次。
- 已经创建的计划不会随考试库更新而改变章节和时长，只会更新列表和卡片上显示的偏差值。
