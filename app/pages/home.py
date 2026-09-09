import reflex as rx

from app.components.footer import (
    BANDCAMP,
    EMAIL,
    KOFI,
    PHONE,
    PHONE_DISPLAY,
    WHATSAPP,
    contact_button,
    footer,
)
from app.components.media_image import safe_image
from app.components.navbar import navbar
from app.states.site_content_state import (
    PORTRAIT_MAIN,
    ContentState,
    FeaturedVideo,
    Milestone,
    Photo,
)


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Productora musical VOCALOID · Lima, Perú",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Lorenly", class_name="block"),
                    rx.el.span(
                        "Music",
                        class_name="block italic text-[#ff5a4e]",
                    ),
                    class_name="mt-6 font-serif text-6xl leading-[0.92] tracking-tight text-stone-50 sm:text-7xl lg:text-8xl",
                ),
                rx.el.p(
                    "Canciones originales en español compuestas, arregladas y producidas para voces "
                    "sintetizadas. Composición desde los 8 años y trabajo VOCALOID desde abril de 2017.",
                    class_name="mt-8 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("music", class_name="h-4 w-4"),
                        "Escuchar la música",
                        href="#musica",
                        class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.22em] text-[#141110] hover:bg-[#ff7468] transition-colors",
                    ),
                    rx.el.a(
                        rx.icon("mail", class_name="h-4 w-4"),
                        "Contactar",
                        href="#contacto",
                        class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.22em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    class_name="mt-10 flex flex-wrap gap-4",
                ),
                class_name="lg:col-span-6 lg:pr-10",
            ),
            rx.el.div(
                rx.el.div(
                    safe_image(
                        "retrato-hero",
                        PORTRAIT_MAIN,
                        "Retrato de Lorenly, productora musical VOCALOID",
                        "w-full aspect-[4/5] object-cover grayscale-[15%] contrast-105",
                    ),
                    rx.el.p(
                        "Lorenly · retrato oficial",
                        class_name="absolute -bottom-4 left-6 bg-[#ff5a4e] px-4 py-2 text-[10px] uppercase tracking-[0.28em] text-[#141110]",
                    ),
                    class_name="relative border border-white/15",
                ),
                rx.el.div(
                    rx.el.p(
                        "«La música en español también puede sonar sintética y seguir siendo nuestra.»",
                        class_name="font-serif text-lg italic leading-snug text-stone-200",
                    ),
                    class_name="mt-10 border-l border-[#ff5a4e] pl-6",
                ),
                class_name="mt-14 lg:col-span-6 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-6 px-6 pb-24 pt-16 lg:grid-cols-12 lg:pt-24",
        ),
        class_name="relative overflow-hidden border-b border-white/10 bg-[#141110]",
    )


def award() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.icon("award", class_name="h-10 w-10 text-[#ff5a4e]"),
                rx.el.p(
                    "Reconocimiento",
                    class_name="mt-6 text-[11px] uppercase tracking-[0.32em] text-stone-500",
                ),
                rx.el.h2(
                    "MIKU EXPO 2020 Europe",
                    class_name="mt-2 font-serif text-5xl text-stone-50",
                ),
                rx.el.p(
                    "mención honorífica",
                    class_name="mt-1 font-serif text-2xl italic text-[#ff5a4e]",
                ),
                class_name="lg:col-span-5 lg:border-r lg:border-white/10 lg:pr-10",
            ),
            rx.el.div(
                rx.el.p(
                    "Lorenly recibió una mención honorífica en MIKU EXPO 2020 Europe, el evento "
                    "internacional dedicado a Hatsune Miku.",
                    class_name="text-lg leading-relaxed text-stone-300",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("list-music", class_name="h-4 w-4"),
                        "Ver el catálogo de música",
                        href="/musica",
                        class_name="flex w-fit items-center gap-3 border border-[#ff5a4e] px-5 py-3 text-xs uppercase tracking-[0.2em] text-[#ff5a4e] hover:bg-[#ff5a4e] hover:text-[#141110] transition-colors",
                    ),
                    class_name="mt-8",
                ),
                class_name="mt-10 lg:col-span-7 lg:mt-0 lg:pl-4",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 px-6 py-20 lg:grid-cols-12 lg:gap-8",
        ),
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _milestone(item: Milestone, **props) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.el.span(
                class_name="mt-2 block h-2 w-2 shrink-0 rounded-full bg-[#ff5a4e]"
            ),
            rx.el.div(
                rx.el.p(
                    item["year"],
                    class_name="text-xs uppercase tracking-[0.3em] text-[#ff5a4e]",
                ),
                rx.el.h3(
                    item["title"],
                    class_name="mt-2 font-serif text-2xl text-stone-50",
                ),
                rx.el.p(
                    item["detail"],
                    class_name="mt-2 max-w-2xl text-sm leading-relaxed text-stone-400",
                ),
            ),
            class_name="flex gap-5",
        ),
        class_name="border-t border-white/10 py-8 first:border-t-0",
        **props,
    )


