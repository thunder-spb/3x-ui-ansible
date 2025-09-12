import subprocess
import re
import pytest

def test_sshd():
    pattern = r"^PermitRootLogin prohibit-password$"
    file_path = '/etc/ssh/sshd_config'
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    match = re.search(pattern, content, re.MULTILINE)
    assert match is not None, f"Pattern '{pattern}' not found in '{file_path}'"

def test_docker_binary():
    try:
        info_result = subprocess.run(["/usr/bin/docker", "info"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        assert "Containers" in info_result.stdout
    except subprocess.CalledProcessError as e:
        pytest.fail(f"The 'docker' command exited with a non-zero status code. Error: {e.stderr}")

def test_iptables():
    info_result = subprocess.run(["/usr/sbin/nft", "list", "ruleset"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    assert "tcp dport 2020 counter" in info_result.stdout
