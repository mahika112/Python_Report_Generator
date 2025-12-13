from datetime import datetime
import platform

with open("report.txt", "w") as f:
    f.write("AUTOMATED CI/CD REPORT\n")
    f.write("=====================\n")
    f.write(f"Generated on: {datetime.now()}\n")
    f.write(f"System: {platform.system()}\n")
    f.write("Status: SUCCESS\n")
