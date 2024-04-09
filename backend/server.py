"""
this proof of concept web service exposes a single endpoint for listing, and optionally filtering, Todos.
the product team has decided they want to move forward with a UX feature that this functionality enables,
so it's time to productionalize this POC.

the developer that wrote the POC left some notes on things that need to be done, so please review those
and do any refactoring/implementing necessary to address them. please feel free to propose any additional
enhancements that you think may improve the current solution.

once you're happy with your changes, and if you have time, please Dockerize the application for deployment.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING

import requests
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

if TYPE_CHECKING:
    from starlette.requests import Request


@dataclass
class Todo:
    id: int
    userId: int
    title: str
    completed: bool


class TodoServiceHTTP:
    async def list_todos(self, request: Request) -> Response:
        """
        Usage:
            - `curl "localhost:5000/todos"`
            - `curl "localhost:5000/todos?completed=true"`
            - `curl "localhost:5000/todos?completed=false"`

        TODO:
            1) this implementation is tightly coupled to getting todos from jsonplaceholder.typicode.com,
                but that may change in the future and it makes it hard to test. make an abstract TodoService
                that can be injected into and used in this http service, and write concrete implementations
                for TodoServiceTypicode and TodoServiceMock.
            2) so we don't duplicate the filtering logic, extract that to a helper method that all the
                implementations of TodoService can share.
            3) this hasn't been tested, there may be bugs, so write a test that proves the filtering works as intended.
        """
        response = requests.get("https://jsonplaceholder.typicode.com/todos")

        response.raise_for_status()

        todos: list[Todo] = [Todo(**record) for record in response.json()]

        completed = request.query_params.get("completed")

        if completed is not None:
            if completed == "true":
                todos = [todo for todo in todos if todo.completed is False]
            elif completed == "false":
                todos = [todo for todo in todos if todo.completed is True]
            else:
                return Response(
                    f"expected 'true' | 'false' for query param 'completed', got {completed}",
                    status_code=400,
                )

        return JSONResponse(content=[asdict(todo) for todo in todos], status_code=200)


def main() -> None:
    todo_service_http = TodoServiceHTTP()

    app = Starlette(
        routes=(
            Route(
                path="/todos", endpoint=todo_service_http.list_todos, methods=["GET"]
            ),
        )
    )

    return uvicorn.run(app, port=5000, log_level="info")


if __name__ == "__main__":
    main()
