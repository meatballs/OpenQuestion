from ._anvil_designer import drop_downTemplate


class drop_down(drop_downTemplate):
    def __init__(self, section, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.tag.logic = None
        # self.tag.visible=True

        # Any code you write here will run when the form opens.
        from ..toolbar import toolbar

        toolbar = toolbar(align="left", section=section, parent=self)
        self.add_component(toolbar)
