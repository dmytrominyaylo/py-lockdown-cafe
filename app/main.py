from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_needed = 0
    all_vaccinated = True
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            all_vaccinated = False
        except NotWearingMaskError:
            masks_needed += 1
    if not all_vaccinated:
        return "All friends should be vaccinated"
    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"
    return f"Friends can go to {cafe.name}"
