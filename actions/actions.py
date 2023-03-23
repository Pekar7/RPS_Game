from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
import score as score


class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def computer_choice(self) -> str:
        generatednum = random.randint(1, 3)
        computerchoice = ""
        if generatednum == 1:
            computerchoice = "камень"
        elif generatednum == 2:
            computerchoice = "бумага"
        elif generatednum == 3:
            computerchoice = "ножницы"

        return (computerchoice)

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"Твой выбор: {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"Выбор компьютера: {comp_choice}")

        if user_choice == "камень" and comp_choice == "ножницы":
            dispatcher.utter_message(text="Поздравляю, ты победил")
            score.user += 1
        elif user_choice == "камень" and comp_choice == "бумага":
            dispatcher.utter_message(text="Компьютер победил тебя в этот раз")
            score.rasa_bot += 1
        elif user_choice == "бумага" and comp_choice == "камень":
            dispatcher.utter_message(text="Поздравляю, ты победил")
            score.user += 1
        elif user_choice == "бумага" and comp_choice == "ножницы":
            dispatcher.utter_message(text="Компьютер победил тебя в этот раз")
            score.rasa_bot += 1
        elif user_choice == "ножницы" and comp_choice == "бумага":
            dispatcher.utter_message(text="Поздравляю, ты победил")
            score.user += 1
        elif user_choice == "ножницы" and comp_choice == "камень":
            dispatcher.utter_message(text="Компьютер победил тебя в этот раз")
            score.rasa_bot += 1
        else:
            dispatcher.utter_message(text="Ничья!")
            score.tie += 1

        return []


class ActionShowScore(Action):

    def name(self) -> Text:
        return "action_show_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"Твои победы: {score.user}")
        dispatcher.utter_message(text=f"Побед компьютера: {score.rasa_bot}")
        dispatcher.utter_message(text=f"Ничьих: {score.tie}")

        return []
