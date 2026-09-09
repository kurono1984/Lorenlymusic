from typing import TypedDict

import reflex as rx

BANDCAMP_URL = "https://lorenly.bandcamp.com"

CATEGORY_INSTRUMENTAL = "Instrumental"
CATEGORY_CANTAUTORA = "Canciones como cantautora"
CATEGORY_VOCALOP = "Canciones como VocaloP"

CATEGORIES: list[str] = [
    CATEGORY_INSTRUMENTAL,
    CATEGORY_CANTAUTORA,
    CATEGORY_VOCALOP,
]

INSTRUMENTAL_TITLES: list[str] = [
    "Scifi – Theme",
    "Soundtrack – Terror del Mediodía",
    "Soundtrack – Inmensidad",
    "Marina",
    "Celeste",
    "Mi cascabel",
    "Ambar",
    "Sixmar",
    "Sixtinne",
    "Tenerum",
    "Mariposa Monarca",
    "Happy Chibi Erhu",
    "Nua Harp",
    "Noche Estrellada Tú",
    "Brisa Divina",
    "Calma y Tempestad",
    "Sorciére",
    "Oiseau Etoilé",
    "Tonerre Rose",
    "Otoño del Valle Sur",
    "Himno de las Plantas LV7",
]

CANTAUTORA_TITLES: list[str] = [
    "Clavelina",
    "Rita sueña",
    "Berenisse",
    "Sí",
    "Rosas Frescas en tu Puerta",
    "Lágrimas",
    "Ladrón de Amor",
    "Me transformáis",
    "Como un arcoiris",
    "Rosicler",
    "Magia",
    "Life / Mi vida sin tu amor",
    "Sueños sobre sueños",
    "Sujétate de mi",
    "Rojo Azul",
    "En una ratonera",
    "Suspirando Amor",
    "Magnolia",
    "Soy Nube",
    "Cerca de tu corazón",
    "Poema de Mentiras",
    "Creo en ti",
    "Agua Secreta, Tierra Lejana",
    "Prodigio de Amor",
    "Amarilis del Cielo",
    "En Flor",
    "Adiós dulce sueño",
    "Julia",
    "Jessique",
    "Entre tus manos",
    "Soledades",
    "Mi Vacío",
    "La Promesa",
    "Hoy",
    "No desesperes",
    "Tiranía",
    "El Camino",
    "Fue",
    "Perdóname",
    "Guardiana",
    "Dios se acordó de mi",
    "Buscaré",
    "A Volar",
    "Tantas mentiras",
    "Desolación",
    "Princesa",
    "Si tú lo quieres",
    "Lo siento",
    "Selene",
    "Que hemos hecho",
    "Canto de Amor",
    "Hojas Secas",
    "Si mis sueños pueden más",
    "¿Dónde estás?",
    "Una sencilla promesa",
    "Si fueras tú",
    "Tan sólo tú",
    "Todo mi amor",
    "Adiós, adiós, adiós",
    "Inagotable",
    "Fantasma de amor",
    "Alma",
]

VOCALOP_TITLES: list[str] = [
    "Rita sueña",
    "Clavelina",
    "Aywakuq",
    "Luna a Cuestas",
    "Magnolia",
    "Agua secreta, Tierra Lejana",
    "Cálida Esperanza",
    "Rosicler",
    "Verde",
    "Amarilis",
    "Life / Mi vida sin tu amor",
    "Noche Estrellada",
    "Soy Nube",
    "Te amaré",
    "Cactus Triste",
    "Amor",
    "Un, dos, tres",
    "Poema de Mentiras",
    "Aspid",
    "All my Love",
    "A las 2:30 pm",
    "Rosas Frescas en tu Puerta",
    "¡Adiós, señor extraño!",
    "Armonía",
    "Nautilus",
    "Nochebuena hoy",
    "Corazón de Fuego",
    "Berenisse",
    "Días Grises, días de color",
    "Sujétate de mi",
    "A ti",
    "Susurro de las Estrellas",
    "Tengo un dragón",
    "Sentimientos",
    "Harawikunaq wasin",
    "Teleférico",
    "Sí",
    "Greetings to Cecilia",
    "Himitsu no Mizu",
    "La Achirana",
    "Espíritus de la Lluvia",
    "Navidad Solitaria",
    "Natividad (Feat Subliminal Sound Engine)",
    "Más cerca que antes",
    "¡Adiós, dulce sueño!",
    "Luz",
    "Nino",
    "Dolor y Desesperanza",
    "Gloria",
    "Ausencia",
    "En Flor",
    "Jessique",
    "Angélica",
    "Lejos",
    "¡Ven, Reina!",
    "Fly Away (Fleur Du Vent)",
    "Por eso novio nunca tendré (MidoriOverwritte)",
    "Búscame (feat Ezequiel Casas)",
    "Te olvidaré (Feat Ezequiel Casas)",
    "Magia (Feat Ahzoren)",
    "Romance (feat Arve)",
    "Between Love (feat Arve)",
]


class CatalogTrack(TypedDict):
    key: str
    title: str
    category: str


def _build_catalog() -> list[CatalogTrack]:
    groups: list[tuple[str, str, list[str]]] = [
        ("inst", CATEGORY_INSTRUMENTAL, INSTRUMENTAL_TITLES),
        ("cant", CATEGORY_CANTAUTORA, CANTAUTORA_TITLES),
        ("voca", CATEGORY_VOCALOP, VOCALOP_TITLES),
    ]
    catalog: list[CatalogTrack] = []
    for prefix, category, titles in groups:
        for index, title in enumerate(titles, start=1):
            catalog.append(
                {
                    "key": f"{prefix}-{index}",
                    "title": title,
                    "category": category,
                }
            )
    return catalog


class CatalogState(rx.State):
    """Catálogo real de música, tal como está publicado en el sitio oficial."""

    query: str = ""
    category: str = "Todas"

    categories: list[str] = [
        "Todas",
        CATEGORY_INSTRUMENTAL,
        CATEGORY_CANTAUTORA,
        CATEGORY_VOCALOP,
    ]

    catalog: list[CatalogTrack] = _build_catalog()

    @rx.var
    def total_count(self) -> int:
        return len(self.catalog)

    @rx.var
    def counts_by_category(self) -> dict[str, int]:
        counts = {name: 0 for name in CATEGORIES}
        for track in self.catalog:
            counts[track["category"]] = counts.get(track["category"], 0) + 1
        counts["Todas"] = len(self.catalog)
        return counts

    @rx.var
    def filtered(self) -> list[CatalogTrack]:
        text = self.query.strip().lower()
        result: list[CatalogTrack] = []
        for track in self.catalog:
            if self.category != "Todas" and track["category"] != self.category:
                continue
            if text and text not in track["title"].lower():
                continue
            result.append(track)
        return result

    @rx.var
    def filtered_count(self) -> int:
        return len(self.filtered)

    @rx.var
    def has_results(self) -> bool:
        return len(self.filtered) > 0

    @rx.var
    def is_filtered(self) -> bool:
        return bool(self.query.strip()) or self.category != "Todas"

    @rx.event
    def set_query(self, value: str):
        self.query = value

    @rx.event
    def set_category(self, value: str):
        self.category = value

    @rx.event
    def clear_filters(self):
        self.query = ""
        self.category = "Todas"
