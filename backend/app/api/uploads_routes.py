from fastapi import APIRouter, File, UploadFile

from app.services.file_upload_service import save_uploaded_file


router = APIRouter(prefix="/uploads", tags=["Uploads"])


@router.post("/")
def upload_file(file: UploadFile = File(...)):
    return save_uploaded_file(file)
