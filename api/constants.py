from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper

JOURNAL_LIST = {
    '1': midimdgscraper,
    '0': expressmadascraper,
    '2': lefigaroscraper,
    '3': lemondescraper,
}