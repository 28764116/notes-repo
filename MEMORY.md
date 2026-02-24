## 记忆记录

### 2026-02-24 笔记同步到 GitHub

**任务：** 帮用户新建 Git 链接同步笔记

**过程：**
1. 检查工作区状态，已有 git 仓库但无提交记录
2. 配置 git 全局身份信息
3. 生成 SSH 密钥对（ed25519 算法）
4. 配置 SSH 连接
5. 指导用户在 GitHub 上添加公钥
6. 成功推送代码到远程仓库

**结果：**
- 仓库地址：https://github.com/28764116/notes-repo
- 提交内容：包含 AGENTS.md、BOOTSTRAP.md、HEARTBEAT.md、IDENTITY.md、SOUL.md、TOOLS.md、USER.md 和 skills 目录

**配置：**
- SSH 密钥对：/root/.ssh/github-notes（私钥）、/root/.ssh/github-notes.pub（公钥）
- Git 全局配置：user.name="Notes User"，user.email="notes@example.com"

---

### 创建定时任务

**任务要求：** 每 5 秒同步笔记库

**实现方案：**
1. 创建同步脚本 `sync_notes.sh`，包含以下功能：
   - 检查脚本是否已在运行
   - 定期同步 Git 仓库
   - 处理未暂存的更改
   - 拉取远程仓库更新
   - 推送本地更改
2. 给脚本添加执行权限
3. 使用 `nohup` 命令启动脚本，让它在后台持续运行
4. 创建 systemd 服务文件，确保脚本可以在系统启动时自动运行
5. 忽略同步日志文件的更改，避免每次同步时都有未暂存的更改

**当前状态：**
同步脚本已成功启动，正在每 5 秒同步一次笔记库。脚本的 PID 为 1937。