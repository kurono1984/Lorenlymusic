import reflex as rx

from app.components.footer import footer
from app.components.media_image import safe_image
from app.components.navbar import navbar
from app.states.artist_state import CONTACT_EMAIL, WHATSAPP_URL
from app.states.silvana_state import (
    UTAU_OFFICIAL_ART,
    VOICEBANK_DOWNLOAD,
    VOICEBANK_DOWNLOAD_LABEL,
    Illustration,
    ListBlock,
    RuleItem,
    SpecItem,
    UtauState,
    UtauVideo,
)


def _spec_row(item: SpecItem, **props) -> rx.Component:
    return rx.el.div(
        rx.icon(
            item["icon"], class_name="mt-1 h-4 w-4 shrink-0 text-[#ff5a4e]"
        ),
        rx.el.div(
            rx.el.dt(
                item["label"],
                class_name="text-[10px] uppercase tracking-[0.26em] text-stone-500",
            ),
            rx.el.dd(
                item["value"],
                class_name=rx.cond(
                    item["label"] == "Nombre japonés",
                    "mt-1 text-sm leading-relaxed text-stone-200 font-['Noto_Sans_JP',_sans-serif]",
                    "mt-1 text-sm leading-relaxed text-stone-200",
                ),
            ),
            class_name="min-w-0",
        ),
        class_name="flex w-full gap-3 border-t border-white/10 py-4",
        **props,
    )


def utau_hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Voicebank UTAU · Español",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Silvana", class_name="block"),
                    rx.el.span(
                        "Aritani", class_name="block italic text-[#ff5a4e]"
                    ),
                    class_name="mt-5 font-serif text-5xl leading-[0.95] text-stone-50 sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    rx.el.span(
                        "シルバナ・アリタニ",
                        lang="ja",
                        class_name="font-['Noto_Sans_JP',_sans-serif]",
                    ),
                    " · Ángel-Quimera con voz y diseño de Lorenly. Banco de voz UTAU "
                    "para pop, rock y baladas en español.",
                    class_name="mt-7 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("download", class_name="h-4 w-4"),
                        VOICEBANK_DOWNLOAD_LABEL,
                        href=VOICEBANK_DOWNLOAD,
                        target="_blank",
                        rel="noopener noreferrer",
                        class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.22em] text-[#141110] hover:bg-[#ff7468] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white",
                    ),
                    rx.el.a(
                        rx.icon("video", class_name="h-4 w-4"),
                        "Ver videos",
                        href="#videos",
                        class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.22em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    class_name="mt-10 flex flex-wrap gap-4",
                ),
                class_name="lg:col-span-6 lg:pr-10",
            ),
            rx.el.div(
                rx.el.div(
                    safe_image(
                        "silvana-oficial",
                        UTAU_OFFICIAL_ART,
                        "Arte oficial de Silvana Aritani por Pimienta Kast",
                        "w-full aspect-[3/4] object-contain bg-[#1c1817]",
                        "aspect-[3/4]",
                    ),
                    rx.el.p(
                        "Silvana Aritani · diseño oficial",
                        class_name="absolute -bottom-4 left-6 bg-[#ff5a4e] px-4 py-2 text-[10px] uppercase tracking-[0.28em] text-[#141110]",
                    ),
                    class_name="relative border border-white/15 bg-[#1c1817]",
                ),
                rx.el.p(
                    "Arte oficial: Pimienta Kast · Voz y diseño: Lorenly.",
                    class_name="mt-10 border-l border-[#ff5a4e] pl-6 font-serif text-lg italic leading-snug text-stone-200",
                ),
                class_name="mt-14 lg:col-span-6 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-8 px-6 pb-20 pt-16 lg:grid-cols-12",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def utau_profile() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Perfil técnico",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "El banco de voz",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Datos del banco de voz y créditos originales del proyecto.",
                    class_name="mt-5 max-w-xl text-base leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-5 lg:pr-10",
            ),
            rx.el.dl(
                rx.foreach(
                    UtauState.identity,
                    lambda item: _spec_row(item, key=item["label"]),
                ),
                class_name="mt-10 border-b border-white/10 lg:col-span-7 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-8 px-6 py-24 lg:grid-cols-12",
        ),
        id="perfil",
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _sheet_card(item: SpecItem, **props) -> rx.Component:
    return rx.el.div(
        rx.icon(item["icon"], class_name="h-5 w-5 text-[#ff5a4e]"),
        rx.el.p(
            item["label"],
            class_name="mt-4 text-[10px] uppercase tracking-[0.26em] text-stone-500",
        ),
        rx.el.p(item["value"], class_name="mt-1 text-sm text-stone-200"),
        class_name="w-full border border-white/10 bg-[#1a1615] p-5 hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def utau_sheet() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Ficha del personaje",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Quién es Silvana",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    UtauState.character_sheet,
                    lambda item: _sheet_card(item, key=item["label"]),
                ),
                class_name="mt-12 grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-5",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        id="ficha",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _story_paragraph(text: str, **props) -> rx.Component:
    return rx.el.p(
        text,
        class_name="mt-5 text-base leading-relaxed text-stone-400 first:mt-0",
        **props,
    )


