# TextAdventures

A Python library for easily making text adventure games.

Inspired by [`textadventure`](https://pypi.org/project/textadventure/).

* [See on Replit](https://replit.com/@QwertyQwerty54/TextAdventures)
* [See on GitHub](https://github.com/Qwerty-Qwerty88/Text-Adventures)

## Getting Started

<!--
Install the library using `pip` or your package manager of choice:

```
pip install TextAdventures
```
-->

And add this code to import the package:

```python
import TextAdventures
```

Or:

```python
from TextAdventures import GoTo, Interaction, Options, Scene, Text
```

## `Scene`

To create a `Scene`, add this code:

```python
myScene = TextAdventures.Scene()
```

Or:

```python
myScene = Scene()
```

`Scene`s take 2 arguments:

- `title`: a string that gets printed at the top of the console.
- `actions`: a `list`/`tuple` of `Action`s that will be ran in order.

## `Action`s

`Action`s can be set to run in a `Scene`. There are currently 4 options:

- `Text`
- `GoTo`
- `Options`
- `Interaction`

But you can expect more soon, or if you don't want to wait, you can make your own! There is a _very_ simple `Action` class that you can import to create your own `Action`s.
