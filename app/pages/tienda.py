import reflex as rx

from app.components.footer import KOFI, footer
from app.components.navbar import navbar
from app.states.artist_state import (
    CONTACT_EMAIL,
    PHONE_PRIMARY,
    PHONE_PRIMARY_DISPLAY,
    WHATSAPP_URL,
)
from app.states.bandcamp_state import BANDCAMP_URL, ShopItem, ShopState


def tienda_hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Tienda · Bandcamp",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Tienda", class_name="block"),
                    rx.el.span(
                        "de Lorenly Music",
                        class_name="block italic text-[#ff5a4e]",
                    ),
                    class_name="mt-5 font-serif text-5xl leading-[0.95] text-stone-50 sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    "Los temas publicados en el Bandcamp oficial de Lorenly Music: «Magnolia», "
                    "«Cálida Esperanza» y «Sí».",
                    class_name="mt-7 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("shopping-bag", class_name="h-4 w-4"),
                        "Ir a lorenly.bandcamp.com",
                        href=BANDCAMP_URL,
                        target="_blank",
                        rel="noopener noreferrer",
                        class_name="flex w-fit items-center gap-3 bg-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.22em] text-[#141110] hover:bg-[#ff7468] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white",
                    ),
                    rx.el.a(
                        rx.icon("coffee", class_name="h-4 w-4"),
                        "Apoyar en Ko-fi",
                        href=KOFI,
                        target="_blank",
                        rel="noopener noreferrer",
                        class_name="flex w-fit items-center gap-3 border border-white/25 px-6 py-4 text-xs uppercase tracking-[0.22em] text-stone-100 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    class_name="mt-10 flex flex-wrap gap-4",
                ),
                class_name="lg:col-span-7 lg:pr-12",
            ),
            rx.el.div(
                rx.el.p(
                    ShopState.item_count.to_string(),
                    class_name="font-serif text-6xl text-[#ff5a4e]",
                ),
                rx.el.p(
                    "temas en Bandcamp",
                    class_name="mt-2 text-[11px] uppercase tracking-[0.24em] text-stone-300",
                ),
                rx.el.p(
                    "Cada enlace lleva directamente a su ficha oficial.",
                    class_name="mt-3 text-sm text-stone-500",
                ),
                class_name="mt-12 border-l border-[#ff5a4e]/60 pl-6 lg:col-span-5 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-start gap-6 px-6 pb-20 pt-16 lg:grid-cols-12",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _unavailable_note(item: ShopItem) -> rx.Component:
    return rx.cond(
        ShopState.unavailable.contains(item["key"]),
        rx.el.div(
            rx.icon("triangle-alert", class_name="h-5 w-5 text-[#ff5a4e]"),
            rx.el.p(
                "Si la ficha de Bandcamp no está disponible, escribe por WhatsApp o correo y "
                "se te envía el enlace directo.",
                class_name="mt-3 max-w-xl text-sm text-stone-300",
            ),
            rx.el.button(
                rx.icon("rotate-ccw", class_name="h-4 w-4"),
                "Ocultar aviso",
                on_click=lambda: ShopState.clear_unavailable(item["key"]),
                class_name="mt-4 flex w-fit items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-400 hover:text-[#ff5a4e] transition-colors",
            ),
            role="status",
            class_name="mt-6 border border-dashed border-white/20 bg-[#141110] p-6",
        ),
        rx.el.button(
            rx.icon("circle-help", class_name="h-4 w-4"),
            "El enlace no está disponible",
            on_click=lambda: ShopState.mark_unavailable(item["key"]),
            class_name="mt-6 flex w-fit items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-500 hover:text-[#ff5a4e] transition-colors",
        ),
    )


def _shop_card(item: ShopItem, **props) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.h2(
                item["title"],
                class_name="font-serif text-3xl text-stone-50 sm:text-4xl",
            ),
            rx.el.span(
                "Bandcamp",
                class_name="w-fit border border-[#ff5a4e]/60 px-3 py-1 text-[10px] uppercase tracking-[0.2em] text-[#ff5a4e]",
            ),
            class_name="flex flex-wrap items-center justify-between gap-4",
        ),
        rx.el.a(
            rx.icon("shopping-cart", class_name="h-4 w-4"),
            "Escuchar y comprar en Bandcamp",
            href=item["external"],
            target="_blank",
            rel="noopener noreferrer",
            aria_label=f"Escuchar y comprar {item['title']} en Bandcamp",
            class_name="mt-6 flex w-fit items-center gap-2 border border-white/20 px-5 py-3 text-[11px] uppercase tracking-[0.18em] text-stone-200 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
        ),
        _unavailable_note(item),
        class_name="border border-white/10 bg-[#1a1615] p-6 sm:p-8 hover:border-[#ff5a4e]/50 transition-colors",
        **props,
    )


def tienda_catalog() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Catálogo",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "Temas publicados",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                class_name="max-w-2xl",
            ),
            rx.el.div(
                rx.foreach(
                    ShopState.items,
                    lambda item: _shop_card(item, key=item["key"]),
                ),
                class_name="mt-12 flex flex-col gap-6",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-20",
        ),
        id="catalogo",
        class_name="border-b border-white/10 bg-[#141110]",
    )


def tienda_cta() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Pedidos y consultas",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h2(
                    "¿Buscas otro formato o una licencia?",
                    class_name="mt-3 font-serif text-4xl text-stone-50 sm:text-5xl",
                ),
                rx.el.p(
                    "Escribe si necesitas una licencia de uso para tu proyecto o un tema a medida. "
                    "También puedes apoyar la producción en Ko-fi.",
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


def tienda_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(tienda_hero(), tienda_catalog(), tienda_cta()),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
