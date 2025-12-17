from __future__ import annotations

import os
import time
import uuid
from typing import Optional, Dict, Any

import httpx


def new_task_id() -> str:
    return str(uuid.uuid4())


def timestamp() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def safe_filename(name: str) -> str:
    # bardzo proste czyszczenie nazwy
    return name.replace(" ", "_").replace("/", "_").replace("\\", "_")


async def download_image(url: str, save_dir: str = "outputs/downloads") -> str:
    """
    Pobiera obraz z URL i zapisuje na dysku. Zwraca ścieżkę pliku.
    """
    os.makedirs(save_dir, exist_ok=True)
    file_name = f"{timestamp()}_{new_task_id()}.jpg"
    out_path = os.path.join(save_dir, file_name)

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(url)
        r.raise_for_status()
        content_type = r.headers.get("content-type", "")

        # Minimalna kontrola typu
        if "image" not in content_type:
            # i tak zapisujemy, ale informacja może pomóc w debugowaniu
            pass

        with open(out_path, "wb") as f:
            f.write(r.content)

    return out_path