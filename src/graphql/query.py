import strawberry
from .reolvers import certificates_resolver




@strawberry.type
class Query:
    certificate:strawberry.field(resolver=certificates_resolver)


