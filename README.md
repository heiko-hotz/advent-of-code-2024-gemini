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

3. Get the input files and problem statements:
   - Visit [Advent of Code](https://adventofcode.com/)
   - For each day:
     - Create `dayXX/input.txt` with your puzzle input
     - Create `dayXX/part1-problem.txt` and `dayXX/part2-problem.txt` with the problem descriptions

4. Run solutions:
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
| 04  | gemini-exp-1121 | ✅     | ❌     | 1/3              | Zero-shot, CoT   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%2219u86k9DX47Z7S253S-Z0FW_W1tekHthB%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     | did not solve part 2     |
| 05  | gemini-exp-1121 | ✅     | ✅     | 2/1              | Zero-shot   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221XV71bCF0inECZ7W9AacPwKf0a0tEMPzt%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |      |
| 06  | gemini-exp-1206 | ✅    | ✅     | 2/2              | CoT   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221VBYQR1257m38-T-o6UlypX623S6DgVKd%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |  solved part 1 only after human hint    |
| 07  | gemini-exp-1206 | ✅    | ✅     | 1/1              | CoT   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221F136Re6CpEnMu7sijkvZROw2vziNlINL%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |      |
| 08  | gemini-exp-1206 | ✅    | ✅     | 1/1              | CoT   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221f4gG-LJf3TuRjpVRMvnfIPZZc-S__ToN%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |      |
| 09  | gemini-exp-1206 | ❌    | `-`     | 3/1              | CoT   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%2212_LaEzYEj9S_BGTbINw3Rtkw-0xWhMAJ%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |      |
| 10  | gemini-exp-1206 | ✅    | ✅     | 1/1              | CoT   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221hCDQ3n-za6_L64R9sTD-p_uQvajaj1d7%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)     |      |
| 11  | gemini-exp-1206 | ✅    | ✅     | 1/1              | CoT   | [Chat](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221SQKUXWTJu_MWTXXMD2DQQM-_9tRXKpjg%22%5D,%22action%22:%22open%22,%22userId%22:%22105677632504908789218%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)  1/2   | After hinting that the naive solution will take too long, Gemini found a more efficient solution     |

Legend:
- ✅ Solved
- ❌ Not solved
- `-` Not attempted

## Repository Structure

Each day's challenge is organized in its own directory:
```
dayXX/
├── input.txt         # Challenge input (not included - get from adventofcode.com)
├── part1-problem.txt # Problem description for part 1 (not included - get from adventofcode.com)
├── part2-problem.txt # Problem description for part 2 (not included - get from adventofcode.com)
├── part1.py         # Solution for part 1
└── part2.py         # Solution for part 2
```

Note: The `input.txt` and problem statement files are not included in this repository. You'll need to get these from the [Advent of Code website](https://adventofcode.com/) using your own account, as per the Advent of Code's terms of use.

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