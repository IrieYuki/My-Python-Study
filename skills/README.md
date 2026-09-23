# skills

这个目录是 Hermes Agent 技能的备份，和本仓库的 Python 学习内容同源保存。
每个子目录一份 `SKILL.md`，外加可选的 `references/`（规范与清单）和 `scripts/`（可直接跑的脚本）。

## verified-cheatsheet-notes

把「速查笔记」整理成能长期查阅的形态：

- **索引表放最前**，它同时充当目录和速查表，每行一个函数/方法，点「用法」直接跳到正文；
- 每条正文格式统一：`#### 名字 一句话` → `**签名** ｜ **返回** ｜ **备注**` → 可运行示例 → 可选 `> ⚠️`；
- 代码示例里的 `#` 注释必须是**真实输出**，写完用脚本验，不靠肉眼。

校验脚本（只用标准库，不需要 pip 安装）：

```bash
python3 skills/verified-cheatsheet-notes/scripts/verify_code_blocks.py note/Python内置函数速查笔记.md
# 输出：104 个代码块｜注释比对 271/271 一致｜退出码 0
```

它逐块执行 Markdown 里的 python 代码块，把 `#` 注释解析成期望值再和真实求值结果比对：
`input()` 用假 stdin 喂（不会卡住），代码块在临时目录里跑（不会污染工作目录），
`# ❌ ValueError` 这类注释表示「这行预期报错」，自动跳过比对。

本地安装位置：`~/.hermes/skills/note-taking/verified-cheatsheet-notes/`。
从 GitHub 复制回去时把整个目录拷到该路径即可。
