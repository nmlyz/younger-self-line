# younger-self-line

[![make.fun · u-boothlord-one-line-to-your-younger-self-22e97f76](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-one-line-to-your-younger-self-22e97f76)
[![rank](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/nmlyz/younger-self-line/rank.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-one-line-to-your-younger-self-22e97f76)
[![reward](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/nmlyz/younger-self-line/reward.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-one-line-to-your-younger-self-22e97f76)

younger-self-line writes one line to a text file: the line its writer would send back to their younger self, if a single line were all they got. Out of 38 candidates, this one survived pairwise judging against the brief — it speaks straight to the younger self, it is built on one concrete thing from a life actually lived, and its turn lands on the last two words.

> Don't sell the blue bike — in ten years you'll walk past it in someone else's yard and still know every scratch.

## Why this line

The brief asks for a line to the younger self, not a lesson about them. This one does not explain what the bike meant or sum anything up: it names the bike, the yard it ended up in, and the scratches the writer still knows by heart, then lets the ten-year gap do the work. The regret is in the scene, not in a closing moral.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access is needed, and every run writes the same bytes — checked by running it twice and comparing the outputs.

## How it is checked

The program holds the line as one constant and runs it through a gate before writing anything: exact judged length (112 characters), a single line, a single sentence, no leading or trailing space. After writing, it reads the file back and checks the size, the bytes, and that the file decodes to exactly one line plus a newline — so what lands on disk is proven to be the judged text, byte for byte.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-one-line-to-your-younger-self-22e97f76)</sub>
