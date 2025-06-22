from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
import random

app = Flask(__name__)
app.secret_key = "autobet_ai_count_complete_2025"

@app.route("/")
def index():
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    stats = [156, 1250.50, 250.10, 0.78]
    recent_trades = [
        ("百家乐", 50, "win", 45, "2025-01-22 10:15:30"),
        ("21点", 30, "loss", -30, "2025-01-22 10:12:15"),
        ("Bettingdev机器人", 100, "win", 180, "2025-01-22 10:01:10")
    ]
    
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
        body { 
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%); 
            color: #ffffff; 
            min-height: 100vh; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .card { 
            background: rgba(26, 31, 58, 0.8); 
            border: 1px solid #00d4ff; 
            border-radius: 15px; 
            backdrop-filter: blur(10px);
        }
        .card-header {
            background: linear-gradient(90deg, #00d4ff, #0099cc);
            border-radius: 15px 15px 0 0 !important;
            color: #000;
            font-weight: bold;
        }
        .stats-card { 
            background: rgba(0, 212, 255, 0.1); 
            border: 1px solid #00d4ff; 
            border-radius: 15px; 
            padding: 20px; 
            text-align: center;
            transition: transform 0.3s ease;
        }
        .stats-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
        }
        .stats-number { 
            font-size: 2rem; 
            font-weight: bold; 
            color: #00d4ff; 
        }
        .btn-primary { 
            background: linear-gradient(90deg, #00d4ff, #0099cc); 
            border: none; 
            color: #000; 
            font-weight: bold;
        }
        .btn-primary:hover {
            background: linear-gradient(90deg, #0099cc, #00d4ff);
            transform: translateY(-2px);
        }
        .pulse {
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        .list-group-item {
            background: transparent !important;
            border-color: #233554 !important;
        }
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
                        <span class="badge bg-success pulse">系统在线</span>
                    </div>
                    <div class="card-body">
                        <!-- 统计卡片 -->
                        <div class="row mb-4">
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">$''' + str(stats[1]) + '''</div>
                                    <div class="text-muted">总利润 (USD)</div>
                                    <i class="fas fa-dollar-sign fa-2x mt-2" style="color: #00ff88;"></i>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">''' + str(stats[0]) + '''</div>
                                    <div class="text-muted">总交易数</div>
                                    <i class="fas fa-exchange-alt fa-2x mt-2" style="color: #00d4ff;"></i>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">''' + str(int(stats[3] * 100)) + '''%</div>
                                    <div class="text-muted">成功率</div>
                                    <i class="fas fa-target fa-2x mt-2" style="color: #ffaa00;"></i>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stats-card">
                                    <div class="stats-number">$''' + str(stats[2]) + '''</div>
                                    <div class="text-muted">佣金支出</div>
                                    <i class="fas fa-percentage fa-2x mt-2" style="color: #ff4757;"></i>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 功能模块 -->
                        <div class="row">
                            <div class="col-md-6">
                                <div class="card mb-4">
                                    <div class="card-header">
                                        <h5><i class="fas fa-rocket me-2"></i>系统功能模块</h5>
                                    </div>
                                    <div class="card-body">
                                        <ul class="list-group list-group-flush">
                                            <li class="list-group-item text-light">
                                                <i class="fas fa-shield-alt text-primary me-2"></i>反病毒解决方案 - 系统安全保护
                                            </li>
                                            <li class="list-group-item text-light">
                                                <i class="fas fa-user-secret text-success me-2"></i>反检测解决方案 - 博彩公司无法检测
                                            </li>
                                            <li class="list-group-item text-light">
                                                <i class="fas fa-file-pdf text-danger me-2"></i>Adobe PDF阅读器 - 文档处理功能
                                            </li>
                                            <li class="list-group-item text-light">
                                                <i class="fas fa-download text-warning me-2"></i>软件安装中心 - 一键安装所需软件
                                            </li>
                                            <li class="list-group-item text-light">
                                                <i class="fas fa-robot text-info me-2"></i>Bettingdev投注机器人 - AI智能投注系统
                                            </li>
                                            <li class="list-group-item text-light">
                                                <i class="fas fa-chart-line text-success me-2"></i>实时交易监控 - 24小时不间断
                                            </li>
                                            <li class="list-group-item text-light">
                                                <i class="fas fa-chart-bar text-primary me-2"></i>数据分析统计 - 智能决策支持
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="card mb-4">
                                    <div class="card-header">
                                        <h5><i class="fas fa-info-circle me-2"></i>系统信息</h5>
                                    </div>
                                    <div class="card-body">
                                        <div class="alert alert-info">
                                            <strong>🔐 登录账户:</strong> ''' + session.get('username', 'KATHERINE9508') + '''<br>
                                            <strong>🟢 系统状态:</strong> <span class="text-success">在线运行</span><br>
                                            <strong>🛡️ 安全等级:</strong> <span class="text-success">最高级</span><br>
                                            <strong>🌐 服务器:</strong> <span class="text-primary">Render云端</span><br>
                                            <strong>⚡ 响应时间:</strong> <span class="text-warning">< 100ms</span>
                                        </div>
                                        
                                        <h6>🎯 快速功能访问</h6>
                                        <div class="row">
                                            <div class="col-6 mb-2">
                                                <a href="/antivirus" class="btn btn-primary w-100 btn-sm">
                                                    <i class="fas fa-shield-alt me-1"></i>反病毒
                                                </a>
                                            </div>
                                            <div class="col-6 mb-2">
                                                <a href="/anti_detection" class="btn btn-success w-100 btn-sm">
                                                    <i class="fas fa-user-secret me-1"></i>反检测
                                                </a>
                                            </div>
                                            <div class="col-6 mb-2">
                                                <a href="/pdf_reader" class="btn btn-danger w-100 btn-sm">
                                                    <i class="fas fa-file-pdf me-1"></i>PDF阅读器
                                                </a>
                                            </div>
                                            <div class="col-6 mb-2">
                                                <a href="/software_installation" class="btn btn-warning w-100 btn-sm">
                                                    <i class="fas fa-download me-1"></i>软件安装
                                                </a>
                                            </div>
                                            <div class="col-12 mb-3">
                                                <a href="/betting_bots" class="btn btn-info w-100">
                                                    <i class="fas fa-robot me-2"></i>Bettingdev投注机器人
                                                </a>
                                            </div>
                                        </div>
                                        
                                        <div class="text-center">
                                            <a href="/logout" class="btn btn-outline-light w-100">
                                                <i class="fas fa-sign-out-alt me-2"></i>退出登录
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 最近交易 -->
                        <div class="row">
                            <div class="col-12">
                                <div class="card">
                                    <div class="card-header">
                                        <h5><i class="fas fa-history me-2"></i>最近交易记录</h5>
                                    </div>
                                    <div class="card-body">
                                        <div class="table-responsive">
                                            <table class="table table-dark table-hover">
                                                <thead>
                                                    <tr>
                                                        <th>游戏类型</th>
                                                        <th>下注金额</th>
                                                        <th>结果</th>
                                                        <th>盈亏</th>
                                                        <th>时间</th>
                                                    </tr>
                                                </thead>
                                                <tbody>''' + ''.join([f'''
                                                    <tr>
                                                        <td>{trade[0]}</td>
                                                        <td>${trade[1]}</td>
                                                        <td><span class="badge {'bg-success' if trade[2] == 'win' else 'bg-danger'}">{trade[2]}</span></td>
                                                        <td class="{'text-success' if trade[3] > 0 else 'text-danger'}">${trade[3]}</td>
                                                        <td>{trade[4]}</td>
                                                    </tr>''' for trade in recent_trades]) + '''
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

@app.route("/antivirus")
def antivirus():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("antivirus.html")

@app.route("/anti_detection")
def anti_detection():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("anti_detection.html")

@app.route("/pdf_reader")
def pdf_reader():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("pdf_reader.html")

@app.route("/software_installation")
def software_installation():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("software_installation.html")

@app.route("/betting_bots")
def betting_bots():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("betting_bots.html")

@app.route("/trading")
def trading():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("trading.html")

@app.route("/analytics")
def analytics():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("analytics.html")

@app.route("/settings")
def settings():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("settings.html")

@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("index"))
    return render_template("profile.html")

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username == "KATHERINE9508" and password == "asd123456":
        session["user_id"] = 1
        session["username"] = username
        return jsonify({"success": True, "redirect": "/dashboard"})
    else:
        return jsonify({"success": False, "message": "用户名或密码错误"})

@app.route("/api/system_stats")
def api_system_stats():
    return jsonify({
        "success": True,
        "data": {
            "cpu_usage": random.uniform(30, 70),
            "memory_usage": random.uniform(40, 80),
            "active_users": 1,
            "today_trades": random.randint(20, 50),
            "total_profit": round(random.uniform(1000, 2000), 2),
            "running_bots": 4,
            "antivirus_status": "已激活",
            "anti_detection_status": "已启用"
        }
    })

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
