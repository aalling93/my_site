MAIN_TEXT_COLOR = "black"
EXTRA_TEXT_COLOR = "gray"
HEADLINES_COLOR = "#030F4F"
HEADLINES_COLOR = ""
DIVIDER_MARGIN_BEFORE = 10
DIVIDER_MARGIN_AFTER = 10
DIVIDER_HEIGHT = 0.1
DIVIDER_SPACING = 10


def DIVIDER(
    colour: str = EXTRA_TEXT_COLOR,
    margin_before: int = DIVIDER_MARGIN_BEFORE,
    margin_after: int = DIVIDER_MARGIN_AFTER,
    height: int = DIVIDER_HEIGHT,
    dot_spacing: int = DIVIDER_SPACING,
):
    # return f'<hr style="border: {spacing}px solid {colour}; width: 100%; margin-top: {margin_before}px; margin-bottom: {margin_after}px;">' border-spacing: 0px {dot_spacing}px;
    return f'<hr style="border: {height}px dotted {colour}; width: 100%; margin-top: {margin_before}px; margin-bottom: {margin_after}px; border-spacing: {dot_spacing}px;">'
