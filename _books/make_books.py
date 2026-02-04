import os
import requests
import time

# You can now change the status or date for any specific book here
books = [
    {"filename": "1984.md", "title": "1984", "author": "George Orwell", "released": "1949", "isbn": "9780451524935", "olid": "OL18197720M", "cat": "classics fiction dystopian political-fiction", "status": "Finished", "date": "2025-01-01"},
    {"filename": "animal_farm.md", "title": "Animal Farm", "author": "George Orwell", "released": "1945", "isbn": "9780143416319", "olid": "OL25740891M", "cat": "classics fiction dystopian satire allegory", "status": "Finished", "date": "2025-01-01"},
    {"filename": "brave_new_world.md", "title": "Brave New World", "author": "Aldous Huxley", "released": "1932", "isbn": "9780060850524", "olid": "OL24364303M", "cat": "classics fiction dystopian science-fiction", "status": "Interested", "date": "2025-01-01"},
    {"filename": "fahrenheit_451.md", "title": "Fahrenheit 451", "author": "Ray Bradbury", "released": "1953", "isbn": "9781451673319", "olid": "OL26993136M", "cat": "classics fiction dystopian science-fiction", "status": "Interested", "date": "2025-01-01"},
    {"filename": "notes_from_underground.md", "title": "Notes from Underground", "author": "Fyodor Dostoevsky", "released": "1864", "isbn": "9781453600627", "olid": "OL24624419M", "cat": "classics philosophy russian-literature fiction existentialism", "status": "Finished", "date": "2025-01-01"},
    {"filename": "the_brothers_karamazov.md", "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "released": "1880", "isbn": "9780374528379", "olid": "OL24371424M", "cat": "classics philosophy russian-literature fiction", "status": "Finished", "date": "2025-01-01"},
    {"filename": "crime_and_punishment.md", "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "released": "1866", "isbn": "9780679734505", "olid": "OL24371426M", "cat": "classics philosophy russian-literature fiction psychological-fiction", "status": "Finished", "date": "2025-01-01"},
    {"filename": "war_and_peace.md", "title": "War and Peace", "author": "Leo Tolstoy", "released": "1867", "isbn": "9780307266934", "olid": "OL60344376M", "cat": "classics history russian-literature fiction", "status": "Interested", "date": "2025-01-01"},
    {"filename": "the_death_of_ivan_ilyich.md", "title": "The Death of Ivan Ilyich", "author": "Leo Tolstoy", "released": "1886", "isbn": "9780553210354", "olid": "OL267174W", "cat": "classics philosophy russian-literature fiction", "status": "Interested", "date": "2025-01-01"},
    {"filename": "catch-22.md", "title": "Catch-22", "author": "Joseph Heller", "released": "1961", "isbn": "9780684833392", "olid": "OL26993138M", "cat": "classics fiction war-fiction satire", "status": "Paused", "date": "2025-01-01"},
    {"filename": "do_androids_dream_of_electric_sheep.md", "title": "Do Androids Dream of Electric Sheep?", "author": "Philip K. Dick", "released": "1968", "isbn": "9780345404473", "olid": "OL1168153W", "cat": "science-fiction fiction dystopian cyberpunk", "status": "Finished", "date": "2025-01-01"},
    {"filename": "foundation.md", "title": "Foundation", "author": "Isaac Asimov", "released": "1951", "isbn": "9780553293357", "olid": "OL18383124M", "cat": "science-fiction fiction space-opera", "status": "Interested", "date": "2025-01-01"},
    {"filename": "foundation_and_empire.md", "title": "Foundation and Empire", "author": "Isaac Asimov", "released": "1952", "isbn": "9780380397013", "olid": "OL46224W", "cat": "science-fiction fiction space-opera", "status": "Interested", "date": "2025-01-01"},
    {"filename": "second_foundation.md", "title": "Second Foundation", "author": "Isaac Asimov", "released": "1953", "isbn": "9780553293364", "olid": "OL4407696M", "cat": "science-fiction fiction space-opera", "status": "Interested", "date": "2025-01-01"},
    {"filename": "foundations_edge.md", "title": "Foundation's Edge", "author": "Isaac Asimov", "released": "1982", "isbn": "9780553293388", "olid": "OL45833879M", "cat": "science-fiction fiction space-opera", "status": "Interested", "date": "2025-01-01"},
    {"filename": "foundation_and_earth.md", "title": "Foundation and Earth", "author": "Isaac Asimov", "released": "1986", "isbn": "9780553587579", "olid": "OL7439997M", "cat": "science-fiction fiction space-opera", "status": "Interested", "date": "2025-01-01"},
    {"filename": "dune.md", "title": "Dune", "author": "Frank Herbert", "released": "1965", "isbn": "9780441172719", "olid": "OL22597282M", "cat": "science-fiction fiction space-opera fantasy", "status": "Finished", "date": "2025-01-01"},
    {"filename": "dune_messiah.md", "title": "Dune Messiah", "author": "Frank Herbert", "released": "1969", "isbn": "", "olid": "OL18143783M", "cat": "science-fiction fiction space-opera fantasy", "status": "Finished", "date": "2025-01-01"},
    {"filename": "children_of_dune.md", "title": "Children of Dune", "author": "Frank Herbert", "released": "1976", "isbn": "9780425043837", "olid": "OL24935059M", "cat": "science-fiction fiction space-opera fantasy", "status": "Finished", "date": "2025-01-01"},
    {"filename": "room_of_many_colours.md", "title": "Room of Many Colours", "author": "Ruskin Bond", "released": "2008", "isbn": "9780143432371", "olid": "OL31189689M", "cat": "short-stories fiction children-literature", "status": "Finished", "date": "2025-01-01"}
]


def openlibrary_lookup(isbn):
    """Lookup book data from Open Library by ISBN and return a dict or None."""
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
    res = requests.get(url)
    data = res.json()
    key = f"ISBN:{isbn}"
    if key not in data:
        return None
    return data[key]

def find_olid(book_data):
    """
    Open Library edition records are included in `identifiers` or `publishers`.
    If there is an edition key, use it. If not, try cover/other identifiers.
    """
    if "identifiers" in book_data:
        # Sometimes `openlibrary` in identifiers has OLIDs
        olids = book_data["identifiers"].get("openlibrary", [])
        if olids:
            # Return the first OLID found
            return olids[0]
    # Fallback: check if edition key present
    if "key" in book_data and book_data["key"].startswith("/books/"):
        return book_data["key"].split("/")[-1]
    return None

updated = []

for b in books:
    isbn = b.get("isbn")
    if not isbn:
        print(f"⚠ No ISBN for {b['title']}, skipping lookup.")
        updated.append(b.copy())
        continue

    print(f"Looking up ISBN {isbn} for '{b['title']}' ...")
    ol_data = openlibrary_lookup(isbn)

    if not ol_data:
        print(f"❌ No Open Library record found for ISBN {isbn}")
        updated.append(b.copy())
        continue

    # Extract OLID
    olid = find_olid(ol_data)

    if olid:
        b["olid"] = olid
        print(f"✅ Found OLID: {olid}")
    else:
        print(f"⚠ Could not find OLID in Open Library data for ISBN {isbn}")

    # Optional verification
    # Compare title & author
    ol_title = ol_data.get("title")
    ol_authors = [a["name"] for a in ol_data.get("authors", [])]

    if ol_title and b["title"].lower() != ol_title.lower():
        print(f"  ⚠ Title mismatch: local = {b['title']} | OL = {ol_title}")

    if ol_authors and b["author"] not in ol_authors:
        print(f"  ⚠ Author mismatch: local = {b['author']} | OL = {ol_authors}")

    # Update and collect
    updated.append(b.copy())

    # Delay to be polite to API
    time.sleep(1)

# After this, `updated` contains corrected data
# Next: write markdown files

# The template now pulls directly from the book dictionary
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
date: {date}
started: {date}
finished: {date}
released: {released}
stars: 
goodreads_review: 
status: {status}
---
"""

for b in books:
    with open(b["filename"], "w", encoding="utf-8") as f:
        f.write(template.format(**b))
    print(f"Created: {b['filename']}")

print("\nAll done! Each file now uses its own data from the dictionary.")