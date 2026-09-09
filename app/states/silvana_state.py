from typing import TypedDict

import reflex as rx

from app.states.videoteca_state import build_video

VOICEBANK_DOWNLOAD = (
    "https://drive.google.com/file/d/10dqMeY9Ynovjk5yKabaJVNhnqnjor-HR/edit"
)
VOICEBANK_DOWNLOAD_LABEL = "Descargar Silvana Aritani"

UTAU_OFFICIAL_ART = (
    "https://lorenlymusic.com/wp-content/uploads/2020/06/utauSilvana-copia.png"
)
UTAU_COMMUNITY_ART = (
    "https://img.webme.com/pic/s/silvananavarrorivera/"
    "comision_silvanaa_by_sofia_design2001-dcjjg91.png"
)
UTAU_COLLAB_ART = (
    "https://lorenlymusic.com/wp-content/uploads/2020/07/"
    "Collab-Gakupo-Aritani-724x1024.jpg"
)


class SpecItem(TypedDict):
    label: str
    value: str
    icon: str


class ListBlock(TypedDict):
    key: str
    icon: str
    title: str
    items: list[str]


class RuleItem(TypedDict):
    key: str
    allowed: bool
    text: str


class Illustration(TypedDict):
    key: str
    title: str
    detail: str
    src: str


class UtauVideo(TypedDict):
    key: str
    title: str
    artist: str
    embed: str
    external: str
    thumb: str


class UtauState(rx.State):
    """Ficha del voicebank UTAU Silvana Aritani, con los datos originales."""

    playing: list[str] = []

    identity: list[SpecItem] = [
        {"label": "Nombre", "value": "Silvana Aritani", "icon": "user-round"},
        {
            "label": "Nombre japonés",
            "value": "シルバナ・アリタニ",
            "icon": "languages",
        },
        {"label": "Motor", "value": "UTAU", "icon": "audio-waveform"},
        {
            "label": "Géneros",
            "value": "Pop, rock y baladas en español",
            "icon": "music",
        },
        {
            "label": "Configuración inicial",
            "value": "Hana Misaki",
            "icon": "sliders-horizontal",
        },
        {
            "label": "Configuración posterior",
            "value": "DJ Kurono",
            "icon": "settings-2",
        },
        {
            "label": "Arte oficial",
            "value": "Pimienta Kast",
            "icon": "palette",
        },
        {
            "label": "Voz y diseño",
            "value": "Lorenly",
            "icon": "badge-check",
        },
    ]

    character_sheet: list[SpecItem] = [
        {"label": "Género", "value": "Femenino", "icon": "venus"},
        {"label": "Especie", "value": "Ángel-Quimera", "icon": "sparkles"},
        {"label": "Edad", "value": "25 años", "icon": "hourglass"},
        {"label": "Cumpleaños", "value": "7 de septiembre", "icon": "cake"},
        {"label": "Signo", "value": "Virgo", "icon": "star"},
        {"label": "Peso", "value": "52 kg", "icon": "weight"},
        {"label": "Altura", "value": "1.57 m", "icon": "ruler"},
        {"label": "Animal", "value": "Búho", "icon": "bird"},
    ]

    personality: str = "Introvertida, hipersensible y soñadora."

    story: list[str] = [
        "Silvana Aritani es un Ángel-Quimera: ama los bosques, las plantas, los "
        "animales pequeños y los atardeceres.",
        "Puede transformarse en búho y predecir el futuro; en esa forma conserva "
        "sus alas color perla.",
    ]

    blocks: list[ListBlock] = [
        {
            "key": "instrumentos",
            "icon": "guitar",
            "title": "Instrumentos",
            "items": ["Guitarra", "Violín"],
        },
        {
            "key": "gustos",
            "icon": "heart",
            "title": "Gustos",
            "items": [
                "Los bosques",
                "Las plantas",
                "Los animales pequeños",
                "Los atardeceres",
                "Color: blanco",
                "Comida: castañas y frutos del bosque",
                "Flor: lirio",
            ],
        },
        {
            "key": "habilidades",
            "icon": "wand-sparkles",
            "title": "Habilidades y aficiones",
            "items": [
                "Transformarse en búho",
                "Predecir el futuro",
                "Conservar sus alas color perla",
                "Tarot",
                "Comunicación animal",
            ],
        },
    ]

    design_rules: list[RuleItem] = [
        {
            "key": "regla-diseno",
            "allowed": False,
            "text": "El diseño del personaje no se modifica, salvo el vestuario y las alas.",
        },
    ]

    illustrations: list[Illustration] = [
        {
            "key": "ilus-oficial",
            "title": "Diseño oficial",
            "detail": "Arte oficial de Silvana Aritani por Pimienta Kast.",
            "src": UTAU_OFFICIAL_ART,
        },
        {
            "key": "ilus-comunidad",
            "title": "Arte de la comunidad",
            "detail": "Comisión de Silvana Aritani realizada por Sofía Design.",
            "src": UTAU_COMMUNITY_ART,
        },
        {
            "key": "ilus-collab",
            "title": "Colaboración",
            "detail": "Ilustración de colaboración entre Gakupo y Silvana Aritani.",
            "src": UTAU_COLLAB_ART,
        },
    ]

    videos: list[UtauVideo] = [
        build_video(
            "iDDkUrZzKiI",
            "Rosas Frescas en tu Puerta (feat Silvana Aritani)",
            "Lorenly",
        ),
        build_video("RLM3ylQlC48", "La Achirana", "Lorenly"),
        build_video(
            "opDPlHLPc9E",
            "Más cerca que antes (feat Silvana Aritani)",
            "Lorenly",
        ),
        build_video(
            "ZH0__V_aK4g",
            "Sí (feat Silvana Aritani & Hajime Ichida)",
            "Lorenly",
        ),
    ]

    @rx.event
    def play(self, key: str):
        if key not in self.playing:
            self.playing.append(key)

    @rx.event
    def stop(self, key: str):
        if key in self.playing:
            self.playing.remove(key)
