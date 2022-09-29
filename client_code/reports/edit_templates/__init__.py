import anvil.server
import anvil

from ._anvil_designer import edit_templatesTemplate


class edit_templates(edit_templatesTemplate):
    def __init__(self, survey_row, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.tag.survey_row = survey_row

        # Any code you write here will run when the form opens.
        rows = anvil.server.call("get_templates")
        self.repeating_panel_1.items = rows

    def link_back_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.open_form("reports.main", self.tag.survey_row)
