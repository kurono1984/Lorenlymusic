from typing import TypedDict

import reflex as rx

BANDCAMP_URL = "https://lorenly.bandcamp.com"


class ShopItem(TypedDict):
    key: str
    title: str
    external: str


class ShopState(rx.State):
    """Enlaces reales del catálogo de Lorenly Music en Bandcamp."""

    unavailable: list[str] = []

    items: list[ShopItem] = [
        {
            "key": "magnolia",
            "title": "Magnolia (Hatsune Miku feat Lorenly)",
            "external": f"{BANDCAMP_URL}/track/magnolia-hatsune-miku-feat-lorenly",
        },
        {
            "key": "calida-esperanza",
            "title": "Cálida Esperanza (Megpoid Gumi feat Lorenly)",
            "external": f"{BANDCAMP_URL}/track/c-lida-esperanza-megpoid-gumi-feat-lorenly",
        },
        {
            "key": "si",
            "title": "Sí (Silvana & Ernesto · Lorenly)",
            "external": f"{BANDCAMP_URL}/track/s-silvana-ernesto-lorenly",
        },
    ]

    @rx.var
    def item_count(self) -> int:
        return len(self.items)

    @rx.event
    def mark_unavailable(self, key: str):
        if key not in self.unavailable:
            self.unavailable.append(key)

    @rx.event
    def clear_unavailable(self, key: str):
        if key in self.unavailable:
            self.unavailable.remove(key)
