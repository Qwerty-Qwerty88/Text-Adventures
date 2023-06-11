"""A Python library for easily making text adventure games.

Please view the `README.md` file [on Replit](https://replit.com/@QwertyQwerty54/TextAdventures#README.md) or [on GitHub](https://github.com/Qwerty-Qwerty88/Text-Adventures) to get started.
"""

from typing import Iterable
from getkey import getkey, keys
from .timing import timeEvent

clear = lambda: print("\033c", end="", flush=True)


class Action:    
    """The base class for an `Action`."""
    
    def __init__(self) -> None:
        pass
        
    def run(self) -> None:
        pass


class Scene:
    """Represents a scene in a text adventure game."""
    
    def __init__(self, title: str, actions: Iterable[Action]) -> None:
        """Initializes a new `Scene` object with the given parameters.

Args:
- `title`: The title of the scene. Printed at the top of the Console when this scene is ran. It will automatically be bold.
- `actions`: An iterable containing all of the actions that will be run in order when this scene is ran.
"""
        
        self.title = title
        self.actions = actions

    def run(self):
        """Prints `title` and runs every `Action` in `actions` (in order). If there are multiple actions, prompts the user to continue after each one."""
        
        clear()
        for i in range(len(self.actions)):
            if self.title:
                print(f"\033[1m{self.title}\033[0m\n")
             
            self.actions[i].run()
            
            try:
                self.actions[i + 1]
            except IndexError:
                pass
            else:
                print("> Continue <")
                getkey()
                clear()


class Text(Action):
    """Prints `text` on the screen."""
    
    def __init__(self, text: str) -> None:
        """Initializes a new `Text` object with the given parameters.

Args:
- `text`: The text that will be printed when this `Action` is ran.
"""
        
        super().__init__()
        self.text = text
        
    def run(self) -> None:
        super().run()
        print(self.text)


class GoTo(Action):
    """Runs another scene. Should be at the end of the list of actions in a `Scene`."""
    
    def __init__(self, scene: Scene) -> None:
        """Initializes a new `GoTo` object with the given parameters.
        
Args:
- `scene`: The `Scene` that will be ran when this `Action` is ran.
"""
        
        super().__init__()
        self.scene = scene
        
    def run(self) -> None:
        """Starts the given scene."""
        
        super().run()
        self.scene.run()
        

class Options(Action):
    """Prompts and gives a set of options available to the player to choose from.

Example Usage:

```py
Options("Pick an option:", {
    "option1": TextAdventures.Text("Option 1 was selected!"),
    "option2": TextAdventures.Text("Option 2 was selected!")
})
```

Note - You should avoid keys like "0", "1", etc. since it might confuse users.
"""
    
    def __init__(self, prompt: str, options: dict[str: Action]) -> None:
        """Initialize a new `Options` object with the given parameters.
        
Args:
- `prompt`: The prompt given when users are asked to choose an option.
- `options`: Each key of the dictionary will be shown as an option, and the value is an `Action` that will be ran if the player chooses that option.
"""
        
        super().__init__()
        self.prompt = prompt
        self.options = options
        self.selectedOption = 0
                
    def printOptions(self) -> None:
        clear()
        print(self.prompt)
        for i in range(len(self.options)):
            option = list(self.options)[i]
            
            if i == self.selectedOption:
                print(f"> {option} <")
            else:
                print(f"  {option}")
        #print(self.selectedOption)
        
    def run(self) -> None:
        """Displays all available options and prompts for user input. Executes selected Action object when chosen by user."""
        
        super().run()
        self.printOptions()

        key = None
    
        while key != keys.ENTER:
            key = getkey()
            
            if key == keys.UP:
                self.selectedOption = len(self.options) - 1 if self.selectedOption == 0 else self.selectedOption - 1
            elif key == keys.DOWN:
                self.selectedOption = 0 if self.selectedOption == len(self.options) - 1 else self.selectedOption + 1
                
            self.printOptions()
    
        for i in range(len(self.options)):
            option = self.options[list(self.options)[i]]
    
            if i == self.selectedOption:
                option.run()
                break


class Interaction(Action):
    """Waits for the player to press the given `key` when ran. If they pressed the key in under `timeLimitSeconds`, `success` will be ran. Otherwise, `failure` will be ran."""
    
    def __init__(self, success: Action, failure: Action, key: str=keys.SPACE, timeLimitSeconds: float=2) -> None:
        """Initialize a new `Interaction` object with the given parameters.
        
Args:
- `success`: The `Action` that will be ran if the player presses the correct key in under `timeLimitSeconds`.
- `failure`: The `Action` that will be ran if the player does not press the correct key in under `timeLimitSeconds`.
- `key`: The key that will trigger `success` or `failure` when pressed. Defaulted is `getkey.keys.SPACE`.
- `timeLimitSeconds`: The time (in seconds) that the player has to successfully press `key`. Default is `2`.
"""
        
        super().__init__()
        self.success = success
        self.failure = failure
        self.key = key
        self.timeLimit = timeLimitSeconds

    def run(self) -> None:
        super().run()
        time, key = 0, ""

        while key != self.key:
            time, key = timeEvent(getkey)

        self.success.run() if time < self.timeLimit else self.failure.run()

    