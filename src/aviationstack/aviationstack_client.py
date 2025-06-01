import httpx
from aviationstack.config import API_BASE_URL
from envs import FLIGHTSTACK_API_KEY


async def call_aviationstack(endpoint: str, params: dict = None) -> dict:
    if params is None:
        params = {}

    params["access_key"] = FLIGHTSTACK_API_KEY
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()