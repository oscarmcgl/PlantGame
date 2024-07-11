
#https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/

import plants as p


from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static, Input
from textual.containers import ScrollableContainer

class Title(Static):
    """A title widget."""

    def __init__(self, text: str):
        super().__init__(f"🌱 {text} 🌱")

class Login(Static):
    """A login widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle the button press event."""
        pass

class Menu(App):

    CSS_PATH = "interface.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Title("Plants in Bloom")
        yield Input(placeholder="Username", id="username", type="text")
        yield Input(placeholder="Password", id="password", type="text", password=True )
        yield Button("Login", id="login", variant="default")


    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = Menu()
    app.run()