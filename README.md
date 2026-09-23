# git

我的第一个 GitHub 仓库，用于测试本地与 GitHub 之间的连接。

## 环境

| 项目 | 说明 |
| --- | --- |
| 本地路径 | `C:\Users\LENOVO\OneDrive\Desktop\git` |
| 远程仓库 | https://github.com/Nychordax/git.git |
| 默认分支 | `main` |

## 常用命令

```bash
# 查看当前改动状态
git status

# 暂存全部改动并提交
git add .
git commit -m "说明这次改了什么"

# 推送到 GitHub
git push
```

## 首次推送（已完成，留作参考）

```bash
git init -b main
git remote add origin https://github.com/Nychordax/git.git
git add .
git commit -m "chore: 初始化仓库"
git push -u origin main
```
