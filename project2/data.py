from testy import internal_runtests
from pathlib import Path
import dimacs
import argparse
import fnmatch


def problem_from_file(dir_path, name):
    base_path = Path(dir_path) / name
    graph_file = base_path.with_suffix(".graph")

    V, L = dimacs.loadWeightedGraph(graph_file)
    edges = [(u, v) for u, v, _ in L]
    entrance = 1
    solution = dimacs.readSolution(graph_file) == "True"

    path_file = base_path.with_suffix(".path")
    path = path_file.read_text().rstrip()

    return dict(name=name, arg=(V, entrance, edges, path), hint=solution)


largish = [
    12,
    1,
    [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (3, 6),
        (3, 7),
        (7, 8),
        (3, 9),
        (2, 10),
        (1, 11),
        (11, 12),
    ],
]

larger = [
    26,
    1,
    [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (5, 7),
        (5, 8),
        (4, 9),
        (9, 10),
        (9, 11),
        (3, 12),
        (12, 13),
        (12, 14),
        (12, 15),
        (2, 16),
        (16, 17),
        (16, 18),
        (18, 19),
        (2, 20),
        (20, 21),
        (20, 22),
        (22, 23),
        (23, 24),
        (20, 25),
        (20, 26),
    ],
]


problems = [
    {"name": "small-1", "arg": [3, 1, [(1, 2), (2, 3)], "+"], "hint": True},
    {
        "name": "small-2",
        "arg": [6, 1, [(1, 2), (2, 3), (2, 4), (1, 5), (5, 6)], "+ ^ + ^ +"],
        "hint": False,
    },
    {
        "name": "small-3",
        "arg": [
            8,
            1,
            [(1, 2), (2, 3), (3, 4), (3, 5), (1, 6), (6, 7), (6, 8)],
            "+ ^ 1 ^ + ^ 1 ^ + ^ 3",
        ],
        "hint": True,
    },
    {
        "name": "small-4",
        "arg": [6, 1, [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)], "+"],
        "hint": False,
    },
    {
        "name": "small-5",
        "arg": [
            9,
            1,
            [(1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (2, 7), (7, 8), (8, 9)],
            "+ + ^ 1 ^ ^ + ^ +",
        ],
        "hint": True,
    },
    {
        "name": "small-6",
        "arg": [
            8,
            1,
            [(1, 2), (2, 3), (3, 4), (3, 5), (2, 6), (2, 7), (1, 8)],
            "+ ^ + + + ^ +",
        ],
        "hint": False,
    },
    {
        "name": "small-7a",
        "arg": largish + ["+ ^ + ^ +"],
        "hint": True,
    },
    {
        "name": "small-7b",
        "arg": largish + ["+ + ^ ^ + + ^ ^ +"],
        "hint": True,
    },
    {
        "name": "small-7c",
        "arg": largish + ["+ + ^ ^ + + ^ ^ + +"],
        "hint": True,
    },
    {
        "name": "small-7d",
        "arg": largish + ["+ + +"],
        "hint": True,
    },
    {
        "name": "small-7e",
        "arg": largish + ["+ + + +"],
        "hint": True,
    },
    {
        "name": "small-7f",
        "arg": largish + ["+ + + + +"],
        "hint": False,
    },
    {
        "name": "small-7g",
        "arg": largish + ["+ ^ + + ^ + ^ ^ +"],
        "hint": False,
    },
    {
        "name": "small-7h",
        "arg": largish + ["+ + + + ^ ^ + + ^ ^ + +"],
        "hint": False,
    },
    {
        "name": "small-7i",
        "arg": largish + ["+ + + ^ + ^ +"],
        "hint": True,
    },
    {
        "name": "larger-8a",
        "arg": larger + ["+ + ^ ^ + + ^ ^ + +"],
        "hint": True,
    },
    {
        "name": "larger-8b",
        "arg": larger + ["+ + + ^ + + ^ ^ 1 + + ^ + ^ 2 ^ ^ ^ ^ 1 2 + ^ 1 + +"],
        "hint": True,
    },
    {
        "name": "larger-8c",
        "arg": larger + ["+ + + ^ ^ + + ^ ^ + +"],
        "hint": False,
    },
    {
        "name": "larger-8d",
        "arg": larger + ["+ + + ^ ^ + ^ + +"],
        "hint": True,
    },
    {
        "name": "larger-8e",
        "arg": larger + ["+ ^ + ^ + ^ + ^ + ^ +"],
        "hint": False,
    },
]


problem_files = [
    "full-binary-small",
    "full-binary-med",
    "full-3nary-small",
    "full-3nary-med",
    "full-binary-invalid-small",
    "full-binary-invalid2-small",
    "full-wide-small",
    "full-wide-med",
    "full-wide-invalid-small",
    "fully-random-small",
    "fully-random-med",
    "fully-random2-med",
    "fully-random-invalid-small",
    "fully-random-invalid2-small",
    "fully-random-invalid-med",
    "fully-random-invalid2-med",
    "maze-2d-small",
    "maze-2d-invalid-small",
    "maze-2d-med",
    "maze-2d-2-med",
    "maze-2d-invalid-med",
    "maze-clique-small",
    "maze-3d-med",
    "maze-3d-2-med",
    "maze-3d-invalid-med",
    "close1",
    "close1-invalid",
    "star-med",
    "star-large",
    "star-large-2",
    "mix-large",
    "mix-variety-large",
    "mix-large-invalid",
]

problems += [problem_from_file("problems", name) for name in problem_files]


def print_arg(N, entrance, corridors, path):
    print(f"{N} komnat, {len(corridors)} korytarzy")


def print_hint(hint):
    print(f"Wynik: {hint}")


def print_sol(sol):
    print(f"Uzyskany wynik: {sol}")


def check(N, entrance, corridors, path, hint, sol):
    if hint == sol:
        print("Test zaliczony")
        return True
    else:
        print("NIEZALICZONY!")
        return False


def runtests(f):
    internal_runtests(print_arg, print_hint, print_sol, check, problems, f)


def runtests_with_args(f):
    parser = argparse.ArgumentParser()
    parser.add_argument("--select", help="which tests to run", nargs="+")
    parser.add_argument("--pattern", help="which tests to run")
    parser.add_argument("--exclude", help="which tests not to run")
    args = parser.parse_args()

    problem_list = problems

    if args.select:
        problem_list = [p for p in problems if p["name"] in args.select]

    if args.pattern:
        problem_list = [p for p in problems if fnmatch.fnmatch(p["name"], args.pattern)]

    if args.exclude:
        problem_list = [
            p for p in problems if not fnmatch.fnmatch(p["name"], args.exclude)
        ]

    internal_runtests(print_arg, print_hint, print_sol, check, problem_list, f)
