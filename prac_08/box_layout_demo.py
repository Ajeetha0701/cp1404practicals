from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet button press event."""
        input_name = self.root.ids.input_name.text.strip()  # Remove leading and trailing whitespaces
        if input_name:  # Check if input is not empty
            self.root.ids.output_label.text = f"Hello {input_name}"
        else:
            self.root.ids.output_label.text = "Please enter a name"

    def handle_clear(self):
        """Handle the clear button press event."""
        self.root.ids.output_label.text = ""  # Clear the output label
        self.root.ids.input_name.text = ""    # Clear the input text


if __name__ == "__main__":
    BoxLayoutDemo().run()

