"""Files."""

from pathlib import Path
import platform
import tempfile


def get_log_dir(extend_path: str = None) -> str:
    """
    Get default log directory depending on OS. Extend to application path if path supplied.

    :param extend_path: Extends the system default location;
     creates a new app directory, defaults to None
    :type extend_path: str, optional
    :return: Log Directory for Logs
    :rtype: str
    """
    directory: dict[str, Path] = {
        "darwin": Path.joinpath(Path.home() / "Library/Logs"),
        "linux": Path("/var/log")
    }
    plat: str = platform.system()
    try:
        if extend_path:
            return f"{str(directory[plat.lower()])}/{extend_path}"
        return str(directory[plat.lower()])
    except KeyError:
        if extend_path:
            return f"{str(tempfile.gettempdir())}/{extend_path}"
        return tempfile.gettempdir()


def set_logdir(location: str = "home", extend: str = "") -> str:
    """Set default logDir if not provided."""
    if location.lower() == "home":
        return get_log_home()
    if location.lower() == "default":
        return get_log_dir()
    if location.lower() == "extend":
        return get_log_dir(extend_path=extend)
    raise ValueError(f"Unknown location type {location}")


def get_log_home() -> str:
    """Return current users `home` direcotry."""
    return str(Path.home())


def with_suffix(logName) -> str:
    """Add suffix to logname."""

    return str(Path(logName).with_suffix('.log'))
