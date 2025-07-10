#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os

# 设置服务器端口
PORT = 8000

# 获取当前目录作为服务器根目录
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    # 设置默认目录
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    # 添加 CORS 头，允许跨域请求
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    # 创建服务器
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"服务器启动在端口 {PORT}")
        print(f"请访问: http://localhost:{PORT}")
        print(f"服务目录: {DIRECTORY}")
        print("按 Ctrl+C 停止服务器")
        
        # 启动服务器
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")
