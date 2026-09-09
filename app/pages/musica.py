import reflex as rx

from app.components.footer import BANDCAMP, footer
from app.components.navbar import navbar
from app.states.music_catalog_state import CatalogState, CatalogTrack


def _count_pill(name: str, count: int, detail: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            f"{count}",
            class_name="font-serif text-4xl text-[#ff5a4e]",
        ),
        rx.el.p(
            name,
            class_name="mt-2 text-[11px] uppercase tracking-[0.24em] text-stone-300",
        ),
        rx.el.p(detail, class_name="mt-2 text-sm text-stone-500"),
        class_name="w-full border-l border-[#ff5a4e]/60 pl-5",
    )


def catalog_header() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Catálogo completo",
                    class_name="text-[11px] uppercase tracking-[0.32em] text-[#ff5a4e]",
                ),
                rx.el.h1(
                    rx.el.span("Música", class_name="block"),
                    rx.el.span(
                        "de Lorenly",
                        class_name="block italic text-[#ff5a4e]",
                    ),
                    class_name="mt-5 font-serif text-5xl leading-[0.95] text-stone-50 sm:text-6xl lg:text-7xl",
                ),
                rx.el.p(
                    "Todo el repertorio publicado, organizado en instrumentales, canciones como "
                    "cantautora y canciones como VocaloP.",
                    class_name="mt-7 max-w-xl text-lg leading-relaxed text-stone-300",
                ),
                class_name="lg:col-span-7 lg:pr-12",
            ),
            rx.el.div(
                _count_pill(
                    "Instrumental",
                    CatalogState.counts_by_category["Instrumental"],
                    "Piezas instrumentales publicadas.",
                ),
                _count_pill(
                    "Cantautora",
                    CatalogState.counts_by_category[
                        "Canciones como cantautora"
                    ],
                    "Canciones firmadas como cantautora.",
                ),
                _count_pill(
                    "VocaloP",
                    CatalogState.counts_by_category["Canciones como VocaloP"],
                    "Canciones producidas con voces sintetizadas.",
                ),
                class_name="mt-12 flex flex-col gap-8 lg:col-span-5 lg:mt-0",
            ),
            class_name="mx-auto grid w-full max-w-7xl grid-cols-1 items-start gap-6 px-6 pb-20 pt-16 lg:grid-cols-12",
        ),
        class_name="border-b border-white/10 bg-[#141110]",
    )


def _category_button(name: str, **props) -> rx.Component:
    return rx.el.button(
        rx.el.span(name),
        rx.el.span(
            CatalogState.counts_by_category.get(name, 0).to_string(),
            class_name="ml-2 text-[10px] text-stone-400",
        ),
        on_click=lambda: CatalogState.set_category(name),
        aria_pressed=CatalogState.category == name,
        class_name=rx.cond(
            CatalogState.category == name,
            "flex items-center border border-[#ff5a4e] bg-[#ff5a4e] px-4 py-2 text-[11px] uppercase tracking-[0.18em] text-[#141110] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white",
            "flex items-center border border-white/20 px-4 py-2 text-[11px] uppercase tracking-[0.18em] text-stone-300 hover:border-[#ff5a4e] hover:text-[#ff5a4e] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ff5a4e]",
        ),
        **props,
    )


def catalog_controls() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "Buscar por título",
                html_for="buscar-cancion",
                class_name="block text-[11px] uppercase tracking-[0.24em] text-stone-400",
            ),
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-stone-500",
                ),
                rx.el.input(
                    id="buscar-cancion",
                    type="search",
                    placeholder="Ej. Clavelina, La Achirana…",
                    default_value=CatalogState.query,
                    on_change=CatalogState.set_query.debounce(300),
                    class_name="w-full border border-white/20 bg-[#1a1615] py-3 pl-11 pr-4 text-base text-stone-100 placeholder:text-stone-500 focus:border-[#ff5a4e] focus:outline-none focus:ring-1 focus:ring-[#ff5a4e]",
                ),
                class_name="relative mt-3",
            ),
            class_name="w-full lg:max-w-sm",
        ),
        rx.el.div(
            rx.el.p(
                "Filtrar por categoría",
                class_name="text-[11px] uppercase tracking-[0.24em] text-stone-400",
            ),
            rx.el.div(
                rx.foreach(
                    CatalogState.categories,
                    lambda name: _category_button(name, key=name),
                ),
                class_name="mt-3 flex flex-wrap gap-2",
                role="group",
                aria_label="Filtros por categoría",
            ),
            class_name="w-full",
        ),
        class_name="flex flex-col gap-8 border border-white/10 bg-[#1a1615] p-6 lg:flex-row lg:items-start lg:justify-between",
    )


