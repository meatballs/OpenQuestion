import anvil.server

from ....utilities import augment
from ._anvil_designer import markdownTemplate


class markdown(markdownTemplate):
    def __init__(self, section, **properties):
        self.init_components(**properties)

        augment.set_event_handler(
            self.column_panel_container, "click", self.column_panel_container_click
        )

        from ..toolbar import toolbar

        toolbar = toolbar(align="left", section=section, parent=self)
        self.add_component(toolbar)

    def text_area_lost_focus(self, **event_args):

        text = self.text_area_text.text

        if text:
            html = anvil.server.call("convert_markdown", text)
            self.markdown_display.html = html
            self.column_panel_container.visible = True
            self.text_area_text.visible = False

    def column_panel_container_click(self, **event_args):
        self.text_area_text.visible = True
        self.text_area_text.focus()
        self.column_panel_container.visible = False
