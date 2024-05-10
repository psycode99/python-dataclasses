from dataclasses import dataclass, InitVar

@dataclass
class C:
    i: int
    j: int | None = None
    database: InitVar[dict | None] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.get('j')

c = C(10, database={"j":"val"})
print(c)