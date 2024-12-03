# Advent of Code 2024 - Gemini Challenge

This repository documents an experiment where Google's Gemini AI model (`gemini-exp-1121`) attempts to solve the [Advent of Code](https://adventofcode.com/) challenges. The goal is to evaluate Gemini's capabilities in understanding and solving complex programming problems.

## Setup & Running the Solutions

1. Clone the repository:
```
git clone [repository-url]
cd advent-of-code-gemini
```

2. Create and activate a virtual environment:
```
python -m venv venv-advent-of-code
source venv-advent-of-code/bin/activate  # On Unix/macOS
# or
.\venv-advent-of-code\Scripts\activate  # On Windows
```

3. Run solutions:
```
python dayXX/part1.py < dayXX/input.txt  # For part 1
python dayXX/part2.py < dayXX/input.txt  # For part 2
```

## Progress Overview

| Day | Model ID  | Part 1 | Part 2 | Attempts (P1/P2) | Prompt Type | Gemini Chat Link | Notes |
|-----|-----------|--------|--------|------------------|-------------|------------------|-------|
| 01  | gemini-exp-1121 | ✅     | ✅     | 1/1              | Zero-shot   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221kkRVShxln7z6qfKgsVEtP20hozJj7YkA%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |       |
| 02  | gemini-exp-1121 | ✅     | ✅     | 1/1              | Zero-shot   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221RLXAgFWunvpYsyfIxwo-AUN4a9kjhTRl%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |       |
| 03  | gemini-exp-1121 | ✅     | ✅     | 1/2              | Zero-shot   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221f0KmVrz838uuehNbgh209gEqR726Utg5%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     | first attempt for part 2 led to a `ValueError` due to improper handling of regex groups     |

Legend:
- ✅ Solved
- ❌ Not solved yet
- `-` Not attempted

## Repository Structure

Each day's challenge is organized in its own directory:
```
dayXX/
├── input.txt         # Challenge input
├── part1-problem.txt # Problem description for part 1
├── part2-problem.txt # Problem description for part 2
├── part1.py         # Solution for part 1
└── part2.py         # Solution for part 2
```

## About the Project

This project aims to:
1. Test Gemini's ability to understand complex problem statements
2. Evaluate its code generation capabilities
3. Document the interaction patterns that lead to successful solutions
4. Provide a reproducible framework for AI-assisted problem solving

## Contributing

Feel free to:
- Submit improvements to the solutions
- Add better documentation
- Share insights about Gemini's problem-solving patterns
- Report issues or suggest improvements

## License

MIT License