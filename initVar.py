from dataclasses import dataclass, InitVar

@dataclass
class C:
    i: int
    j: int | None = None
    database: InitVar[str | None] = None

    def __post_init_(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database={"j":"val"})