BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'horizontal'
        TextInput:
            id: input_number
            text: '34'
            font_size: 48
            multiline: False
            input_filter: 'int'
            hint_text: 'Enter miles'
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: '+'
                font_size: 24
                on_press: app.handle_increment(1)
            Button:
                text: '-'
                font_size: 24
                on_press: app.handle_increment(-1)
    Button:
        text: 'Convert to km'
        size_hint_y: None
        height: '48dp'
        on_press: app.handle_calculate(input_number.text)
    Label:
        id: output_label
        text: "54.717"
        font_size: 48
        color: (0, 0, 1, 1)
