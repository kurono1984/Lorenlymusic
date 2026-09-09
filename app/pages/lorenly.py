import reflex as rx

from app.components.footer import footer
from app.components.media_image import safe_image
from app.components.navbar import navbar
from app.states.artist_state import (
    CONTACT_EMAIL,
    LORENLY_PORTRAIT,
    PHONE_PRIMARY,
    PHONE_PRIMARY_DISPLAY,
    WHATSAPP_URL,
    ProfileState,
    StagePhoto,
    TimelineItem,
    VoicebankItem,
)


def _fact(label: str, value: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            label,
            class_name="text-[10px] uppercase tracking-[0.26em] text-[#ff5a4e]",
        ),
        rx.el.p(value, class_name="mt-2 text-sm text-stone-300"),
        class_name="w-full border-l border-white/15 pl-4",
    )


def lorenly_hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Perfil · Productora VOCALOID",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Lorenly", class_name="block"),
                    rx.el.span(
                        "desde Lima, Perú",
                        class_name="block italic text-[#ff5a4e]",
                    ),
                    class_name="mt-6 font-serif text-5xl leading-[0.95] tracking-tight text-stone-50 sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    "Compone música desde los ocho años y trabaja con voces sintetizadas VOCALOID "
                    "desde abril de 2017. Compone, escribe, arregla y produce sus propias canciones "
                    "en español.",
                    class_name="mt-8 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                rx.el.div(
                    _fact("Composición", "Desde los 8 años"),
                    _fact("Origen", "Lima, Perú"),
                    _fact("VOCALOID", "Desde abril de 2017"),
                    _fact("Comunidad", "VocaloP Hispanos (2019)"),
                    class_name="mt-10 grid grid-cols-1 gap-6 sm:grid-cols-2",
                ),
                class_name="lg:col-span-7 lg:pr-12",
            ),
            rx.el.div(
                rx.el.div(
                    safe_image(
                        "lorenly-retrato",
                        LORENLY_PORTRAIT,
                        "Lorenly, productora musical VOCALOID",
                        "w-full aspect-[4/5] object-cover grayscale-[15%] contrast-105",
                    ),
                    rx.el.p(
                        "Lorenly · retrato",
                        class_name="absolute -bottom-4 left-6 bg-[#ff5a4e] px-4 py-2 text-[10px] uppercase tracking-[0.28em] text-[#141110]",
                    ),
                    class_name="relative border border-white/15",
                ),
                rx.el.p(
                    "Composición, letras, arreglos y producción de canciones en español.",
                    class_name="mt-10 border-l border-[#ff5a4e] pl-6 font-serif text-lg italic leading-snug text-stone-200",
                ),
                class_name="mt-14 lg:col-span-5 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-6 px-6 pb-20 pt-16 lg:grid-cols-12 lg:pt-24",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def biografia() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Biografía",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "De los 8 años a la producción VOCALOID",
                    class_name="mt-4 font-serif text-4xl leading-tight text-stone-50 sm:text-5xl",
                ),
                class_name="lg:col-span-5 lg:pr-10",
            ),
            rx.el.div(
                rx.el.p(
                    "Lorenly compone música desde los ocho años. Entre 2011 y 2012 formó parte de "
                    "Animatissimo, desde septiembre de 2012 integra el proyecto Luminus Hearts y "
                    "desde 2016 participa en UCG.",
                    class_name="text-base leading-relaxed text-stone-300",
                ),
                rx.el.p(
                    "En abril de 2017 comenzó a producir canciones con voces sintetizadas VOCALOID, "
                    "y en 2019 impulsó VocaloP Hispanos.",
                    class_name="mt-5 text-base leading-relaxed text-stone-400",
                ),
                rx.el.p(
                    "En 2020 recibió una mención honorífica en MIKU EXPO 2020 Europe. Además de su "
                    "catálogo propio, desarrolla el voicebank UTAU Silvana Aritani.",
                    class_name="mt-5 text-base leading-relaxed text-stone-400",
                ),
                class_name="mt-10 lg:col-span-7 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-8 px-6 py-24 lg:grid-cols-12",
        ),
        id="biografia",
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _timeline_item(item: TimelineItem, **props) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    class_name="mt-2 block h-2 w-2 shrink-0 rounded-full bg-[#ff5a4e]"
                ),
                rx.el.p(
                    item["year"],
                    class_name="text-xs uppercase tracking-[0.28em] text-[#ff5a4e]",
                ),
                class_name="flex items-start gap-3 sm:w-48 sm:shrink-0",
            ),
            rx.el.div(
                rx.el.h3(
                    item["title"],
                    class_name="font-serif text-2xl text-stone-50",
                ),
                rx.el.p(
                    item["detail"],
                    class_name="mt-2 max-w-2xl text-sm leading-relaxed text-stone-400",
                ),
                class_name="mt-3 min-w-0 sm:mt-0",
            ),
            class_name="flex flex-col sm:flex-row sm:gap-8",
        ),
        class_name="border-t border-white/10 py-8 first:border-t-0",
        **props,
    )


