import os
import shutil
from uuid import uuid4

from fastapi import UploadFile


UPLOAD_DIR = "backend/uploads"


def save_uploaded_file(file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": unique_filename,
        "original_filename": file.filename,
        "file_path": file_path,
        "url": f"/uploads/{unique_filename}",
    }
