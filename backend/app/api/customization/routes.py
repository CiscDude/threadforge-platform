from fastapi import APIRouter
from app.services.customization_service import CustomizationService

router = APIRouter(
    prefix="/customizations",
    tags=["Customizations"]
)


@router.get("/colors")
def get_colors():
    return CustomizationService.get_available_colors()


@router.get("/sizes")
def get_sizes():
    return CustomizationService.get_available_sizes()


@router.get("/print-locations")
def get_print_locations():
    return CustomizationService.get_available_print_locations()


@router.post("/price")
def calculate_price(
    color: str,
    size: str,
    print_location: str
):
    return CustomizationService.calculate_customization_price(
        color,
        size,
        print_location
    )
