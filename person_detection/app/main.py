from __future__ import annotations

import os
from typing import Optional, Dict, Any

from fastapi import FastAPI, Query, UploadFile, File, HTTPException
from pydantic import BaseModel

from app.detector import (
    load_image_from_path,
    detect_people_hog,
    draw_boxes,
    save_image,
)
from app.io_utils import new_task_id, timestamp, safe_filename, download_image


app = FastAPI(title="Person Detection API", version="1.0.0")


# --- Prosta “baza” zadań w pamięci (bez kolejki) ---
TASKS: Dict[str, Dict[str, Any]] = {}


class TaskCreated(BaseModel):
    task_id: str


class TaskStatus(BaseModel):
    task_id: str
    status: str  # "processing" | "done" | "error"
    result: Optional[dict] = None
    error: Optional[str] = None


def _run_detection(image_path: str, draw: bool) -> dict:
    """
    Robi wykrycie i opcjonalnie zapisuje obraz z prostokątami do outputs/.
    """
    image = load_image_from_path(image_path)
    det = detect_people_hog(image)

    output_image_path = None
    if draw:
        draw_boxes(image, det.boxes)
        base = os.path.basename(image_path)
        base = os.path.splitext(base)[0]
        output_image_path = os.path.join("outputs", f"{base}_{timestamp()}_boxed.jpg")
        save_image(image, output_image_path)

    return {
        "image_path": image_path,
        "people_count": det.people_count,
        "boxed_image_path": output_image_path,
    }


def _create_and_finish_task(result: dict) -> str:
    """
    Bez kolejki: tworzymy task_id i od razu ustawiamy status done.
    """
    task_id = new_task_id()
    TASKS[task_id] = {"status": "done", "result": result, "error": None}
    return task_id


@app.get("/count-from-path", response_model=TaskCreated)
def count_from_path(
    image_path: str = Query(..., description="Ścieżka do pliku zdjęcia, np. images/grupa.jpg"),
    draw: bool = Query(True, description="Czy rysować prostokąty i zapisać wynik do outputs/")
):
    try:
        result = _run_detection(image_path=image_path, draw=draw)
        task_id = _create_and_finish_task(result)
        return {"task_id": task_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/count-from-url", response_model=TaskCreated)
async def count_from_url(
    url: str = Query(..., description="URL do zdjęcia w Internecie"),
    draw: bool = Query(True, description="Czy rysować prostokąty i zapisać wynik do outputs/")
):
    """
    GET: pobiera obraz z Internetu (URL), zapisuje lokalnie, liczy osoby.
    """
    task_id = new_task_id()
    TASKS[task_id] = {"status": "processing", "result": None, "error": None}

    try:
        downloaded_path = await download_image(url)
        result = _run_detection(image_path=downloaded_path, draw=draw)
        TASKS[task_id] = {"status": "done", "result": result, "error": None}
        return {"task_id": task_id}
    except Exception as e:
        TASKS[task_id] = {"status": "error", "result": None, "error": str(e)}
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/count-from-upload", response_model=TaskCreated)
async def count_from_upload(
    file: UploadFile = File(...),
    draw: bool = Query(True, description="Czy rysować prostokąty i zapisać wynik do outputs/")
):
    """
    POST: przyjmuje upload zdjęcia, zapisuje, liczy osoby.
    """
    task_id = new_task_id()
    TASKS[task_id] = {"status": "processing", "result": None, "error": None}

    try:
        os.makedirs("outputs/uploads", exist_ok=True)
        filename = safe_filename(file.filename or "upload.jpg")
        saved_path = os.path.join("outputs/uploads", f"{timestamp()}_{task_id}_{filename}")

        content = await file.read()
        with open(saved_path, "wb") as f:
            f.write(content)

        result = _run_detection(image_path=saved_path, draw=draw)
        TASKS[task_id] = {"status": "done", "result": result, "error": None}
        return {"task_id": task_id}
    except Exception as e:
        TASKS[task_id] = {"status": "error", "result": None, "error": str(e)}
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/task/{task_id}", response_model=TaskStatus)
def get_task_status(task_id: str):
    """
    Endpoint statusu zadania (bez kolejki — ale trzymamy wynik w pamięci).
    """
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Nie ma takiego task_id")

    data = TASKS[task_id]
    return {
        "task_id": task_id,
        "status": data["status"],
        "result": data["result"],
        "error": data["error"],
    }