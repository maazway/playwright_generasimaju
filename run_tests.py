import subprocess
import os
import sys
from datetime import datetime
import pytz
from dotenv import load_dotenv
from utils.email_report import send_email_with_attachment

load_dotenv()

if __name__ == "__main__":
    # Target file/folder test
    test_target = sys.argv[1] if len(sys.argv) > 1 else "tests/"

    # Nama file HTML report
    report_path = "test_report.html"

    # Pastikan di root folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    # Jalankan pytest dengan HTML report
    # Tampilkan langsung ke terminal (tanpa capture_output)
    subprocess.run([
        "pytest",
        test_target,
        f"--html={report_path}",
        "--self-contained-html"
    ], shell=True)

    # Waktu WIB timezone-aware
    now_wib = datetime.now(pytz.timezone("Asia/Jakarta"))
    waktu = now_wib.strftime("%d %b %Y | %H:%M WIB")

    # Hitung hasil dari isi HTML report
    with open(report_path, "r", encoding="utf-8") as f:
        html = f.read()
        passed = html.count("✔")
        failed = html.count("✘")
        total = passed + failed

    # Buat subject dan body
    subject = f"TEST REPORT - {waktu}"
    body = f"""Hasil test selesai:
- Total: {total}
- Passed: {passed}
- Failed: {failed}
"""

    # Kirim email
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

