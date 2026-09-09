import reflex as rx


class SiteState(rx.State):
    """Navegación compartida y estados accesibles para medios."""

    menu_open: bool = False
    broken_images: list[str] = []
    active_embeds: list[str] = []

    @rx.event
    def toggle_menu(self):
        self.menu_open = not self.menu_open

    @rx.event
    def close_menu(self):
        self.menu_open = False

    @rx.event
    def image_failed(self, key: str):
        if key not in self.broken_images:
            self.broken_images.append(key)

    @rx.event
    def activate_embed(self, key: str):
        if key not in self.active_embeds:
            self.active_embeds.append(key)

    @rx.event
    def deactivate_embed(self, key: str):
        if key in self.active_embeds:
            self.active_embeds.remove(key)