def _catalog_row(track: CatalogTrack, **props) -> rx.Component:
    return rx.el.li(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    track["category"],
                    class_name="text-[10px] uppercase tracking-[0.26em] text-[#ff5a4e]",
                ),
                rx.el.h3(
                    track["title"],
                    class_name="mt-2 font-serif text-2xl text-stone-50 sm:text-3xl",
                ),
                class_name="min-w-0 flex-1",
            ),
            rx.icon(
                "music",
                class_name="mt-2 h-5 w-5 shrink-0 text-stone-600",
            ),
            class_name="flex flex-row items-start justify-between gap-5",
        ),
        class_name="border-t border-white/10 py-8 first:border-t-0 hover:bg-white/[0.02] transition-colors",
        **props,
    )


def empty_state() -> rx.Component:
    return rx.el.div(
        rx.icon("search-x", class_name="h-8 w-8 text-[#ff5a4e]"),
        rx.el.p(
            "Sin coincidencias",
            class_name="mt-4 font-serif text-2xl text-stone-50",
        ),
        rx.el.p(
            "No hay canciones que coincidan con la búsqueda o el filtro elegido.",
            class_name="mt-2 max-w-md text-sm text-stone-400",
        ),
        rx.el.button(
            rx.icon("rotate-ccw", class_name="h-4 w-4"),
            "Limpiar búsqueda y filtros",
            on_click=CatalogState.clear_filters,
            class_name="mt-6 flex items-center gap-2 bg-[#ff5a4e] px-5 py-3 text-[11px] uppercase tracking-[0.18em] text-[#141110] hover:bg-[#ff7468] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white",
        ),
        class_name="flex flex-col items-center justify-center border border-dashed border-white/20 bg-[#1a1615] px-6 py-20 text-center",
    )


def catalog_results() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                rx.el.span(
                    CatalogState.filtered_count.to_string(),
                    class_name="font-serif text-2xl text-stone-50",
                ),
                rx.el.span(
                    f" de {CatalogState.total_count} piezas",
                    class_name="text-sm text-stone-400",
                ),
                class_name="flex items-baseline gap-2",
            ),
            rx.cond(
                CatalogState.is_filtered,
                rx.el.button(
                    rx.icon("x", class_name="h-4 w-4"),
                    "Limpiar filtros",
                    on_click=CatalogState.clear_filters,
                    class_name="flex items-center gap-2 text-[11px] uppercase tracking-[0.18em] text-stone-400 hover:text-[#ff5a4e] transition-colors",
                ),
                rx.fragment(),
            ),
            class_name="mt-12 flex flex-wrap items-center justify-between gap-4 border-b border-white/10 pb-4",
            aria_live="polite",
        ),
        rx.cond(
            CatalogState.has_results,
            rx.el.ul(
                rx.foreach(
                    CatalogState.filtered,
                    lambda track: _catalog_row(track, key=track["key"]),
                ),
                class_name="mt-2",
            ),
            rx.el.div(empty_state(), class_name="mt-10"),
        ),
        class_name="w-full",
    )


def catalog_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            catalog_controls(),
            catalog_results(),
            rx.el.a(
                rx.icon("shopping-bag", class_name="h-4 w-4"),
                "Catálogo en Bandcamp",
                href=BANDCAMP,
                target="_blank",
                rel="noopener noreferrer",
                class_name="mt-14 flex w-fit items-center gap-3 border border-[#ff5a4e] px-6 py-4 text-xs uppercase tracking-[0.2em] text-[#ff5a4e] hover:bg-[#ff5a4e] hover:text-[#141110] transition-colors",
            ),
            class_name="mx-auto w-full max-w-7xl px-6 py-20",
        ),
        id="catalogo",
        class_name="bg-[#141110]",
    )


def musica_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(catalog_header(), catalog_section()),
        footer(),
        class_name="min-h-screen bg-[#141110] font-['Inter'] antialiased selection:bg-[#ff5a4e] selection:text-[#141110]",
    )
