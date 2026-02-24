#!/bin/bash
# 自动拉取笔记项目的脚本
# 每 5 秒执行一次 git pull

REPO_DIR="/root/.openclaw/workspace/notebook"
LOG_FILE="$REPO_DIR/pull_logs.txt"
SLEEP_INTERVAL=5

# 检查仓库目录是否存在
if [ ! -d "$REPO_DIR" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Error: Repository directory $REPO_DIR does not exist" >> "$LOG_FILE"
    exit 1
fi

# 进入仓库目录
cd "$REPO_DIR" || exit 1

# 循环拉取
while true; do
    # 记录开始时间
    START_TIME=$(date '+%Y-%m-%d %H:%M:%S')
    
    # 执行 git pull
    PULL_OUTPUT=$(git pull 2>&1)
    EXIT_CODE=$?
    
    # 记录结果
    if [ $EXIT_CODE -eq 0 ]; then
        echo "$START_TIME - Success: $PULL_OUTPUT" >> "$LOG_FILE"
    else
        echo "$START_TIME - Error ($EXIT_CODE): $PULL_OUTPUT" >> "$LOG_FILE"
    fi
    
    # 等待指定时间
    sleep $SLEEP_INTERVAL
done
