import os
import time
import sys

# ---------- Animation Effects ----------
def type_text(text, speed=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def progress_bar(task="Working"):
    type_text(task)
    for _ in range(20):
        sys.stdout.write("▮")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")

# ---------- Core Logic ----------
def auto_rename(folder_path, prefix):
    if not os.path.exists(folder_path):
        type_text("❌ Folder path not found!")
        return

    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    if not files:
        type_text("📭 No files available to rename.")
        return

    progress_bar("🔍 Scanning folder")

    count = 1
    for file in files:
        name, ext = os.path.splitext(file)
        new_name = f"{prefix}_{count}{ext}"

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        type_text(f"✅ {file} ➜ {new_name}")
        count += 1

    type_text("\n🎉 File renaming completed successfully!")

# ---------- Program Start ----------
type_text("🚀 SMART FILE RENAMER TOOL")
type_text("⚙️ Automating file naming made easy\n")

folder = input("📂 Enter folder path: ")
prefix = input("✏️ Enter file name prefix (default: file): ").strip()

if not prefix:
    prefix = "file"

auto_rename(folder, prefix)
type_text("🤖 Automation finished. Keep exploring Python!")
