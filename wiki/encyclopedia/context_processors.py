from . import util

entries = util.list_entries()

def entries_processor(request):
    return {
        "entries": entries
    }