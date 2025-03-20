from fastapi import APIRouter, HTTPException
from app.services.tecdoc_api import (
    get_all_manufacturers,
    get_models_by_manufacturer,
    get_vehicle_types,
    get_category_v3,
    get_category_v2,
    get_category_v1,
    get_articles,
    get_vehicle_types_by_model
)

router = APIRouter(prefix="/tecdoc", tags=["TecDoc"])

@router.get("/all-brands-debug")
async def all_brands_debug():
    try:
        data = await get_all_manufacturers()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models/{manufacturer_id}")
async def list_models_for_manufacturer(manufacturer_id: int):
    try:
        data = await get_models_by_manufacturer(manufacturer_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/engine-types/{manufacturer_id}/{model_id}")
async def list_engine_types(manufacturer_id: int, model_id: int):
    try:
        data = await get_vehicle_types_by_model(
            model_id=model_id,
            manufacturer_id=manufacturer_id
        )
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/category-v3/{category_id}/{manufacturer_id}")
async def category_v3(category_id: int, manufacturer_id: int):
    try:
        data = await get_category_v3(category_id, manufacturer_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/category-v2/{vehicle_id}/{manufacturer_id}")
async def category_v2(vehicle_id: int, manufacturer_id: int):
    try:
        data = await get_category_v2(vehicle_id, manufacturer_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/category-v1/{vehicle_id}/{manufacturer_id}")
async def category_v1(vehicle_id: int, manufacturer_id: int):
    try:
        data = await get_category_v1(vehicle_id, manufacturer_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/articles/{vehicle_id}/{product_group_id}/{manufacturer_id}")
async def list_articles(
    vehicle_id: int,
    product_group_id: int,
    manufacturer_id: int,
    lang_id: int = 15,
    country_filter_id: int = 180,
    type_id: int = 1
):
    try:
        data = await get_articles(vehicle_id, product_group_id, manufacturer_id, lang_id, country_filter_id, type_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
