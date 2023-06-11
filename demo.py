from TextAdventures import GoTo, Interaction, Options, Scene, Text

finalScene = Scene("Final Scene", [
    Text("That's all for now folks!")
])

sceneInteractionSuccess = Scene("\033[32mInteraction Success", [
    Text("You did it!"),
    GoTo(finalScene)
])
sceneInteractionFailure = Scene("\033[31mInteraction Fail", [
    Text("Oh no! You didn't interact in time..."),
    GoTo(finalScene)
])
sceneInteraction = [
    Text("Quick! Press the space key within two seconds!"),
    Interaction(
        success=GoTo(sceneInteractionSuccess),
        failure=GoTo(sceneInteractionFailure)
    )
]

sceneA = Scene("Scene A", [
    Text("This is Scene A!"),
    *sceneInteraction
])
sceneB = Scene("Scene B", [
    Text("This is Scene B!"),
    *sceneInteraction
])
sceneC = Scene("Scene C", [
    Text("This is Scene C!"),
    *sceneInteraction
])

scene = Scene("\033[34mText Adventure", [
    Text("Multiline\ndescription!"),
    Options("Pick an option:", {
        "A": GoTo(sceneA),
        "B": GoTo(sceneB),
        "C": GoTo(sceneC)
    })
])

scene.run()
