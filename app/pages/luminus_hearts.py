import reflex as rx

from app.components.footer import KOFI, footer
from app.components.navbar import navbar
from app.states.artist_state import (
    CONTACT_EMAIL,
    PHONE_PRIMARY,
    PHONE_PRIMARY_DISPLAY,
    WHATSAPP_URL,
)
from app.states.duo_state import LuminusState, Member, MissionPoint


def luminus_hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Proyecto musical · Fundado en septiembre de 2012",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Luminus", class_name="block"),
                    rx.el.span(
                        "Hearts", class_name="block italic text-[#ff5a4e]"
                    ),
                    class_name="mt-5 font-serif text-5xl leading-[0.95] text-stone-50 sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    "Proyecto musical fundado en septiembre de 2012, con Silvana Navarro, "
                    "Renzo Pacheco y Josseline García.",
                    class_name="mt-7 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("users", class_name="h-4 w-4"),
                        "Integrantes",
                        href="#integrantes",
                        class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.22em] text-[#141110] hover:bg-[#ff7468] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white",
                    ),
                    rx.el.a(
                        rx.icon("sparkles", class_name="h-4 w-4"),
                        "Misión",
                        href="#mision",
                        class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.22em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    class_name="mt-10 flex flex-wrap gap-4",
                ),
                class_name="lg:col-span-7 lg:pr-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Fundación",
                        class_name="text-[10px] uppercase tracking-[0.28em] text-[#ff5a4e]",
                    ),
                    rx.el.p(
                        LuminusState.founded,
                        class_name="mt-3 font-serif text-4xl leading-tight text-stone-50",
                    ),
                    rx.el.div(
                        class_name="mt-8 h-24 w-full border-y border-white/15 bg-[repeating-linear-gradient(to_bottom,transparent_0px,transparent_11px,rgba(255,255,255,0.18)_11px,rgba(255,255,255,0.18)_12px)]",
                    ),
                    class_name="border border-white/15 bg-[#1a1615] p-8",
                ),
                rx.el.p(
                    "Pop, pop-rock, balada rock, indie-pop, world music, folk pop, música de "
                    "cámara, new age y neo-orquestal.",
                    class_name="mt-10 border-l border-[#ff5a4e] pl-6 font-serif text-lg italic leading-snug text-stone-200",
                ),
                class_name="mt-14 lg:col-span-5 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-8 px-6 pb-20 pt-16 lg:grid-cols-12",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _story_paragraph(text: str, **props) -> rx.Component:
    return rx.el.p(
        text,
        class_name="mt-5 text-base leading-relaxed text-stone-400 first:mt-0",
        **props,
    )


def luminus_story() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Historia del proyecto",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "El proyecto",
                    class_name="mt-3 font-serif text-4xl leading-tight text-stone-50 sm:text-5xl",
                ),
                class_name="lg:col-span-5 lg:pr-10",
            ),
            rx.el.div(
                rx.foreach(LuminusState.story, _story_paragraph),
                class_name="mt-10 lg:col-span-7 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-8 px-6 py-24 lg:grid-cols-12",
        ),
        id="historia",
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def _instrument(text: str, **props) -> rx.Component:
    return rx.el.li(
        rx.icon("music-2", class_name="mt-0.5 h-4 w-4 shrink-0 text-[#ff5a4e]"),
        rx.el.span(text, class_name="text-sm leading-relaxed text-stone-300"),
        class_name="flex gap-2",
        **props,
    )


def _member(member: Member, **props) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.h3(
                member["name"],
                class_name="font-serif text-3xl text-stone-50",
            ),
            rx.el.p(
                member["role"],
                class_name="mt-1 text-xs uppercase tracking-[0.18em] text-[#ff5a4e]",
            ),
            rx.cond(
                member["instruments"].length() > 0,
                rx.el.div(
                    rx.el.p(
                        "Instrumentos",
                        class_name="mt-6 text-[10px] uppercase tracking-[0.26em] text-stone-500",
                    ),
                    rx.el.ul(
                        rx.foreach(member["instruments"], _instrument),
                        class_name="mt-3 flex flex-col gap-2",
                    ),
                ),
                rx.fragment(),
            ),
            class_name="p-6",
        ),
        class_name="flex flex-col border border-white/10 bg-[#1a1615] hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def luminus_members() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Integrantes",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Tres integrantes",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    LuminusState.members,
                    lambda member: _member(member, key=member["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 md:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        id="integrantes",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _genre(genre: str, **props) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            genre,
            class_name="font-serif text-xl text-stone-50",
        ),
        class_name="w-full border-l border-[#ff5a4e]/60 pl-5",
        **props,
    )


def _mission(point: MissionPoint, **props) -> rx.Component:
    return rx.el.article(
        rx.icon(point["icon"], class_name="h-6 w-6 text-[#ff5a4e]"),
        rx.el.h3(
            point["title"],
            class_name="mt-4 font-serif text-2xl text-stone-50",
        ),
        rx.el.p(
            point["detail"],
            class_name="mt-2 text-sm leading-relaxed text-stone-400",
        ),
        class_name="border border-white/10 bg-[#141110] p-6 hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def luminus_identity() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Géneros",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Cómo suena Luminus",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.div(
                    rx.foreach(
                        LuminusState.genres,
                        lambda genre: _genre(genre, key=genre),
                    ),
                    class_name="mt-10 grid grid-cols-1 gap-5 sm:grid-cols-2",
                ),
                class_name="lg:col-span-5 lg:pr-10",
            ),
            rx.el.div(
                rx.el.p(
                    "Misión",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Para qué hacen música",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.div(
                    rx.foreach(
                        LuminusState.mission,
                        lambda point: _mission(point, key=point["key"]),
                    ),
                    class_name="mt-10 grid grid-cols-1 gap-4 sm:grid-cols-2",
                ),
                class_name="mt-16 lg:col-span-7 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-10 px-6 py-24 lg:grid-cols-12",
        ),
        id="mision",
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def luminus_cta() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Contacto",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Colabora con Luminus Hearts",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Si quieres proponer una colaboración, escribe por el canal que prefieras. "
                    "También puedes apoyar el proyecto en Ko-fi.",
                    class_name="mt-5 max-w-lg text-base leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-7",
            ),
            rx.el.div(
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
                rx.el.a(
                    rx.icon("coffee", class_name="h-4 w-4"),
                    "Ko-fi",
                    href=KOFI,
                    target="_blank",
                    rel="noopener noreferrer",
                    class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.2em] text-[#141110] hover:bg-[#ff7468] transition-colors",
                ),
                class_name="mt-10 flex flex-wrap gap-4 lg:col-span-5 lg:mt-0 lg:flex-col",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-8 px-6 py-24 lg:grid-cols-12",
        ),
        id="contacto",
        class_name="bg-[#1a1615]",
    )


def luminus_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            luminus_hero(),
            luminus_story(),
            luminus_members(),
            luminus_identity(),
            luminus_cta(),
        ),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
