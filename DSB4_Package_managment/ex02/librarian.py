import os
import subprocess
import sys
import tarfile

def check_virtual_env(expected_env_name="frinksam"):
    current_env = os.getenv("VIRTUAL_ENV")
    if not current_env:
        raise EnvironmentError("Virtual environment is not active.")

    if os.path.basename(current_env) != expected_env_name:
        raise EnvironmentError(f"Not in the correct virtual environment: expected {expected_env_name}.")

def install_libraries():
    requirements_text = "beautifulsoup4\npytest\n"
    with open("temp_requirements.txt", "w") as f:
        f.write(requirements_text)

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "temp_requirements.txt"])

    os.remove("temp_requirements.txt")

def print_libraries():
    subprocess.run([sys.executable, "-m", "pip", "freeze"])

def save_requirements():
    with open("requirements.txt", "w") as f:
        subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=f)

def archive_virtual_env(env_path="../ex00/frinksam", archive_name="frinksam.tar.gz"):
    if not os.path.isdir(env_path):
        raise FileNotFoundError(f"Directory '{env_path}' not found.")

    if os.path.exists(archive_name):
        raise FileExistsError(f"Archive '{archive_name}' already exists.")

    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(env_path, arcname=os.path.basename(env_path))

    print(f"Архив '{archive_name}' создан.")


if __name__ == "__main__":
    check_virtual_env()
    install_libraries()
    print_libraries()
    save_requirements()
    archive_virtual_env()
