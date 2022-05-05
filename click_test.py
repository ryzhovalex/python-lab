"""Is it possible to propagate input args from argparse to click decorated function?
"""
import click
import argparse


@click.command()
@click.argument("name")
def hello(name):
    print(f"Hello, {name}.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode")
    namespace = parser.parse_args()
    if namespace.mode == "call":
        hello()  # type: ignore


if __name__ == "__main__":
    main()