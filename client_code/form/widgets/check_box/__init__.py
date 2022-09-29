import anvil

from ._anvil_designer import check_boxTemplate
from .check_box_other import check_box_other


class check_box(check_boxTemplate):
    def __init__(self, options, **properties):
        self.init_components(**properties)

        self.tag.logic = None
        self.tag.options = options

        for op in options["regular_options"]:
            c = anvil.CheckBox(text=op, foreground="black")
            self.column_panel.add_component(c)

        if options["other_option"]:
            check_other_form = check_box_other()
            check_other_form.text_box.placeholder = options["other_placeholder"]
            check_other_form.check_box.text = options["other_option"]

            self.column_panel.add_component(check_other_form)
