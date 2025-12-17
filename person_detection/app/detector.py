from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Optional
import os
import cv2


@dataclass
class DetectionResult:
    people_count: int
    boxes: List[Tuple[int, int, int, int]]  # (x, y, w, h)


def detect_people_hog(image_bgr) -> DetectionResult:
    """
    Proste wykrywanie ludzi w OpenCV (HOG + SVM).
    Działa “wystarczająco” do projektu, bez modeli DL.
    """
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # detectMultiScale zwraca prostokąty (x,y,w,h)
    boxes, _ = hog.detectMultiScale(
        image_bgr,
        winStride=(8, 8),
        padding=(8, 8),
        scale=1.05
    )

    boxes_list = [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in boxes]
    return DetectionResult(people_count=len(boxes_list), boxes=boxes_list)


def draw_boxes(image_bgr, boxes: List[Tuple[int, int, int, int]]) -> None:
    """
    Rysuje prostokąty na obrazie (modyfikuje image_bgr in-place).
    """
    for (x, y, w, h) in boxes:
        cv2.rectangle(image_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)


def load_image_from_path(image_path: str):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Plik nie istnieje: {image_path}")

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Nie można wczytać obrazu: {image_path}")
    return image


def save_image(image_bgr, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    ok = cv2.imwrite(output_path, image_bgr)
    if not ok:
        raise ValueError(f"Nie udało się zapisać obrazu: {output_path}")
