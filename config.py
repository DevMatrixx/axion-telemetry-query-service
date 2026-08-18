"""
Axion Telemetry Query Service - Configuration
"""

import os
from dataclasses import dataclass

@dataclass
class Settings:
    # PostgreSQL connection string
    # Format: postgresql://<user>:<password>@<host>:<port>/<database>
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@123@10.244.0.47:5432/axiondb",
    )
    # Allows configuring a different port, e.g., if we run multiple services
    PORT: int = int(os.getenv("PORT", "8000"))

settings = Settings()
