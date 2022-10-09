from typing import Optional


class GameUIAdapter:
    @staticmethod
    def get_question_choice_selected(form: dict[str, str]) -> Optional[int]:
        """
        Gets choice selected by the user in the UI if it exists.

        :param form: payload of user request
        """
        return next((key for key in form.keys() if key.startswith("choice_")), None)
