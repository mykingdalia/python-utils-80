from typing import Final

# Constants used in the autoclicker utility

CLICK_INTERVAL: Final[float] = 0.1  # Time in seconds between clicks
MAX_CLICKS: Final[int] = 1000  # Maximum number of clicks allowed
MIN_CLICKS: Final[int] = 1  # Minimum number of clicks

# Mouse button constants
class MouseButton:
    LEFT: Final[int] = 1
    RIGHT: Final[int] = 2
    MIDDLE: Final[int] = 3

# Default configuration settings for the autoclicker
DEFAULT_SETTINGS: Final[dict[str, int]] = {
    'clicks': 100,
    'interval': 0.1,
    'button': MouseButton.LEFT
}

