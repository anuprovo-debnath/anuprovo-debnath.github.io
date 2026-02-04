import os

books = [
    {"filename": "1984.md", "title": "1984", "author": "George Orwell", "released": "1949", "isbn": "9780451524935", "olid": "OL26993132M", "cat": "classics fiction dystopian political-fiction"},
    {"filename": "animal-farm.md", "title": "Animal Farm", "author": "George Orwell", "released": "1945", "isbn": "9780143416319", "olid": "OL26993134M", "cat": "classics fiction dystopian satire allegory"},
    {"filename": "brave-new-world.md", "title": "Brave New World", "author": "Aldous Huxley", "released": "1932", "isbn": "9780060850524", "olid": "OL24364303M", "cat": "classics fiction dystopian science-fiction"},
    {"filename": "fahrenheit-451.md", "title": "Fahrenheit 451", "author": "Ray Bradbury", "released": "1953", "isbn": "9781451673319", "olid": "OL26993136M", "cat": "classics fiction dystopian science-fiction"},
    {"filename": "notes-from-underground.md", "title": "Notes from Underground", "author": "Fyodor Dostoevsky", "released": "1864", "isbn": "9780679734512", "olid": "OL24624419M", "cat": "classics philosophy russian-literature fiction existentialism"},
    {"filename": "the-brothers-karamazov.md", "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "released": "1880", "isbn": "9780374528379", "olid": "OL24371424M", "cat": "classics philosophy russian-literature fiction"},
    {"filename": "crime-and-punishment.md", "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "released": "1866", "isbn": "9780679734505", "olid": "OL24371426M", "cat": "classics philosophy russian-literature fiction psychological-fiction"},
    {"filename": "war-and-peace.md", "title": "War and Peace", "author": "Leo Tolstoy", "released": "1867", "isbn": "9780307266934", "olid": "OL60344376M", "cat": "classics history russian-literature fiction"},
    {"filename": "the-death-of-ivan-ilyich.md", "title": "The Death of Ivan Ilyich", "author": "Leo Tolstoy", "released": "1886", "isbn": "9780553210354", "olid": "OL267174W", "cat": "classics philosophy russian-literature fiction"},
    {"filename": "catch-22.md", "title": "Catch-22", "author": "Joseph Heller", "released": "1961", "isbn": "9780684833392", "olid": "OL26993138M", "cat": "classics fiction war-fiction satire"},
    {"filename": "do-androids-dream-of-electric-sheep.md", "title": "Do Androids Dream of Electric Sheep?", "author": "Philip K. Dick", "released": "1968", "isbn": "9780345404473", "olid": "OL1168153W", "cat": "science-fiction fiction dystopian cyberpunk"},
    {"filename": "foundation.md", "title": "Foundation", "author": "Isaac Asimov", "released": "1951", "isbn": "9780553293357", "olid": "OL18383124M", "cat": "science-fiction fiction space-opera"},
    {"filename": "foundation-and-empire.md", "title": "Foundation and Empire", "author": "Isaac Asimov", "released": "1952", "isbn": "9780553293340", "olid": "OL46390W", "cat": "science-fiction fiction space-opera"},
    {"filename": "second-foundation.md", "title": "Second Foundation", "author": "Isaac Asimov", "released": "1953", "isbn": "9780553293364", "olid": "OL4407696M", "cat": "science-fiction fiction space-opera"},
    {"filename": "foundations-edge.md", "title": "Foundation's Edge", "author": "Isaac Asimov", "released": "1982", "isbn": "9780553293388", "olid": "OL45833879M", "cat": "science-fiction fiction space-opera"},
    {"filename": "foundation-and-earth.md", "title": "Foundation and Earth", "author": "Isaac Asimov", "released": "1986", "isbn": "9780553587579", "olid": "OL7439997M", "cat": "science-fiction fiction space-opera"},
    {"filename": "dune.md", "title": "Dune", "author": "Frank Herbert", "released": "1965", "isbn": "9780441172719", "olid": "OL22597282M", "cat": "science-fiction fiction space-opera fantasy"},
    {"filename": "dune-messiah.md", "title": "Dune Messiah", "author": "Frank Herbert", "released": "1969", "isbn": "9780441013593", "olid": "OL7500957M", "cat": "science-fiction fiction space-opera fantasy"},
    {"filename": "children-of-dune.md", "title": "Children of Dune", "author": "Frank Herbert", "released": "1976", "isbn": "9780441104024", "olid": "OL39443998M", "cat": "science-fiction fiction space-opera fantasy"},
    {"filename": "room-of-many-colours.md", "title": "Room of Many Colours", "author": "Ruskin Bond", "released": "2008", "isbn": "9788184754636", "olid": "OL31189689M", "cat": "short-stories fiction children-literature"}
]

template = """---
layout: book-review
title: {title}
author: {author}
cover: 
olid: {olid}
isbn: {isbn}
categories: {cat}
tags: 
buy_link: 
date: 
started: 
finished: 
released: {released}
stars: 
goodreads_review: 
status: 
---"""

for b in books:
    with open(b["filename"], "w", encoding="utf-8") as f:
        f.write(template.format(**b))
    print(f"Created: {b['filename']}")

print("\nAll done!")