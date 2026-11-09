import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PACKAGES_PATH = os.path.join(ROOT, "packages")
DIST_PATH = os.path.join(ROOT, "dist")


def main():
  print("Packaging extensions..")

  # On Windows, npm also installs an extensionless bash shim that CreateProcess can't run.
  cli = shutil.which("icuewidget.cmd" if os.name == "nt" else "icuewidget")
  if not cli:
    sys.exit("icuewidget CLI not found. Install it with: npm install -g icuewidget-cli")

  os.makedirs(DIST_PATH, exist_ok=True)

  packages = sorted(
    name for name in os.listdir(PACKAGES_PATH)
    if os.path.isfile(os.path.join(PACKAGES_PATH, name, "manifest.json"))
  )
  if not packages:
    sys.exit(f"No widget folders with a manifest.json found in {PACKAGES_PATH}")

  failed = []
  for package in packages:
    print(f"\n== {package}")
    output = os.path.join(DIST_PATH, f"{package}.icuewidget")
    result = subprocess.run([cli, "package", os.path.join(PACKAGES_PATH, package), "-o", output])
    if result.returncode != 0:
      failed.append(package)

  if failed:
    sys.exit(f"\nFailed to package: {', '.join(failed)}")

  print(f"\nPackaged {len(packages)} widget(s) into {DIST_PATH}")


if __name__ == "__main__":
  main()
