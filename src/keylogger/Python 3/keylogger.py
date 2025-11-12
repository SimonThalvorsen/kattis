print(
    "".join(
        dict(
            zip(
                "clank bong click tap poing clonk clack ping tip cloing tic cling bing pong clang pang clong tac boing boink cloink rattle clock toc clink tuc".split(),
                list("abcdefghijklmnopqrstuvwxyz"),
            )
        )[input()]
        for _ in range(int(input()))
    ),
)
