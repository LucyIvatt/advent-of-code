# advent-of-code

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white) ![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)

This repository contains all of my solutions for the [advent of code](https://adventofcode.com/) challenges between 2021-2025.

All solutions are written in Python or Typescript (or hopefully Go for 2026!).

| Key |    Value     |
|-----|:------------:|
| ⭐   |   2 stars    |
| ⭑   |    1 star    |
| ⭑   |    1 star    |
| ─   | Not released |
| ➖   |     N/A*     |

**2025 onwards no longer have 25 days of challenges, instead having only 12*

Python: 🐍 Typescript: ⌨️ Go: 🦫

|        | 2021 🐍 | 2022 🐍 | 2023 🐍 | 2024 ⌨️ | 2025 🐍 | 2026 🦫 |
|--------|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| Day 1  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 2  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 3  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 4  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 5  |    ⭐    |    ⭐    |    ⭑    |    ⭐    |    ⭐    |    ─    |
| Day 6  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 7  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 8  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 9  |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭑    |    ─    |
| Day 10 |    ⭐    |    ⭐    |    ⭑    |    ⭐    |    ⭐    |    ─    |
| Day 11 |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ─    |
| Day 12 |    ⭐    |    ⭐    |         |    ⭐    |    ⭑    |    ─    |
| Day 13 |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ➖    |    ➖    |
| Day 14 |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ➖    |    ➖    |
| Day 15 |    ⭐    |    ⭐    |    ⭐    |    ⭐    |    ➖    |    ➖    |
| Day 16 |    ⭐    |         |    ⭐    |    ⭐    |    ➖    |    ➖    |
| Day 17 |    ⭐    |         |         |   ⭐\*   |    ➖    |    ➖    |
| Day 18 |         |         |         |    ⭐    |    ➖    |    ➖    |
| Day 19 |         |         |         |    ⭐    |    ➖    |    ➖    |
| Day 20 |         |         |         |         |    ➖    |    ➖    |
| Day 21 |         |         |         |         |    ➖    |    ➖    |
| Day 22 |         |         |         |         |    ➖    |    ➖    |
| Day 23 |         |         |         |         |    ➖    |    ➖    |
| Day 24 |         |         |         |         |    ➖    |    ➖    |
| Day 25 |         |         |         |         |    ➖    |    ➖    |
| Total  |  34/50  |  30/50  |  28/50  |  38/50  |  22/24  |    ─    |
| %      | **68%** | **60%** | **56%** | **76%** | **92%** |  **─**  |

_\*with the amount of help I needed from reddit & friends, I don't think p2 for this one reaaaally counts_ 😂

_\**2025 onwards no longer have 25 days of challenges, instead having only 12_

## Python Run Config

Given I have a slightly cursed module setup 🫠

### Code Runner Executor Config
```json
    "code-runner.executorMap": {
        "python": "cd $dir && PYTHONPATH={path-to-repo}/advent-of-code python3 \"$fileName\""
    },
    "code-runner.executorMapByGlob": {
        "*.spec.ts": "npm t",
    },
```

### VsCode launch.json Config
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "cwd": "${fileDirname}",
      "env": {
        "PYTHONPATH": "{path-to-repo}/advent-of-code"
      },
      "console": "integratedTerminal"
    }
  ]
}
```

## TO-DO
- [ ] Update scripts and/or structure of the `advent-of-code-inputs` private repo to respect the new `typescript/` & `python/` folder structures when backing up and restoring text file inputs
- [ ] Add missing backups for inputs for 2024 because they were on my old laptop and I didn't back them up 🙄
- [ ] Add further notes about local setup of the repo & tests in VSCode
- [ ] Automatically save inputs to backup repo on push?
