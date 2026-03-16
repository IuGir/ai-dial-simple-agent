from typing import Any

from task.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "search_users"

    @property
    def description(self) -> str:
        return "Search users by name, surname, email, or gender. All parameters are optional; use whichever filters you have."

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Filter by first name"},
                "surname": {"type": "string", "description": "Filter by surname"},
                "email": {"type": "string", "description": "Filter by email"},
                "gender": {"type": "string", "description": "Filter by gender"},
            },
            "required": [],
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        try:
            return self._user_client.search_users(**arguments)
        except Exception as e:
            return f"Error while searching users: {e!s}"
