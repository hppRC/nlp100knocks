print(
    *map(
        lambda x: len(x),
        "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        .replace(",", "")
        .replace(".", "")
        .split(" ")
    )
)