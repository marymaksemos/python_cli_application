import json
import sys

def main():
    # handle command line arguments
    if len(sys.argv) < 2:
        print("Invalid command. Use 'new', 'list', 'edit', 'delete', or 'export'.")
        return
    command = sys.argv[1]
    if command == "new":
        add_note(sys.argv[2])
    elif command == "list":
        list_notes()
    elif command == "edit":
        edit_note(int(sys.argv[2]), sys.argv[3])
    elif command == "delete":
        delete_note(int(sys.argv[2]))
    elif command == "export":
        export_notes()
    else:
        print("Invalid command. Use 'new', 'list', 'edit', 'delete', or 'export'.")

def add_note(content):
    # add a new note to the guestbook
    notes = load_notes()
    notes.append(content)
    save_notes(notes)
    print("Note added.")

def list_notes():
    # list all notes in the guestbook
    notes = load_notes()
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note}")

def edit_note(index, content):
    # edit the specified note in the guestbook
    notes = load_notes()
    try:
        notes[index - 1] = content
        save_notes(notes)
        print("Note edited.")
    except IndexError:
        print("Invalid note index.")

def delete_note(index):
    # delete the specified note from the guestbook
    notes = load_notes()
    try:
        del notes[index - 1]
        save_notes(notes)
        print("Note deleted.")
    except IndexError:
        print("Invalid note index.")

def export_notes():
    # export notes in json format
    notes = load_notes()
    json_str = json.dumps(notes)
    print(json_str)

def load_notes():
    # load notes from file
    try:
        with open("guestbook.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_notes(notes):
    # save notes to file
    with open("guestbook.json", "w") as f:
        json.dump(notes, f)

if __name__ == "__main__":
    main()
