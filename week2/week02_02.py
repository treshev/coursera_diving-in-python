import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper


@to_json
def get_data():
    return {
        'data': 42
    }


@to_json
def test():
    return 324234


if __name__ == "__main__":
    get_data()