return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete AutoBet AI Count Platform</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%); color: #ffffff; min-height: 100vh; }
        .card { background: rgba(26, 31, 58, 0.8); border: 1px solid #00d4ff; border-radius: 15px; }
        .stats-card { background: rgba(0, 212, 255, 0.1); border: 1px solid #00d4ff; border-radius: 15px; padding: 20px; text-align: center; }
        .stats-number { font-size: 2rem; font-weight: bold; color: #00d4ff; }
        .btn-primary { background: linear-gradient(90deg, #00d4ff, #0099cc); border: none; color: #000; }
    </style>
</head>
<body>
    <div class="container-fluid mt-4">
        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header text-center">
                        <h1><i class="fas fa-robot me-2"></i>Complete AutoBet AI Count Platform</h1>
                        <p class="mb-0">专业投注自动化系统 - 成功上线！</p>
                    </div>
                    <div class="card-body">
                        <div class="row mb-4">
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">''' + str(stats[1]) + '''</div>
                                    <div class="text-muted">总利润 (USD)</div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">''' + str(stats[0]) + '''</div>
                                    <div class="text-muted">总交易数</div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">''' + str(int(stats[3] * 100)) + '''%</div>
                                    <div class="text-muted">成功率</div>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">''' + str(stats[2]) + '''</div>
                                    <div class="text-muted">佣金支出</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="row">
                            <div class="col-md-6">
                                <h5>🚀 系统功能模块</h5>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item bg-transparent text-light">✅ 反病毒解决方案 - 系统安全保护</li>
                                    <li class="list-group-item bg-transparent text-light">✅ 反检测解决方案 - 博彩公司无法检测</li>
                                    <li class="list-group-item bg-transparent text-light">✅ Adobe PDF阅读器 - 文档处理功能</li>
                                    <li class="list-group-item bg-transparent text-light">✅ 软件安装中心 - 一键安装所需软件</li>
                                    <li class="list-group-item bg-transparent text-light">✅ Bettingdev投注机器人 - AI智能投注系统</li>
                                    <li class="list-group-item bg-transparent text-light">✅ 实时交易监控 - 24小时不间断</li>
                                    <li class="list-group-item bg-transparent text-light">✅ 数据分析统计 - 智能决策支持</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <h5>🔐 系统信息</h5>
                                <div class="alert alert-info">
                                    <strong>登录账户:</strong> ''' + session.get('username', 'KATHERINE9508') + '''<br>
                                    <strong>系统状态:</strong> <span class="text-success">在线运行</span><br>
                                    <strong>安全等级:</strong> <span class="text-success">最高级</span><br>
                                    <strong>服务器:</strong> <span class="text-primary">Render云端</span>
                                </div>
                                
                                <h5>🎯 快速功能</h5>
                                <div class="row">
                                    <div class="col-6 mb-2">
                                        <a href="/antivirus" class="btn btn-primary w-100 btn-sm">反病毒</a>
                                    </div>
                                    <div class="col-6 mb-2">
                                        <a href="/anti_detection" class="btn btn-success w-100 btn-sm">反检测</a>
                                    </div>
                                    <div class="col-6 mb-2">
                                        <a href="/pdf_reader" class="btn btn-danger w-100 btn-sm">PDF阅读器</a>
                                    </div>
                                    <div class="col-6 mb-2">
                                        <a href="/software_installation" class="btn btn-warning w-100 btn-sm">软件安装</a>
                                    </div>
                                    <div class="col-12">
                                        <a href="/betting_bots" class="btn btn-info w-100">Bettingdev投注机器人</a>
                                    </div>
                                </div>
                                
                                <div class="mt-3">
                                    <a href="/logout" class="btn btn-outline-light w-100">退出登录</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''
