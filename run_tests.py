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

    # Jalankan hanya sekali: generate HTML, JSON, dan ambil output
    result = subprocess.run([
        "pytest",
        test_target,
        f"--html={report_html}",
        "--self-contained-html",
        "--json-report",
        f"--json-report-file={report_json}"
    ], shell=True)

    # Cari durasi test
    match = re.search(r"=+.+in (\d+\.\d+)s", result.stdout)
    duration = match.group(1) + " detik" if match else "N/A"

    # Ambil waktu WIB
    now_wib = datetime.now(pytz.timezone("Asia/Jakarta"))
    waktu = now_wib.strftime("%d %b %Y | %H:%M WIB")

    # Ambil ringkasan test dari file JSON
    total, passed, failed = parse_test_result_json(report_json)

    # Susun email
    subject = f"Automation Test Report for GenMaju - {waktu}"
    body = f"""
    <b>Automation Test Report for <a href="https://www.generasimaju.co.id/">https://www.generasimaju.co.id</a></b><br><br>

    <b>Summary:</b><br>
    • Total Test: <b>{total}</b><br>
    • Passed : <b>{passed}</b><br>
    • Failed : <b>{failed}</b><br>
    • Duration : <b>{duration}</b><br><br>

    <b>Check the attached HTML report for the full test results</b><br>
    <i>This report is auto-generated and maintained by Mazway</i>
    """

    recipients = os.getenv("EMAIL_TO", "").split(",")

    print("EMAIL_USER:", os.getenv("EMAIL_USER"))
    print("EMAIL_PASS:", "OK" if os.getenv("EMAIL_PASS") else "MISSING")

    # Kirim email hanya jika file HTML tersedia
    if os.path.exists(report_html):
        send_email_with_attachment(
            subject=subject,
            body=body,
            to_emails=recipients,
            from_email=os.getenv("EMAIL_FROM"),
            smtp_user=os.getenv("EMAIL_USER"),
            smtp_pass=os.getenv("EMAIL_PASS"),
            attachment_path=report_html
        )
    else:
        print("Gagal mengirim email: file report HTML tidak ditemukan.")
        