def trayectoria() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Trayectoria",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Línea de tiempo",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.ol(
                rx.foreach(
                    ProfileState.timeline,
                    lambda item: _timeline_item(item, key=item["year"]),
                ),
                class_name="mt-10",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        id="trayectoria",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _voicebank(item: VoicebankItem, **props) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.el.h3(
                item["name"],
                class_name="font-serif text-2xl text-stone-50",
            ),
            rx.el.span(
                item["engine"],
                class_name="w-fit border border-[#ff5a4e]/60 px-3 py-1 text-[10px] uppercase tracking-[0.22em] text-[#ff5a4e]",
            ),
            class_name="flex flex-wrap items-center justify-between gap-3",
        ),
        rx.el.p(
            item["detail"],
            class_name="mt-3 text-sm leading-relaxed text-stone-400",
        ),
        class_name="border border-white/10 bg-[#141110] p-6 hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def bancos_de_voz() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Herramientas",
                        class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                    ),
                    rx.el.h2(
                        "Bancos de voz utilizados",
                        class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                    ),
                    rx.el.p(
                        "Voces VOCALOID y UTAU que aparecen en sus canciones publicadas.",
                        class_name="mt-5 max-w-xl text-base leading-relaxed text-stone-300",
                    ),
                    class_name="lg:col-span-5 lg:pr-10",
                ),
                rx.el.ul(
                    rx.foreach(
                        ProfileState.voicebanks,
                        lambda item: _voicebank(item, key=item["name"]),
                    ),
                    class_name="mt-10 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:col-span-7 lg:mt-0",
                ),
                class_name="grid grid-cols-1 gap-8 lg:grid-cols-12",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _gallery_photo(item: StagePhoto, **props) -> rx.Component:
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


def imagenes() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Imágenes",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Portada y presentaciones",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    ProfileState.stage_photos,
                    lambda item: _gallery_photo(item, key=item["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def cierre() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Trabajemos juntos",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "¿Tienes un proyecto musical?",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Composición, letras, arreglos, video lyrics y manipulación VOCALOID o UTAU. "
                    "Revisa los servicios o escribe directamente.",
                    class_name="mt-5 max-w-lg text-base leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-7",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("list", class_name="h-4 w-4"),
                    "Ver servicios",
                    href="/servicios",
                    class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.2em] text-[#141110] hover:bg-[#ff7468] transition-colors",
                ),
                rx.el.a(
                    rx.icon("phone", class_name="h-4 w-4"),
                    PHONE_PRIMARY_DISPLAY,
                    href=f"tel:{PHONE_PRIMARY}",
                    class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.2em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                ),
                rx.el.a(
                    rx.icon("message-circle", class_name="h-4 w-4"),
                    "WhatsApp",
                    href=WHATSAPP_URL,
                    target="_blank",
                    rel="noopener noreferrer",
                    class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.2em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                ),
                rx.el.a(
                    rx.icon("mail", class_name="h-4 w-4"),
                    CONTACT_EMAIL,
                    href=f"mailto:{CONTACT_EMAIL}",
                    class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.2em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                ),
                class_name="mt-10 flex flex-wrap gap-4 lg:col-span-5 lg:mt-0 lg:flex-col",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-8 px-6 py-24 lg:grid-cols-12",
        ),
        class_name="bg-[#1a1615]",
    )


def lorenly_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            lorenly_hero(),
            biografia(),
            trayectoria(),
            bancos_de_voz(),
            imagenes(),
            cierre(),
        ),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
