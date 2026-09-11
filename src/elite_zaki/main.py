"""
Elite Zaki application entry point.
"""

from .config import DEFAULT_CONFIG


def main() -> None:
    """Start the Elite Zaki application."""

    print(f"{DEFAULT_CONFIG.project_name} v{DEFAULT_CONFIG.version}")
    print(f"Operating mode: {DEFAULT_CONFIG.mode}")
    print("System initialized successfully.")


if __name__ == "__main__":
    main()
