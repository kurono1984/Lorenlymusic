from typing import TypedDict

import reflex as rx

PORTRAIT_MAIN = (
    "https://lorenlymusic.com/wp-content/uploads/2022/07/DSC_00362.jpg"
)
PERFORMANCE_ONE = (
    "https://lorenlymusic.com/wp-content/uploads/2020/07/"
    "92508002_2608078536128427_4057306002230345728_n.jpg"
)
PERFORMANCE_TWO = (
    "https://lorenlymusic.com/wp-content/uploads/2020/07/"
    "1040900_373110886144863_1679968572_o.jpg"
)


class NavLink(TypedDict):
    label: str
    href: str


class Milestone(TypedDict):
    year: str
    title: str
    detail: str


class Photo(TypedDict):
    key: str
    caption: str
    place: str
    src: str


class FeaturedVideo(TypedDict):
    key: str
    title: str
    artist: str
    url: str
    thumb: str


class ContentState(rx.State):
    """Contenido editorial verificado del sitio de Lorenly Music."""

    nav_links: list[NavLink] = [
        {"label": "Portada", "href": "/"},
        {"label": "Música", "href": "/musica"},
        {"label": "Canciones", "href": "/canciones"},
        {"label": "Lorenly", "href": "/lorenly"},
        {"label": "Servicios", "href": "/servicios"},
        {"label": "Tienda", "href": "/tienda"},
        {"label": "Silvana Aritani", "href": "/utau-silvana-aritani"},
        {"label": "Luminus Hearts", "href": "/luminus-hearts"},
    ]

    milestones: list[Milestone] = [
        {
            "year": "Desde los 8 años",
            "title": "Empieza a componer",
            "detail": "Lorenly compone música desde los ocho años de edad.",
        },
        {
            "year": "2011 – 2012",
            "title": "Animatissimo",
            "detail": "Forma parte de Animatissimo entre 2011 y 2012.",
        },
        {
            "year": "Desde 2012",
            "title": "Luminus Hearts",
            "detail": "Integra el proyecto Luminus Hearts, fundado en septiembre de 2012.",
        },
        {
            "year": "Desde 2016",
            "title": "UCG",
            "detail": "Participa en UCG desde 2016.",
        },
        {
            "year": "Abril de 2017",
            "title": "Comienza como productora VOCALOID",
            "detail": "Inicia su trabajo con voces sintetizadas VOCALOID en abril de 2017.",
        },
        {
            "year": "2019",
            "title": "VocaloP Hispanos",
            "detail": "Impulsa VocaloP Hispanos en 2019.",
        },
        {
            "year": "2020",
            "title": "MIKU EXPO 2020 Europe",
            "detail": "Recibe una mención honorífica en MIKU EXPO 2020 Europe.",
        },
    ]

    photos: list[Photo] = [
        {
            "key": "foto-retrato",
            "caption": "Retrato de Lorenly",
            "place": "Lorenly Music",
            "src": PORTRAIT_MAIN,
        },
        {
            "key": "foto-directo-1",
            "caption": "Lorenly en una presentación en vivo",
            "place": "En directo",
            "src": PERFORMANCE_ONE,
        },
        {
            "key": "foto-directo-2",
            "caption": "Lorenly durante una actuación",
            "place": "En directo",
            "src": PERFORMANCE_TWO,
        },
    ]

    featured_videos: list[FeaturedVideo] = [
        {
            "key": "TRwN0MwPUJE",
            "title": "Luna a cuestas (feat Hatsune Miku)",
            "artist": "Lorenly",
            "url": "https://www.youtube.com/watch?v=TRwN0MwPUJE",
            "thumb": "https://i.ytimg.com/vi/TRwN0MwPUJE/hqdefault.jpg",
        },
        {
            "key": "_WZ5Pw0EYjI",
            "title": "Cálida Esperanza (feat Megpoid)",
            "artist": "Lorenly",
            "url": "https://www.youtube.com/watch?v=_WZ5Pw0EYjI",
            "thumb": "https://i.ytimg.com/vi/_WZ5Pw0EYjI/hqdefault.jpg",
        },
        {
            "key": "RLM3ylQlC48",
            "title": "La Achirana",
            "artist": "Lorenly",
            "url": "https://www.youtube.com/watch?v=RLM3ylQlC48",
            "thumb": "https://i.ytimg.com/vi/RLM3ylQlC48/hqdefault.jpg",
        },
    ]
