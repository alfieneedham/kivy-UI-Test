import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Application(App):
    def build(self):
        layout = GridLayout(cols=2)

        self.numClicks = 0

        self.increaseCounter = Button(text = "Click Me.")
        self.increaseCounter.bind(on_press = self.increase_counter)
        layout.add_widget(self.increaseCounter)
        self.totalNumClicks = Label(text = "Total Clicks: " + str(self.numClicks))
        layout.add_widget(self.totalNumClicks)

        return layout

    def increase_counter(self, instance):
        self.numClicks += 1
        self.totalNumClicks.text = "Total Clicks: " + str(self.numClicks)

if __name__ == "__main__":
    myApp = Application()
    myApp.run()