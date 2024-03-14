"""
Think of it as a specialized department in a company that only focuses on producing certain products.
This department takes care of all the details of manufacturing, and the rest of the company simply requests the product 
when needed without worrying about how it's made.
Mechanics:
    - A client depends on a concrete implementation of an interface. It requests the implementation froom a creator component using some sort of identifier.
Solves: Easily add new types of products without disturbing the existing client code.

Common usages:
    - SQLAlchemy uses factories to create database session objects. SQLAlchemy's sessionmaker()
"""

import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

class SongSerializer:
    # client component of the pattern
    # interface defined is product, a function that takes a song and returns a string representation
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)


# Provide a separate component with the responsability to decide which concrete 
# implementation should be used, format in the case of this class
# creator component
def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)

# Functions below are concreate implementations of the product
def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')
