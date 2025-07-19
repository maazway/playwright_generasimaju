import subprocess
import os
import sys
import json
import re
from datetime import datetime
import pytz
from dotenv import load_dotenv
from utils.email_report import send_email_with_attachment

load_dotenv()

def parse_test_result_json(json_path):
    """Ambil total, passed, failed dari file JSON report."""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            report = json.load(f)
        total = report.get("summary", {}).get("total", 0)
        passed = report.get("summary", {}).get("passed", 0)
        failed = report.get("summary", {}).get("failed", 0)
        return total, passed, failed
    except Exception:
        return 0, 0, 0

if __name__ == "__main__":
    test_target = sys.argv[1] if len(sys.argv) > 1 else "tests/"
    report_html = "test_report.html"
    report_json = "report.json"

    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    # Jalankan test dan ambil stdout
    result = subprocess.run([
        "pytest",
        test_target,
        f"--html={report_html}",
        "--self-contained-html",
        "--json-report",
        f"--json-report-file={report_json}"
    ], capture_output=True, text=True, shell=True)

    # Cari durasi dari output
    match = re.search(r"=+.+in (\d+\.\d+)s", result.stdout)
    duration = match.group(1) + " detik" if match else "N/A"

    # Ambil waktu WIB
    now_wib = datetime.now(pytz.timezone("Asia/Jakarta"))
    waktu = now_wib.strftime("%d %b %Y | %H:%M WIB")

    total, passed, failed = parse_test_result_json(report_json)

    subject = f"Automation Test Report for GenMaju - {waktu}"
    body = f"""
<b>Automation Test Report for <a href="https://www.generasimaju.co.id/">https://www.generasimaju.co.id</a></b><br><br>

<b>Summary:</b><br>
• Total Test: <b>{total}</b><br>
• Passed : <b>{passed}</b><br>
• Failed : <b>{failed}</b><br>
• Duration : <b>{duration}</b><br><br>

<i>Check the attached HTML report for the full test results</i><br><br>

<b>This report is auto-generated and maintained by Mazway</b>
"""

    recipients = os.getenv("EMAIL_TO", "").split(",")

    send_email_with_attachment(
        subject=subject,
        body=body,
        to_emails=recipients,
        from_email=os.getenv("EMAIL_FROM"),
        smtp_user=os.getenv("EMAIL_USER"),
        smtp_pass=os.getenv("EMAIL_PASS"),
        attachment_path=report_html
    )
