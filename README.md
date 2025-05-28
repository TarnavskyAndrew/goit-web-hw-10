# My Python Projects

Welcome to my repository with Python projects!  
Here I learn, practice and improve my coding skills.

---

<details>
<summary>Bot Assistant — Personal CLI Helper</summary>


*A Python console bot for contact management, with backup support, data validation and multilingual support.*


## Possibilities:

- Add/delete/edit contacts
- Search by name and phone number
- Display all contacts
- Backup
- Command line support
- Number validation
- Multilingual interface (UA/EN)
- Extensible architecture


### 🛠️ Functional Overview

Bot Assistant is a command-line personal assistant that allows you to manage your contact book efficiently. 
Here's what it can do:

| Command                            | Description                                                  |
|------------------------------------|--------------------------------------------------------------|
| `hello`                            | Greet the assistant and get a prompt for help                |
| `add <name> <phone>`               | Add a new contact with a phone number                        |
| `change <name> <new_phone>`        | Change an existing contact's phone number                    |
| `phone <name>`                     | Show the phone number(s) of a contact                        |
| `all`                              | Display all contacts in the address book                     |
| `add-birthday <name> <YYYY-MM-DD>` | Add a birthday for a contact                                 |
| `show-birthday <name>`             | Show the birthday of a contact                               |
| `birthdays`                        | Show upcoming birthdays within the next 7 days               |
| `delete <name>`                    | Delete a contact                                             |
| `help`                             | Display available commands and usage instructions            |
| `lang`                             | Change the interface language (UA / EN)                      |
| `restore`                          | Restore the contact book from the last backup                |
| `exit` or `close`                  | Exit the assistant and save all data                         |
---

## Project structure:

```python
root_folder/
│
├── pyproject.toml
├── poetry.lock
├── README.md
├── src/
│ └── bot_assistant/
│ ├── main.py
│ ├── models/
│ ├── views/
│ ├── handlers/
│ ├── utils/
│ └── data/
├── dev_tools/
│ └── check.py
├── tests/
└── .vscode/
```


## Project status:

The project is in progress and will be improved.


### Run the bot:

`pip install poetry`
`poetry install`
`poetry shell`
`poetry run run-bot`

https://github.com/TarnavskyAndrew/goit-web-hw-10


</details>