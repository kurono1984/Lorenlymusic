import reflex as rx

from app.pages.canciones import canciones_page
from app.pages.home import home_page
from app.pages.lorenly import lorenly_page
from app.pages.luminus_hearts import luminus_page
from app.pages.musica import musica_page
from app.pages.privacy import privacy_page
from app.pages.servicios import servicios_page
from app.pages.silvana_aritani import silvana_page
from app.pages.tienda import tienda_page


def index() -> rx.Component:
    return home_page()


def musica() -> rx.Component:
    return musica_page()


def canciones() -> rx.Component:
    return canciones_page()


def lorenly() -> rx.Component:
    return lorenly_page()


def servicios() -> rx.Component:
    return servicios_page()


def tienda() -> rx.Component:
    return tienda_page()


def silvana_aritani() -> rx.Component:
    return silvana_page()


def utau_silvana_aritani() -> rx.Component:
    return silvana_page()


def luminus_hearts() -> rx.Component:
    return luminus_page()


def privacy() -> rx.Component:
    return privacy_page()


app = rx.App(
    theme=rx.theme(appearance="light"),
    style={"fontFamily": "Inter, sans-serif"},
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Noto+Sans+JP:wght@400;500&family=Playfair+Display:ital,wght@0,500;0,700;1,500&display=swap",
            rel="stylesheet",
        ),
    ],
    stylesheets=["/lorenly.css"],
)
app.add_page(
    index, route="/", title="Lorenly Music · Productora musical VOCALOID"
)
app.add_page(
    musica,
    route="/musica",
    title="Música · Catálogo completo de Lorenly Music",
)
app.add_page(
    canciones,
    route="/canciones",
    title="Canciones en video · Lorenly Music",
)
app.add_page(
    lorenly,
    route="/lorenly",
    title="Lorenly · Productora musical VOCALOID en Lima, Perú",
)
app.add_page(
    servicios,
    route="/servicios",
    title="Servicios musicales · Lorenly Music",
)
app.add_page(
    tienda,
    route="/tienda",
    title="Tienda · Lorenly Music en Bandcamp",
)
app.add_page(
    utau_silvana_aritani,
    route="/utau-silvana-aritani",
    title="Silvana Aritani · Voicebank UTAU",
)
app.add_page(
    silvana_aritani,
    route="/silvana-aritani",
    title="Silvana Aritani · Voicebank UTAU",
)
app.add_page(
    luminus_hearts,
    route="/luminus-hearts",
    title="Luminus Hearts · Dúo de Lorenly Music",
)
app.add_page(
    privacy,
    route="/privacy-policy",
    title="Política de privacidad · Lorenly Music",
)
