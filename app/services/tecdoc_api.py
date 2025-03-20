import httpx
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

API_HOST = "tecdoc-catalog.p.rapidapi.com"
API_KEY = os.getenv("RAPIDAPI_KEY")
if not API_KEY:
    raise ValueError("⚠️ RAPIDAPI_KEY não carregada do ambiente!")

headers = {
    "X-RapidAPI-Key": str(API_KEY),
    "X-RapidAPI-Host": API_HOST
}

BASE_URL = f"https://{API_HOST}"

async def get_all_manufacturers():
    url = f"{BASE_URL}/manufacturers/list/lang-id/15/country-filter-id/180/type-id/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

async def get_models_by_manufacturer(
    manufacturer_id: int,
    lang_id: int = 15,
    country_filter_id: int = 180,
    type_id: int = 1
):
    url = (
        f"{BASE_URL}/models/list/manufacturer-id/{manufacturer_id}"
        f"/lang-id/{lang_id}"
        f"/country-filter-id/{country_filter_id}"
        f"/type-id/{type_id}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

# Função para obter os engine types usando o modelId (equivalente a modelSeriesId)
async def get_vehicle_types_by_model(
    model_id: int,
    manufacturer_id: int,
    lang_id: int = 15,
    country_filter_id: int = 180,
    type_id: int = 1
):
    url = (
        f"{BASE_URL}/types/list-vehicles-types/{model_id}"
        f"/manufacturer-id/{manufacturer_id}"
        f"/lang-id/{lang_id}"
        f"/country-filter-id/{country_filter_id}"
        f"/type-id/{type_id}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

async def get_vehicle_types(
    vehicle_id: int,
    manufacturer_id: int,
    lang_id: int = 15,
    country_filter_id: int = 180,
    type_id: int = 1
):
    url = (
        f"{BASE_URL}/types/list-vehicles-types/{vehicle_id}"
        f"/manufacturer-id/{manufacturer_id}"
        f"/lang-id/{lang_id}"
        f"/country-filter-id/{country_filter_id}"
        f"/type-id/{type_id}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

# Category Variant 3
async def get_category_v3(
    category_id: int,
    manufacturer_id: int,
    lang_id: int = 15,
    country_filter_id: int = 180,
    type_id: int = 1
):
    url = (
        f"{BASE_URL}/category/category-products-groups-variant-3/{category_id}"
        f"/manufacturer-id/{manufacturer_id}"
        f"/lang-id/{lang_id}"
        f"/country-filter-id/{country_filter_id}"
        f"/type-id/{type_id}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

# Category Variant 2
async def get_category_v2(
    vehicle_id: int,
    manufacturer_id: int,
    lang_id: int = 4,
    country_filter_id: int = 62,
    type_id: int = 1
):
    url = (
        f"{BASE_URL}/category/category-products-groups-variant-2/{vehicle_id}"
        f"/manufacturer-id/{manufacturer_id}"
        f"/lang-id/{lang_id}"
        f"/country-filter-id/{country_filter_id}"
        f"/type-id/{type_id}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

# Category Variant 1
async def get_category_v1(
    vehicle_id: int,
    manufacturer_id: int,
    lang_id: int = 15,
    country_filter_id: int = 180,
    type_id: int = 1
):
    url = (
        f"{BASE_URL}/category/category-products-groups-variant-1/{vehicle_id}"
        f"/manufacturer-id/{manufacturer_id}"
        f"/lang-id/{lang_id}"
        f"/country-filter-id/{country_filter_id}"
        f"/type-id/{type_id}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

async def get_articles(
    vehicle_id: int,
    product_group_id: int,
    manufacturer_id: int,
    lang_id: int = 15,
    country_filter_id: int = 180,
    type_id: int = 1
):
    url = (
        f"{BASE_URL}/articles/list/vehicle-id/{vehicle_id}"
        f"/product-group-id/{product_group_id}"
        f"/manufacturer-id/{manufacturer_id}"
        f"/lang-id/{lang_id}"
        f"/country-filter-id/{country_filter_id}"
        f"/type-id/{type_id}"
    )
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
