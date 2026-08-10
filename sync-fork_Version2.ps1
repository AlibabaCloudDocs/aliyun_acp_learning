Write-Host "开始同步fork仓库..." -ForegroundColor Green

# 1. 添加上游仓库（如果还没有）
$remotes = git remote
if ($remotes -notcontains "upstream") {
    Write-Host "添加upstream源..."
    git remote add upstream https://github.com/AlibabaCloudDocs/aliyun_acp_learning.git
} else {
    Write-Host "upstream源已存在"
}

# 2. 验证远程源
Write-Host "`n当前远程源：" -ForegroundColor Cyan
git remote -v

# 3. 获取上游最新更改
Write-Host "`n获取上游最新更改..." -ForegroundColor Yellow
git fetch upstream

# 4. 切换到main分支
Write-Host "切换到main分支..." -ForegroundColor Yellow
git checkout main

# 5. 合并上游更改
Write-Host "合并上游更改..." -ForegroundColor Yellow
git merge upstream/main

# 6. 推送到你的fork
Write-Host "推送到你的fork..." -ForegroundColor Yellow
git push origin main

Write-Host "`n✅ 同步完成！" -ForegroundColor Green