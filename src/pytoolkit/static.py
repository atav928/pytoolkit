# pylint: disable=line-too-long
"""Global Static Vars."""

from typing import cast

ENCODING: str = "utf-8"

# See https://www.linuxtrainingacademy.com/all-umasks/
FILE_UMASK_PERMISSIONS = {
    "default": 0o40775,  # umask 002 rw-rw-r- rwxrwx-r
    "restrictive": 0o40770,  # umask 037 rw-r--- rwxr---
    "root": 0o40755,  # umask 022 rw-r-r- rwxr-xr-x
}

NONETYPE: None = cast(None, object())
DEFAULT_TO: list[str] = ["john.doe@acme.com"]
DEFAULT_FROM: str = "python-script@acme.com"
DEFAULT_CC: list[str] = [""]
DEFAULT_BCC: list[str] = [""]
TMP_PEM_POSTFIX = "_pytookit.pem"
PEM_REGEX = (
    r".*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}_pytoolkit\.pem$"
)

RE_DOMAIN = r".*\.(com|net|gov)$"
RE_IP4 = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
SANATIZE_KEYS = [
    "password",
    "cacontext",
    "log",
    "plaintext",
    "token",
    "jwt",
    "cert",
    "authorization",
    "auth",
]
CONFIG_PATH = "{}/{}.{}"
SPLUNK_HEC_EVENTPATH = "services/collector/event"
