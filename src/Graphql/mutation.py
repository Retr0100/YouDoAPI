import strawberry

from schema import TodoInput, TodoType, UserInput, UserType
from service.dailyTodo import TodoService
from service.user import UserService

@strawberry.type
class Mutation:
    """The mutations available in the GraphQL API for usering purposes.

    Returns:
        _type_: _description_
    """

    @strawberry.mutation
    async def create_todo(self,todo_data:TodoInput) -> TodoType:
        """Create a new todo case with given data.

        Args:
            todo_data (DailyTodoInput): _description_

        Returns:
            userType: _description_
        """
        return await TodoService.create(todo_data=todo_data)

    @strawberry.mutation
    async def delete_todo(self,id:int) -> int:
        """Delete an existing todo case by its id.

        Args:
            id (int): _description_

        Returns:
            str: _description_
        """
        return await TodoService.delete(id)

    @strawberry.mutation
    async def update_todo(self,id:int,todo_data:TodoInput) -> str:
        """Update an existing todo case's information.

        Args:
            id (int): _description_
            todo_data (userInput): _description_

        Returns:
            str: _description_
        """
        return await TodoService.update(id,todo_data)

    @strawberry.mutation
    async def create_user(self,user_data:UserInput) -> UserType:
        """Create a new user case with given data.

        Args:
            user_data (DailyTodoInput): _description_

        Returns:
            userType: _description_
        """
        return await UserService.create(user_data=user_data)

    @strawberry.mutation
    async def delete_user(self,id:int) -> int:
        """Delete an existing user case by its id.

        Args:
            id (int): _description_

        Returns:
            str: _description_
        """
        return await UserService.delete(id)

    @strawberry.mutation
    async def update_user(self,id:int,user_data:UserInput) -> str:
        """Update an existing user case's information.

        Args:
            id (int): _description_
            user_data (userInput): _description_

        Returns:
            str: _description_
        """
        return await UserService.update(id,user_data)