def utau_story() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Personalidad e historia",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "El Ángel-Quimera",
                    class_name="mt-3 font-serif text-4xl leading-tight text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    UtauState.personality,
                    class_name="mt-6 text-base leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-5 lg:pr-10",
            ),
            rx.el.div(
                rx.foreach(UtauState.story, _story_paragraph),
                class_name="mt-10 lg:col-span-7 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-8 px-6 py-24 lg:grid-cols-12",
        ),
        id="historia",
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _block_item(text: str, **props) -> rx.Component:
    return rx.el.li(
        rx.icon("dot", class_name="mt-0.5 h-4 w-4 shrink-0 text-[#ff5a4e]"),
        rx.el.span(text, class_name="text-sm leading-relaxed text-stone-300"),
        class_name="flex gap-2",
        **props,
    )


def _block(block: ListBlock, **props) -> rx.Component:
    return rx.el.article(
        rx.icon(block["icon"], class_name="h-6 w-6 text-[#ff5a4e]"),
        rx.el.h3(
            block["title"],
            class_name="mt-4 font-serif text-2xl text-stone-50",
        ),
        rx.el.ul(
            rx.foreach(block["items"], _block_item),
            class_name="mt-5 flex flex-col gap-3",
        ),
        class_name="flex flex-col border border-white/10 bg-[#1a1615] p-6 hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def utau_blocks() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Detalles",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Instrumentos, gustos, habilidades",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    UtauState.blocks,
                    lambda block: _block(block, key=block["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 md:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _rule(rule: RuleItem, **props) -> rx.Component:
    return rx.el.li(
        rx.cond(
            rule["allowed"],
            rx.icon(
                "circle-check",
                class_name="mt-0.5 h-5 w-5 shrink-0 text-[#ff5a4e]",
            ),
            rx.icon(
                "circle-x", class_name="mt-0.5 h-5 w-5 shrink-0 text-stone-500"
            ),
        ),
        rx.el.span(
            rule["text"],
            class_name="text-sm leading-relaxed text-stone-300",
        ),
        class_name="flex gap-3 border-t border-white/10 py-4",
        **props,
    )


def utau_rules() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Regla de diseño",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Sobre el diseño",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Silvana Aritani es un personaje original de Lorenly.",
                    class_name="mt-5 max-w-xl text-base leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-5 lg:pr-10",
            ),
            rx.el.ul(
                rx.foreach(
                    UtauState.design_rules,
                    lambda rule: _rule(rule, key=rule["key"]),
                ),
                class_name="mt-10 border-b border-white/10 lg:col-span-7 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-8 px-6 py-24 lg:grid-cols-12",
        ),
        id="reglas",
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _illustration(item: Illustration, **props) -> rx.Component:
    return rx.el.figure(
        safe_image(
            item["key"],
            item["src"],
            item["title"],
            "w-full aspect-[3/4] object-contain bg-[#1c1817] transition-all duration-500",
            "aspect-[3/4]",
        ),
        rx.el.figcaption(
            rx.el.p(
                item["title"],
                class_name="font-serif text-xl text-stone-50",
            ),
            rx.el.p(
                item["detail"],
                class_name="mt-2 text-sm leading-relaxed text-stone-400",
            ),
            class_name="mt-4",
        ),
        class_name="border border-white/10 bg-[#1a1615] p-4",
        **props,
    )


def utau_illustrations() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Ilustraciones",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Galería del personaje",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    UtauState.illustrations,
                    lambda item: _illustration(item, key=item["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        id="ilustraciones",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _video_card(video: UtauVideo, **props) -> rx.Component:
    return rx.el.article(
        rx.cond(
            UtauState.playing.contains(video["key"]),
            rx.el.div(
                rx.el.iframe(
                    src=video["embed"],
                    title=f"Video de {video['title']}",
                    loading="lazy",
                    allow="accelerometer; clipboard-write; encrypted-media; picture-in-picture",
                    allow_full_screen=True,
                    class_name="absolute inset-0 h-full w-full border-0",
                ),
                class_name="relative aspect-video w-full bg-black",
            ),
            rx.el.button(
                rx.el.img(
                    src=video["thumb"],
                    alt=f"Miniatura del video {video['title']}",
                    loading="lazy",
                    referrer_policy="no-referrer",
                    class_name="absolute inset-0 h-full w-full object-cover grayscale-[25%] group-hover:grayscale-0 transition-all duration-500",
                ),
                rx.el.span(
                    rx.icon("play", class_name="h-6 w-6 text-[#141110]"),
                    class_name="relative flex h-14 w-14 items-center justify-center rounded-full bg-[#ff5a4e] group-hover:bg-[#ff7468] transition-colors",
                ),
                on_click=lambda: UtauState.play(video["key"]),
                aria_label=f"Reproducir {video['title']}",
                class_name="group relative flex aspect-video w-full items-center justify-center overflow-hidden border-b border-white/10 bg-[#1c1817] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ff5a4e]",
            ),
        ),
        rx.el.div(
            rx.el.h3(
                video["title"],
                class_name="font-serif text-2xl leading-snug text-stone-50",
            ),
            rx.el.p(
                video["artist"],
                class_name="mt-2 text-xs uppercase tracking-[0.18em] text-stone-500",
            ),
            rx.el.div(
                rx.cond(
                    UtauState.playing.contains(video["key"]),
                    rx.el.button(
                        rx.icon("eye-off", class_name="h-4 w-4"),
                        "Ocultar reproductor",
                        on_click=lambda: UtauState.stop(video["key"]),
                        class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-400 hover:text-[#ff5a4e] transition-colors",
                    ),
                    rx.el.button(
                        rx.icon("play", class_name="h-4 w-4"),
                        "Reproducir aquí",
                        on_click=lambda: UtauState.play(video["key"]),
                        class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-300 hover:text-[#ff5a4e] transition-colors",
                    ),
                ),
                rx.el.a(
                    rx.icon("arrow-up-right", class_name="h-4 w-4"),
                    "Ver en YouTube",
                    href=video["external"],
                    target="_blank",
                    rel="noopener noreferrer",
                    aria_label=f"Ver {video['title']} en YouTube",
                    class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-400 hover:text-[#ff5a4e] transition-colors",
                ),
                class_name="mt-5 flex flex-wrap items-center gap-x-6 gap-y-3 border-t border-white/10 pt-4",
            ),
            class_name="p-5",
        ),
        class_name="flex flex-col border border-white/10 bg-[#1a1615] hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def utau_videos() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Videos",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Silvana en movimiento",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Canciones publicadas con Silvana Aritani. Los reproductores se cargan solo "
                    "cuando los pides.",
                    class_name="mt-5 max-w-xl text-base leading-relaxed text-stone-300",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    UtauState.videos,
                    lambda video: _video_card(video, key=video["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        id="videos",
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def utau_download() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Descarga",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Silvana Aritani · Voicebank UTAU",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "La descarga del banco de voz está alojada en Google Drive. Si el enlace no "
                    "responde, escribe por WhatsApp o correo.",
                    class_name="mt-5 max-w-lg text-base leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-7",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("download", class_name="h-4 w-4"),
                    VOICEBANK_DOWNLOAD_LABEL,
                    href=VOICEBANK_DOWNLOAD,
                    target="_blank",
                    rel="noopener noreferrer",
                    class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.2em] text-[#141110] hover:bg-[#ff7468] transition-colors",
                ),
                rx.el.a(
                    rx.icon("message-circle", class_name="h-4 w-4"),
                    "Pedir por WhatsApp",
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
        id="descarga",
        class_name="bg-[#141110]",
    )


def silvana_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            utau_hero(),
            utau_profile(),
            utau_sheet(),
            utau_story(),
            utau_blocks(),
            utau_rules(),
            utau_illustrations(),
            utau_videos(),
            utau_download(),
        ),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
