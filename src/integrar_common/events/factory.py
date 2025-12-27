from __future__ import annotations
import uuid
from datetime import datetime, timezone

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def envelope(*, producer: str, correlation_id: str, payload: dict, dedupe_key: str, trace_id: str | None = None) -> dict:
    return {
        "event_id": str(uuid.uuid4()),
        "schema_version": "1.0",
        "trace_id": trace_id or str(uuid.uuid4()),
        "correlation_id": correlation_id,
        "producer": producer,
        "created_at": now_iso(),
        "dedupe_key": dedupe_key,
        "payload": payload,
    }

def segmentos_prontos_event(
    *,
    producer: str,
    processo_id: str,
    artefato_id: str,
    segmento_ids: list[str],
    pipeline_version: str,
) -> dict:
    payload = {
        "processo_id": processo_id,
        "artefato_id": artefato_id,
        "segmento_ids": segmento_ids,
        "pipeline_version": pipeline_version,
    }
    dedupe_key = f"{artefato_id}:segmentos_prontos:{pipeline_version}:{len(segmento_ids)}"
    return envelope(producer=producer, correlation_id=processo_id, payload=payload, dedupe_key=dedupe_key)
