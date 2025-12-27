from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class EventEnvelope(BaseModel):
    event_id: str
    schema_version: str = "1.0"
    trace_id: str
    correlation_id: str
    producer: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    dedupe_key: str
    payload: Dict[str, Any]
    meta: Optional[Dict[str, Any]] = None
