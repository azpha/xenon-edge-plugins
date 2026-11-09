import os
import subprocess

PACKAGES_PATH = os.path.abspath("./packages")

def main():
  print("Packaging extensions..")

  packages = [x for x in os.listdir(PACKAGES_PATH) if "." not in x]
  if not os.path.exists("./dist"):
    os.mkdir("./dist")

  for package in packages:
    try:
      subprocess.run(["icuewidget", "package", "-o", f"../../dist/{package}"], cwd=os.path.join(PACKAGES_PATH, package), shell=True)
    except Exception as e:
      print(f"Failed to package {package}")
      print(e)

  print("Packaged!")

if __name__ == "__main__":
  main()