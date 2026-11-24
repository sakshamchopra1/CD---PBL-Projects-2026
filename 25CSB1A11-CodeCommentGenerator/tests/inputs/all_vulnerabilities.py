"""
Multi-Vulnerability Exploit Sample.
Triggers SEC001 (eval), SEC002 (shell=True), SEC003 (hardcoded secret), SEC004 (MD5).
"""
import os
import subprocess
import hashlib

API_SECRET_TOKEN = "sk-live-98f7a63b21c04e928a"


def execute_user_script(script_cmd: str):
    # SEC002: Shell injection with shell=True
    return subprocess.check_output(script_cmd, shell=True)


def insecure_hash_password(raw_pass: str) -> str:
    # SEC004: Insecure cryptographic hash (MD5)
    return hashlib.md5(raw_pass.encode()).hexdigest()


def dynamic_calculate(expr: str):
    # SEC001: Dangerous dynamic evaluation
    return eval(expr)
