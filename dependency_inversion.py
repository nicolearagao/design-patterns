"""
Dependency inversion: objects do not create each other anymore, two modules shouldn't be dependent
on each other on a tight way. + cohesion -coupling
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.
"""
import os

class ApiClient:

    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")  # <-- dependency
        self.timeout = int(os.getenv("TIMEOUT"))  # <-- dependency


class Service:

    def __init__(self) -> None:
        self.api_client = ApiClient()  # <-- dependency


def main() -> None:
    service = Service()  # <-- dependency
    ...


if __name__ == "__main__":
    main()

class ApiClient:

    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key
        self.timeout = timeout
    
    # ApiClient is decoupled from knowing where the options come from.
    # You can read a key and a timeout from a configuration file or even get them from a database.


class Service:

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client
    
    # Service is decoupled from the ApiClient. It does not create it anymore. You can provide other compatible object.


def main(service: Service) -> None:  # <-- dependency is injected
    ...
    # Function main() is decoupled from Service. It receives it as an argument.


if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_key=os.getenv("API_KEY"),
                timeout=int(os.getenv("TIMEOUT")),
            ),
        ),
    )
    # assemble and inject the objects like this increases complexity. Solutions in Python ?