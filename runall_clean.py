import os
import sys
import json
import re
import subprocess
from datetime import datetime

import pytz
from dotenv import load_dotenv

from utils.email_report import send_email_with_attachment

load_dotenv()


def parse_test_result_json(json_path):
    """Parse test result JSON report and return total, passed, and failed counts."""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            report = json.load(f)
        summary = report.get("summary", {})
        return summary.get("total", 0), summary.get("passed", 0), summary.get("failed", 0)
    except Exception as e:
        print(f"Failed to parse JSON report: {e}")
        return 0, 0, 0


def run_pytest_live(command):
    """Run pytest command and stream output in real-time."""
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )

    full_output = ""
    for line in process.stdout:
        print(line, end="")
        full_output += line

    process.wait()
    return full_output


def main():
    test_target = sys.argv[1] if len(sys.argv) > 1 else "tests/"
    report_html = "test_report.html"
    report_json = "report.json"

    # Ensure we are in base project directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    # Run pytest with live output
    pytest_command = (
        f"pytest -s {test_target} "
        f"--html={report_html} --self-contained-html "
        f"--json-report --json-report-file={report_json} "
        f"--maxfail=1000 --disable-warnings"
    )

    print("Running tests...\n")
    full_output = run_pytest_live(pytest_command)

    # Extract duration from output
    duration_match = re.search(r"in (\d+\.\d+)s", full_output)
    duration = f"{duration_match.group(1)} seconds" if duration_match else "N/A"

    # Timestamp
    now_wib = datetime.now(pytz.timezone("Asia/Jakarta"))
    waktu = now_wib.strftime("%d %b %Y | %H:%M WIB")

    # Parse JSON report
    total, passed, failed = parse_test_result_json(report_json)

    # Build email
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
    from_email = os.getenv("EMAIL_FROM")
    smtp_user = os.getenv("EMAIL_USER")
    smtp_pass = os.getenv("EMAIL_PASS")

    # Uncomment if sending email is needed
    if smtp_user and smtp_pass:
        try:
            send_email_with_attachment(
                subject=subject,
                body=body,
                to_emails=recipients,
                from_email=from_email,
                smtp_user=smtp_user,
                smtp_pass=smtp_pass,
                attachment_path=report_html
            )
        except Exception as e:
            print(f"Failed to send email: {e}")
    else:
        print("EMAIL_USER or EMAIL_PASS not set in .env — email not sent.")


if __name__ == "__main__":
    main()
