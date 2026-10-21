# ExamQuest 考试库

这是备考专注 App **ExamQuest** 的考试列表数据。App 启动或进入「选择考试」页时，每天最多联网一次读取这里的 `ExamCatalog.json`；版本号比 App 当前的高就自动换成新列表，不用发新版 App。

## 怎么加一个考试

1. 直接在 GitHub 网页上编辑 `ExamCatalog.json`：在 `exams` 数组里复制一段，改成新考试。
2. 把顶部的 `version` 加 1，`updatedAt` 改成当天日期。**不加版本号 App 不会更新。**
3. 提交（Commit）到 `main`。几分钟内 App 就能拉到。

每段的字段含义和规则见 [FIELDS.md](FIELDS.md)。改完本地可以跑一下检查：

```bash
python3 -I validate.py ExamCatalog.json
```

## 规则

- `id` 一旦发布不要改，已建的计划靠它找偏差值。
- 偏差值查不到就写 `null`，不要编。
- 同一分类的考试放在一起，数组顺序就是列表顺序。
- 文件有问题（不是合法 JSON、`exams` 为空、版本号没加）App 会忽略这次更新，继续用旧列表，不会崩。

## 隐私

App 只下载这一个公开文件，不上传任何数据。关掉设置里的「自动更新考试库」后不再联网。
