import reflex as rx

from app.components.footer import contact_button, footer
from app.components.media_image import safe_image
from app.components.navbar import navbar
from app.states.artist_state import (
    CONTACT_EMAIL,
    PHONE_PRIMARY,
    PHONE_PRIMARY_DISPLAY,
    WHATSAPP_URL,
    ProfileState,
    ServiceItem,
    StagePhoto,
)
from app.states.site_content_state import PERFORMANCE_ONE


def servicios_hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Servicios musicales",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Nueve formas", class_name="block"),
                    rx.el.span(
                        "de hacer tu canción",
                        class_name="block italic text-[#ff5a4e]",
                    ),
                    class_name="mt-6 font-serif text-5xl leading-[0.95] tracking-tight text-stone-50 sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    "Composición, letras, arreglos, música infantil, video lyrics, demos y "
                    "manipulación de voces VOCALOID. Cada trabajo se acuerda antes de empezar: "
                    "estilo, duración, entregas y formato de los archivos finales.",
                    class_name="mt-8 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("message-circle", class_name="h-4 w-4"),
                        "Escribir por WhatsApp",
                        href=WHATSAPP_URL,
                        target="_blank",
                        rel="noopener noreferrer",
                        class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.22em] text-[#141110] hover:bg-[#ff7468] transition-colors",
                    ),
                    rx.el.a(
                        rx.icon("mail", class_name="h-4 w-4"),
                        "Pedir presupuesto",
                        href=f"mailto:{CONTACT_EMAIL}",
                        class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.22em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    class_name="mt-10 flex flex-wrap gap-4",
                ),
                class_name="lg:col-span-7 lg:pr-12",
            ),
            rx.el.div(
                rx.el.div(
                    safe_image(
                        "servicios-directo",
                        PERFORMANCE_ONE,
                        "Lorenly durante una actuación en directo",
                        "w-full aspect-[4/5] object-cover grayscale-[15%] contrast-105",
                    ),
                    rx.el.p(
                        "Actuación en vivo",
                        class_name="absolute -bottom-4 left-6 bg-[#ff5a4e] px-4 py-2 text-[10px] uppercase tracking-[0.28em] text-[#141110]",
                    ),
                    class_name="relative border border-white/15",
                ),
                class_name="mt-14 lg:col-span-5 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-center gap-6 px-6 pb-20 pt-16 lg:grid-cols-12 lg:pt-24",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _include(text: rx.Var, **props) -> rx.Component:
    return rx.el.li(
        rx.icon("check", class_name="mt-0.5 h-4 w-4 shrink-0 text-[#ff5a4e]"),
        rx.el.span(text, class_name="text-sm text-stone-400"),
        class_name="flex items-start gap-2",
        **props,
    )


def _service_card(item: ServiceItem, **props) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.p(
                item["number"],
                class_name="font-serif text-4xl text-stone-700",
            ),
            rx.icon("audio-lines", class_name="h-6 w-6 text-[#ff5a4e]"),
            class_name="flex items-center justify-between gap-4",
        ),
        rx.el.h3(
            item["title"],
            class_name="mt-6 font-serif text-2xl leading-snug text-stone-50",
        ),
        rx.el.p(
            item["summary"],
            class_name="mt-2 text-xs uppercase tracking-[0.14em] text-stone-500",
        ),
        rx.el.p(
            item["detail"],
            class_name="mt-4 text-sm leading-relaxed text-stone-400",
        ),
        rx.el.ul(
            rx.foreach(item["includes"], lambda text: _include(text)),
            class_name="mt-5 flex flex-col gap-2 border-t border-white/10 pt-5",
        ),
        rx.el.a(
            rx.icon("message-circle", class_name="h-4 w-4"),
            "Consultar este servicio",
            href=WHATSAPP_URL,
            target="_blank",
            rel="noopener noreferrer",
            class_name="mt-6 flex w-fit items-center gap-2 border border-white/20 px-4 py-2 text-[11px] uppercase tracking-[0.18em] text-stone-200 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ff5a4e]",
        ),
        class_name="flex h-full flex-col border border-white/10 bg-[#1a1615] p-6 sm:p-8 hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def servicios_grid() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Catálogo de servicios",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Qué se puede producir",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    ProfileState.services,
                    lambda item: _service_card(item, key=item["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        id="servicios",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _stage_photo(item: StagePhoto, **props) -> rx.Component:
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
        class_name="border border-white/10 bg-[#141110] p-4",
        **props,
    )


def actuaciones() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "En directo",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Portada y actuaciones",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    ProfileState.stage_photos,
                    lambda item: _stage_photo(item, key=item["key"]),
                ),
                class_name="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-24",
        ),
        class_name="border-b border-white/10 bg-[#1a1615]",
    )


def contacto_servicios() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Contacto directo",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Cuéntame tu proyecto",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Escribe indicando el tipo de servicio, la fecha en la que lo necesitas y las "
                    "referencias musicales que tengas. Te responderé con la propuesta de trabajo.",
                    class_name="mt-6 max-w-lg text-base leading-relaxed text-stone-300",
                ),
                rx.el.a(
                    rx.icon("user", class_name="h-4 w-4"),
                    "Conocer a Lorenly",
                    href="/lorenly",
                    class_name="mt-8 flex w-fit items-center gap-3 border border-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.2em] text-[#ff5a4e] hover:bg-[#ff5a4e] hover:text-[#141110] transition-colors",
                ),
                class_name="lg:col-span-6",
            ),
            rx.el.div(
                contact_button(
                    "phone",
                    "Teléfono",
                    PHONE_PRIMARY_DISPLAY,
                    f"tel:{PHONE_PRIMARY}",
                ),
                contact_button(
                    "message-circle",
                    "WhatsApp",
                    "+51 965 048 629",
                    WHATSAPP_URL,
                ),
                contact_button(
                    "mail",
                    "Correo electrónico",
                    CONTACT_EMAIL,
                    f"mailto:{CONTACT_EMAIL}",
                ),
                class_name="mt-10 flex flex-col gap-4 lg:col-span-6 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 gap-10 px-6 py-24 lg:grid-cols-12",
        ),
        id="contacto",
        class_name="bg-[#141110]",
    )


def servicios_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            servicios_hero(),
            servicios_grid(),
            actuaciones(),
            contacto_servicios(),
        ),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
