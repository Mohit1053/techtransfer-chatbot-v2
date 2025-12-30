# Configuration Management
# Copy this file to config.py and update with your actual API keys

from dotenv import load_dotenv
import os
import random
import time
import logging
from collections import defaultdict
from threading import RLock

load_dotenv()

if not logging.getLogger().hasHandlers():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - [%(filename)s.%(funcName)s:%(lineno)d] - %(message)s'
    )

# =============================================================================
# SECURITY WARNING: NEVER hardcode API keys here!
# Load keys from environment variables only.
# =============================================================================

# Load API keys from environment
GOOGLE_API_KEYS = os.getenv("GOOGLE_API_KEYS", "").split(",")
GOOGLE_API_KEYS = [key.strip() for key in GOOGLE_API_KEYS if key.strip()]

# Fallback to single key
if not GOOGLE_API_KEYS:
    single_key = os.getenv("GOOGLE_API_KEY", "")
    if single_key:
        GOOGLE_API_KEYS = [single_key]

# Rate limiting configuration
REQUEST_LIMITS = {
    "per_minute": 60,
    "per_day": 1500,
}

# Key usage tracking
_key_usage = defaultdict(lambda: {"count": 0, "last_reset": time.time()})
_lock = RLock()


def get_available_api_key():
    """Get an available API key with rate limiting."""
    if not GOOGLE_API_KEYS:
        raise ValueError(
            "No Google API keys found. "
            "Please set GOOGLE_API_KEY or GOOGLE_API_KEYS in your .env file."
        )
    
    with _lock:
        current_time = time.time()
        
        for key in GOOGLE_API_KEYS:
            usage = _key_usage[key]
            
            # Reset counter every minute
            if current_time - usage["last_reset"] > 60:
                usage["count"] = 0
                usage["last_reset"] = current_time
            
            # Check rate limit
            if usage["count"] < REQUEST_LIMITS["per_minute"]:
                usage["count"] += 1
                logging.info(f"Using API Key: {key[:10]}...")
                return key
        
        raise ValueError("All API keys are rate-limited. Please wait.")


def get_random_google_api_key():
    """Get a random Google API key from the pool."""
    if not GOOGLE_API_KEYS:
        raise ValueError(
            "No Google API keys found. "
            "Please set GOOGLE_API_KEY or GOOGLE_API_KEYS in your .env file."
        )
    key = random.choice(GOOGLE_API_KEYS)
    print(f"Using API Key: {key[:10]}...")
    return key