def biography() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Biografía",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Compositora, cantautora y VocaloP",
                    class_name="mt-4 font-serif text-4xl leading-tight text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Lorenly compone música desde los ocho años. Integró Animatissimo entre 2011 y "
                    "2012, forma parte de Luminus Hearts desde 2012 y participa en UCG desde 2016.",
                    class_name="mt-6 text-base leading-relaxed text-stone-300",
                ),
                rx.el.p(
                    "Trabaja con voces sintetizadas VOCALOID desde abril de 2017, impulsó VocaloP "
                    "Hispanos en 2019 y desarrolla el voicebank UTAU Silvana Aritani.",
                    class_name="mt-4 text-base leading-relaxed text-stone-400",
                ),
                class_name="lg:sticky lg:top-28 lg:col-span-5",
            ),
            rx.el.ol(
                rx.foreach(
                    ContentState.milestones,
                    lambda item: _milestone(item, key=item["year"]),
                ),
                class_name="mt-12 lg:col-span-7 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-10 px-6 py-24 lg:grid-cols-12",
        ),
        id="biografia",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _photo(item: Photo, **props) -> rx.Component:
    return rx.el.figure(
        safe_image(
            item["key"],
            item["src"],
            item["caption"],
            "w-full aspect-[4/5] object-cover grayscale-[20%] hover:grayscale-0 transition-all duration-500",
        ),
        rx.el.figcaption(
            rx.el.p(
                item["place"],
                class_name="text-[10px] uppercase tracking-[0.28em] text-[#ff5a4e]",
            ),
            rx.el.p(item["caption"], class_name="mt-2 text-sm text-stone-300"),
            class_name="mt-4",
        ),
        class_name="border border-white/10 bg-[#1a1615] p-4",
        **props,
    )


def gallery() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Trayectoria en imágenes",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Retratos y presentaciones",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    ContentState.photos,
                    lambda item: _photo(item, key=item["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _featured_video(item: FeaturedVideo, **props) -> rx.Component:
    return rx.el.a(
        rx.el.img(
            src=item["thumb"],
            alt=f"Miniatura del video {item['title']}",
            loading="lazy",
            referrer_policy="no-referrer",
            class_name="aspect-video w-full object-cover grayscale-[20%] group-hover:grayscale-0 transition-all duration-500",
        ),
        rx.el.div(
            rx.el.h3(
                item["title"],
                class_name="font-serif text-2xl leading-snug text-stone-50",
            ),
            rx.el.p(
                item["artist"],
                class_name="mt-1 text-xs uppercase tracking-[0.18em] text-stone-500",
            ),
            rx.el.span(
                rx.icon("arrow-up-right", class_name="h-4 w-4"),
                "Ver en YouTube",
                class_name="mt-4 flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-[#ff5a4e]",
            ),
            class_name="p-5",
        ),
        href=item["url"],
        target="_blank",
        rel="noopener noreferrer",
        class_name="group flex flex-col border border-white/10 bg-[#1a1615] hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def music() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Videos",
                        class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                    ),
                    rx.el.h2(
                        "Tres canciones publicadas",
                        class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                    ),
                ),
                rx.el.a(
                    rx.icon("video", class_name="h-4 w-4"),
                    "Ver la videoteca completa",
                    href="/canciones",
                    class_name="flex h-fit w-fit items-center gap-2 border border-white/20 px-5 py-3 text-xs uppercase tracking-[0.2em] text-stone-200 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                ),
                class_name="flex flex-wrap items-end justify-between gap-6",
            ),
            rx.el.div(
                rx.foreach(
                    ContentState.featured_videos,
                    lambda item: _featured_video(item, key=item["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 md:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        id="musica",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def contact() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Contacto",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Hablemos de tu canción",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Composición, letra en español, arreglos, manipulación VOCALOID/UTAU y mezcla. "
                    "Escribe por el canal que prefieras y cuéntame tu proyecto.",
                    class_name="mt-6 max-w-lg text-base leading-relaxed text-stone-300",
                ),
                rx.el.a(
                    rx.icon("coffee", class_name="h-4 w-4"),
                    "Apoyar en Ko-fi",
                    href=KOFI,
                    target="_blank",
                    rel="noopener noreferrer",
                    class_name="mt-8 flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.2em] text-[#141110] hover:bg-[#ff7468] transition-colors",
                ),
                class_name="lg:col-span-6",
            ),
            rx.el.div(
                contact_button(
                    "phone", "Teléfono", PHONE_DISPLAY, f"tel:{PHONE}"
                ),
                contact_button(
                    "message-circle", "WhatsApp", "Abrir conversación", WHATSAPP
                ),
                contact_button(
                    "mail", "Correo electrónico", EMAIL, f"mailto:{EMAIL}"
                ),
                contact_button(
                    "shopping-bag",
                    "Bandcamp",
                    "lorenly.bandcamp.com",
                    BANDCAMP,
                ),
                class_name="mt-10 flex flex-col gap-4 lg:col-span-6 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-10 px-6 py-24 lg:grid-cols-12",
        ),
        id="contacto",
        class_name="bg-[#1a1615]",
    )


def home_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero(),
            award(),
            biography(),
            gallery(),
            music(),
            contact(),
        ),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
