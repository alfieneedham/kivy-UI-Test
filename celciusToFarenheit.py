import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Application(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text = "Enter temperature in celcius:"))
        self.tempInCelcius = TextInput(multiline = False)
        layout.add_widget(self.tempInCelcius)

        self.calculateButton = Button(text = "Convert to farenheit: ")
        self.calculateButton.bind(on_press = self.convert_to_farenheit)
        layout.add_widget(self.calculateButton)
        self.resultLabel = Label(text = "")
        layout.add_widget(self.resultLabel)
        
        return layout

    def convert_to_farenheit(self, instance):
        tempInFarenheit = self.get_temp_in_celcius() * 1.8 + 32
        self.resultLabel.text = ("Temp in farenheit: " + str(tempInFarenheit))

    def get_temp_in_celcius(self):
        return float(self.tempInCelcius.text)

if __name__ == "__main__":
    myApp = Application()
    myApp.run()