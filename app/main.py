from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError
from typing import Any


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = sum(1 for friend in friends
                       if try_visit_cafe(friend, cafe) == "mask")
    all_vaccinated = all(try_visit_cafe(friend, cafe) != "vaccine"
                         for friend in friends)
    if not all_vaccinated:
        return "All friends should be vaccinated"
    if masks_needed:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"


def try_visit_cafe(friend: Any, cafe: Any) -> Any:
    try:
        cafe.visit_cafe(friend)
        return None
    except VaccineError:
        return "vaccine"
    except NotWearingMaskError:
        return "mask"
