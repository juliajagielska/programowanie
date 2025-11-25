from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
import requests

API_URL: str = "https://api.openbrewerydb.org/v1/breweries"

@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]

    def __str__(self) -> str:
        return (
            f"Brewery: {self.name} ({self.brewery_type})\n"
            f"  address: {self.street}, {self.postal_code} {self.city}, "
            f"{self.state}, {self.country}\n"
            f"  współrzędne: {self.latitude}, {self.longitude}\n"
            f"  telefon: {self.phone}\n"
            f"  www: {self.website_url}\n"
        )


def fetch_breweries(limit: int = 20) -> List[Brewery]:
    params = {"per_page": limit}
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    breweries: List[Brewery] = []
    for item in data:
        breweries.append(
            Brewery(
                id=str(item.get("id", "")),
                name=item.get("name", ""),
                brewery_type=item.get("brewery_type"),
                street=item.get("street"),
                city=item.get("city"),
                state=item.get("state"),
                postal_code=item.get("postal_code"),
                country=item.get("country"),
                longitude=float(item["longitude"])
                if item.get("longitude") not in (None, "")
                else None,
                latitude=float(item.get("latitude")) if item.get("latitude") not in (None, "") else None,
                phone=item.get("phone"),
                website_url=item.get("website_url"),
            )
        )
    return breweries


if __name__ == "__main__":
    breweries_list: List[Brewery] = fetch_breweries(limit=20)
    for brewery in breweries_list:
        print(brewery)
        print("-" * 40)






