"""Custom slipbox CLI command for generating Anki flashcards."""

from pathlib import Path

import genanki
from slipbox.app import require_dot_slipbox
from slipbox.cli import GenbuWithHelp
from slipbox.slipbox import Slipbox


def generate_flashcards(output: str) -> None:
    """Generate anki flash cards from notes."""
    model = genanki.Model(
        1635490798,  # model ID
        "Note",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card",
                "qfmt": "<h1>{{Question}}</h1>",
                "afmt": "{{Answer}}",
            },
        ],
    )
    deck = genanki.Deck(1843743983,  # deck ID
                        "Slipbox")
    dot = require_dot_slipbox()
    with Slipbox(dot) as slipbox:
        sql = "SELECT title, html FROM Notes"
        for title, html in slipbox.conn.execute(sql):
            note = genanki.Note(model=model,
                                fields=[
                                    title,
                                    html.replace(' style="display:none"', "")
                                ])
            deck.add_note(note)
    genanki.Package(deck).write_to_file(Path(output))


exports = [GenbuWithHelp(generate_flashcards, name="flashcards")]
