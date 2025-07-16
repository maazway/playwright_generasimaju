import subprocess
import os
import sys
import json
import time
from datetime import datetime
from dotenv import load_dotenv
from utils.email_report import send_email_with_attachment

load_dotenv()

def wait_for_json(path, timeout=5):
    for _ in range(timeout * 10):
        if os.path.exists(path):
            return True
        time.sleep(0.1)
    return False

def parse_test_result_json(path):
    try:
        with open(path, "r") as f:
            report = json.load(f)
        total = report["summary"]["total"]
        passed = report["summary"]["passed"]
        failed = report["summary"]["failed"]
        return total, passed, failed
    except Exception:
        return 0, 0, 0

if __name__ == "__main__":
    test_target = sys.argv[1] if len(sys.argv) > 1 else "tests/"
    report_path = "test_report.html"
    json_path = "report.json"

    # Jalankan pytest via subprocess
    cmd = [
        "pytest",
        test_target,
        f"--html={report_path}",
        "--self-contained-html",
        "--json-report",
        f"--json-report-file={json_path}"
    ]

    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Pastikan JSON selesai ditulis
    if wait_for_json(json_path):
        total, passed, failed = parse_test_result_json(json_path)
    else:
        total, passed, failed = 0, 0, 0

    now_wib = datetime.utcnow().timestamp() + (7 * 3600)
    waktu = datetime.fromtimestamp(now_wib).strftime("%d %b %Y | %H:%M WIB")

    subject = f"TEST REPORT - {waktu}"
    body = f"""Hasil test selesai:
- Total: {total}
- Passed: {passed}
- Failed: {failed}
"""

    recipients = os.getenv("EMAIL_TO", "").split(",")

    send_email_with_attachment(
        subject=subject,
        body=body,
        to_emails=recipients,
        from_email=os.getenv("EMAIL_FROM"),
        smtp_user=os.getenv("EMAIL_USER"),
        smtp_pass=os.getenv("EMAIL_PASS"),
        attachment_path=report_path
    )
