# WebScan-Tools Web漏洞自动化扫描工具
## 项目介绍
基于Python开发的轻量级Web漏洞扫描工具，集成调用sqlmap，可自动化检测SQL注入、XSS跨站脚本漏洞，自动生成漏洞扫描报告。
## 技术栈
Python3、SQLMap、HTTP请求
## 环境依赖
1. 安装Python3环境
2. 本地部署sqlmap工具
## 使用方法
打开命令行执行：
python scan.py -u 目标URL
