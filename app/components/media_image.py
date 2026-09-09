import reflex as rx

from app.states.site_state import SiteState


def safe_image(
    key: str,
    src: str,
    alt: str,
    class_name: str,
    ratio: str = "aspect-[4/5]",
) -> rx.Component:
    """Imagen real con un estado accesible de reserva si no está disponible."""
    return rx.cond(
        SiteState.broken_images.contains(key),
        rx.el.div(
            rx.icon("image-off", class_name="h-8 w-8 text-[#ff5a4e]"),
            rx.el.p(
                alt,
                class_name="mt-3 max-w-xs text-center text-sm text-stone-300",
            ),
            rx.el.p(
                "La imagen no está disponible en este momento.",
                class_name="mt-1 text-xs text-stone-500",
            ),
            role="img",
            aria_label=alt,
            class_name=f"flex w-full {ratio} flex-col items-center justify-center border border-dashed border-white/20 bg-[#1c1817] p-6",
        ),
        rx.el.img(
            src=src,
            alt=alt,
            loading="lazy",
            referrer_policy="no-referrer",
            class_name=class_name,
        ),
    )
