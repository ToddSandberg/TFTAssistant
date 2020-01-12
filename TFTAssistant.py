import kivy

kivy.require('1.0.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from Models.PredictionResult import PredictionResult
from kivy.clock import Clock

# Set the size of the window
from kivy.config import Config
Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 100)


# Widget with UI logic
class RecommendedPicksWidget(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='horizontal')
        self.add_widget(Label(text="Start up a game of TFT to start assistant"))
        # TODO add interval to check if screen has changed
        # something like this? Clock.schedule_interval(self.update, 1 / 30.0)

        # TODO Obtain array from external api, this is just test data now
        recommended_picks = [
            PredictionResult("leona", 50.0, "good"),
            PredictionResult("singed", 10.0, "good")
        ]
        self.update(recommended_picks)

    def update(self, recommended):
        # Clear existing widgets
        children = self.children[:]
        self.clear_widgets(children)

        # TODO sort prediction results
        for i in range(min(5, len(recommended))):
            pick = recommended[i]
            # TODO get champion picture, maybe from folder
            self.add_widget(Label(text=pick.champion_name + "\n" + str(pick.probability) + "%"))
            # TODO add reason on hover over
        self.canvas.ask_update()


# App that contains widget
class RecommendedPicksWindow(App):

    def build(self):
        return RecommendedPicksWidget()


if __name__ == '__main__':
    RecommendedPicksWindow().run()
