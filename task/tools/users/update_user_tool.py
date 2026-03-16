from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserUpdate


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return "update_user"

    @property
    def description(self) -> str:
        return "Update an existing user by ID. Provide id and new_info with the fields to change (all optional in new_info)."

    @property
    def input_schema(self) -> dict[str, Any]:
        new_info_schema = UserUpdate.model_json_schema()
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "User ID that should be updated.",
                },
                "new_info": {
                    "type": new_info_schema.get("type", "object"),
                    "properties": new_info_schema.get("properties", {}),
                    "description": "Fields to update (all optional).",
                },
            },
            "required": ["id"],
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        try:
            user_id = int(arguments["id"])
            new_info = arguments.get("new_info") or {}
            user_update = UserUpdate.model_validate(new_info)
            return self._user_client.update_user(user_id, user_update)
        except Exception as e:
            return f"Error while updating user: {e!s}"
