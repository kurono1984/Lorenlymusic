from typing import TypedDict

import reflex as rx


class Member(TypedDict):
    key: str
    name: str
    role: str
    instruments: list[str]


class MissionPoint(TypedDict):
    key: str
    icon: str
    title: str
    detail: str


class LuminusState(rx.State):
    """Datos verificados del dúo Luminus Hearts."""

    founded: str = "Septiembre de 2012"

    story: list[str] = [
        "Luminus Hearts fue fundado en septiembre de 2012.",
        "Su música recorre el pop, el pop-rock, la balada rock, el indie-pop, el "
        "world music, lo experimental, el folk pop, la música de cámara, el new "
        "age y lo neo-orquestal.",
    ]

    members: list[Member] = [
        {
            "key": "silvana-navarro",
            "name": "Silvana Navarro",
            "role": "Compositora y soprano",
            "instruments": ["Flauta", "Teclado", "Melódica"],
        },
        {
            "key": "renzo-pacheco",
            "name": "Renzo Pacheco",
            "role": "Compositor",
            "instruments": ["Flauta", "Violín", "Oboe"],
        },
        {
            "key": "josseline-garcia",
            "name": "Josseline García",
            "role": "Mezzosoprano",
            "instruments": [],
        },
    ]

    genres: list[str] = [
        "Pop",
        "Pop-rock",
        "Balada rock",
        "Indie-pop",
        "World music",
        "Experimental",
        "Folk pop",
        "Música de cámara",
        "New age",
        "Neo-orquestal",
    ]

    mission: list[MissionPoint] = [
        {
            "key": "mision-integrar",
            "icon": "sparkles",
            "title": "Integrar espiritualidad y música",
            "detail": "Unir la espiritualidad humana y la música en una misma práctica.",
        },
        {
            "key": "mision-afectar",
            "icon": "sun",
            "title": "Afectar positivamente",
            "detail": "Buscar que la música afecte de forma positiva a quien la escucha.",
        },
        {
            "key": "mision-comunidad",
            "icon": "users",
            "title": "Construir comunidad",
            "detail": "Formar una comunidad abierta, flexible y armoniosa.",
        },
    ]
