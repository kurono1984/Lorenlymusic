import reflex as rx

from app.states.site_content_state import ContentState, NavLink
from app.states.site_state import SiteState


def _desktop_link(link: NavLink, **props) -> rx.Component:
    return rx.el.a(
        link["label"],
        href=link["href"],
        class_name="relative text-[13px] uppercase tracking-[0.18em] text-stone-200 hover:text-[#ff5a4e] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#ff5a4e] transition-colors py-2",
        **props,
    )


def _mobile_link(link: NavLink, **props) -> rx.Component:
    return rx.el.a(
        rx.el.span(link["label"]),
        rx.icon("arrow-up-right", class_name="h-4 w-4 text-[#ff5a4e]"),
        href=link["href"],
        on_click=SiteState.close_menu,
        class_name="flex items-center justify-between border-b border-white/10 py-4 text-lg font-medium text-stone-100 hover:text-[#ff5a4e] transition-colors",
        **props,
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.icon("disc-3", class_name="h-6 w-6 text-[#ff5a4e]"),
                rx.el.span(
                    rx.el.span(
                        "Lorenly",
                        class_name="font-serif text-xl tracking-tight",
                    ),
                    rx.el.span(
                        "Music",
                        class_name="ml-1 text-[11px] uppercase tracking-[0.35em] text-[#ff5a4e]",
                    ),
                    class_name="flex items-baseline text-stone-50",
                ),
                href="/",
                class_name="flex items-center gap-3 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#ff5a4e]",
            ),
            rx.el.nav(
                rx.foreach(
                    ContentState.nav_links,
                    lambda link: _desktop_link(link, key=link["href"]),
                ),
                class_name="hidden lg:flex items-center gap-6",
                aria_label="Navegación principal",
            ),
            rx.el.button(
                rx.cond(
                    SiteState.menu_open,
                    rx.icon("x", class_name="h-6 w-6"),
                    rx.icon("menu", class_name="h-6 w-6"),
                ),
                on_click=SiteState.toggle_menu,
                aria_label="Abrir menú de navegación",
                aria_expanded=SiteState.menu_open,
                class_name="lg:hidden text-stone-100 p-2 -mr-2 hover:text-[#ff5a4e] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#ff5a4e]",
            ),
            class_name="mx-auto flex w-full max-w-7xl items-center justify-between gap-6 px-6 py-5",
        ),
        rx.cond(
            SiteState.menu_open,
            rx.el.nav(
                rx.foreach(
                    ContentState.nav_links,
                    lambda link: _mobile_link(link, key=link["href"]),
                ),
                class_name="lg:hidden border-t border-white/10 bg-[#141110] px-6 pb-8",
                aria_label="Navegación móvil",
            ),
            rx.fragment(),
        ),
        class_name="sticky top-0 z-50 border-b border-white/10 bg-[#141110]/95 backdrop-blur",
    )
