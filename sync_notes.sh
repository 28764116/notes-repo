#!/bin/bash

# 笔记同步脚本
# 每 5 秒同步一次 Git 仓库

LOG_FILE="/root/.openclaw/workspace/sync_notes.log"
REPO_DIR="/root/.openclaw/workspace"

# 检查是否已经在运行
if [ -f /tmp/sync_notes.pid ]; then
    PID=$(cat /tmp/sync_notes.pid)
    if kill -0 $PID 2>/dev/null; then
        echo "$(date +'%Y-%m-%d %H:%M:%S') - 同步脚本已在运行 (PID: $PID)" >> $LOG_FILE
        exit 1
    else
        rm -f /tmp/sync_notes.pid
    fi
fi

# 保存当前 PID
echo $$ > /tmp/sync_notes.pid

# 同步循环
while true; do
    echo "============================================" >> $LOG_FILE
    echo "$(date +'%Y-%m-%d %H:%M:%S') - 开始同步笔记库" >> $LOG_FILE
    
    cd $REPO_DIR
    git add . >> $LOG_FILE 2>&1
    
    # 检查是否有需要提交的更改
    if git diff --staged | grep -q "."; then
        git commit -m "同步笔记 - $(date +'%Y-%m-%d %H:%M:%S')" >> $LOG_FILE 2>&1
    fi
    
    # 先尝试拉取，如有冲突则合并
    git pull origin master >> $LOG_FILE 2>&1
    git push origin master >> $LOG_FILE 2>&1
    
    echo "$(date +'%Y-%m-%d %H:%M:%S') - 同步完成" >> $LOG_FILE
    echo "============================================" >> $LOG_FILE
    echo >> $LOG_FILE
    
    sleep 5
done