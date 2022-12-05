from typing import List
from requests.models import Response

data: str
lines: List[str]
numbers: List[int]

def get_data(
    session: str = ...,
    day: int = ...,
    year: int = ...,
    block: bool = ...,
) -> str: ...
def submit(
    answer: int | str,
    part: str = ...,
    day: int = ...,
    year: int = ...,
    session: str = ...,
    reopen: bool = ...,
    quiet: bool = ...,
) -> Response: ...
