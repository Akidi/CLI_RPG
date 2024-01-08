def confirm(question: str, defaultConfirm: bool = True) -> bool:
    confirm = input(f"{question} {"[Yes/no]" if defaultConfirm else "[yes/No]"}").lower()
    if (confirm.startswith("y") or confirm == "" and defaultConfirm):
        return True
    return False