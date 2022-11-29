import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Application(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text="FirstNumber"))
        self.firstNumberInput = TextInput(multiline = False)
        layout.add_widget(self.firstNumberInput)

        layout.add_widget(Label(text="SecondNumber"))
        self.secondNumberInput = TextInput(multiline = False)
        layout.add_widget(self.secondNumberInput)

        self.calculateButton = Button(text="Add")
        self.calculateButton.bind(on_press = self.handle_click)
        layout.add_widget(self.calculateButton)
        self.resultLabel = Label(text="")
        layout.add_widget(self.resultLabel)

        return layout

    def handle_click(self, instance):
        result = self.get_first_number() + self.get_second_number()
        self.resultLabel.text = ("Result: " + str(result))

    def get_first_number(self):
        return int(self.firstNumberInput.text)
    
    def get_second_number(self):
        return int(self.secondNumberInput.text)

if __name__ == "__main__":
    myApp = Application()
    myApp.run()