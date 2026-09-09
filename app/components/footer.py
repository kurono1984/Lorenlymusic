import reflex as rx

from app.states.site_content_state import ContentState, NavLink

PHONE = "+51965048629"
PHONE_DISPLAY = "+51 965 048 629"
WHATSAPP = "https://wa.me/51965048629"
EMAIL = "lorenly75@gmail.com"
BANDCAMP = "https://lorenly.bandcamp.com"
KOFI = "https://ko-fi.com/lorenly"


def _footer_link(link: NavLink, **props) -> rx.Component:
    return rx.el.a(
        link["label"],
        href=link["href"],
        class_name="block py-1 text-sm text-stone-400 hover:text-[#ff5a4e] transition-colors",
        **props,
    )


def contact_button(
    icon: str, label: str, value: str, href: str
) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5 text-[#ff5a4e] shrink-0"),
        rx.el.span(
            rx.el.span(
                label,
                class_name="block text-[11px] uppercase tracking-[0.22em] text-stone-400",
            ),
            rx.el.span(value, class_name="block text-base text-stone-50"),
        ),
        href=href,
        class_name="flex items-center gap-4 border border-white/15 px-5 py-4 hover:border-[#ff5a4e] hover:bg-white/5 transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ff5a4e]",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Lorenly Music",
                    class_name="font-serif text-3xl text-stone-50",
                ),
                rx.el.p(
                    "Productora musical VOCALOID. Canciones originales en español compuestas, arregladas y producidas desde Lima, Perú.",
                    class_name="mt-4 max-w-sm text-sm leading-relaxed text-stone-400",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("shopping-bag", class_name="h-4 w-4"),
                        "Bandcamp",
                        href=BANDCAMP,
                        target="_blank",
                        rel="noopener noreferrer",
                        class_name="flex w-fit items-center gap-2 border border-white/20 px-4 py-2 text-xs uppercase tracking-[0.2em] text-stone-200 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    rx.el.a(
                        rx.icon("coffee", class_name="h-4 w-4"),
                        "Ko-fi",
                        href=KOFI,
                        target="_blank",
                        rel="noopener noreferrer",
                        class_name="flex w-fit items-center gap-2 border border-white/20 px-4 py-2 text-xs uppercase tracking-[0.2em] text-stone-200 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors",
                    ),
                    class_name="mt-6 flex flex-wrap gap-3",
                ),
                class_name="max-w-md",
            ),
            rx.el.div(
                rx.el.h2(
                    "Secciones",
                    class_name="text-[11px] uppercase tracking-[0.25em] text-[#ff5a4e]",
                ),
                rx.el.nav(
                    rx.foreach(
                        ContentState.nav_links,
                        lambda link: _footer_link(link, key=link["href"]),
                    ),
                    class_name="mt-4 flex flex-col",
                    aria_label="Navegación del pie de página",
                ),
            ),
            rx.el.div(
                rx.el.h2(
                    "Contacto",
                    class_name="text-[11px] uppercase tracking-[0.25em] text-[#ff5a4e]",
                ),
                rx.el.div(
                    contact_button(
                        "phone", "Teléfono", PHONE_DISPLAY, f"tel:{PHONE}"
                    ),
                    contact_button(
                        "message-circle", "WhatsApp", "Escribir ahora", WHATSAPP
                    ),
                    contact_button("mail", "Correo", EMAIL, f"mailto:{EMAIL}"),
                    class_name="mt-4 flex flex-col gap-3",
                ),
            ),
            class_name="mx-auto grid w-full max-w-7xl gap-12 px-6 py-16 md:grid-cols-2 lg:grid-cols-[1.4fr_0.8fr_1.2fr]",
        ),
        rx.el.div(
            rx.el.p(
                "© Lorenly Music · Lima, Perú. Todos los derechos reservados.",
                class_name="text-xs text-stone-500",
            ),
            rx.el.a(
                "Política de privacidad",
                href="/privacy-policy",
                class_name="text-xs text-stone-400 underline decoration-[#ff5a4e]/60 underline-offset-4 hover:text-[#ff5a4e]",
            ),
            class_name="mx-auto flex w-full max-w-7xl flex-col gap-3 border-t border-white/10 px-6 py-6 sm:flex-row sm:items-center sm:justify-between",
        ),
        class_name="border-t border-white/10 bg-[#141110]",
    )
