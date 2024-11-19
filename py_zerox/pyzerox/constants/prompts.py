class Prompts:
    """Class for storing prompts for the Nedrox system."""

    DEFAULT_SYSTEM_PROMPT = """
    Convert the following PDF page to markdown.
    Return only the markdown with no explanation text.
    Do not exclude any content from the page.
    """