
class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"
