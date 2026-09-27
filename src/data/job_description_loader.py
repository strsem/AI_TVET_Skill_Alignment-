import json


def load_job_descriptions(
    file_path: str
) -> list[dict]:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data