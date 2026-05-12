# Day 5 — Design Patterns
### Mythical Creature Stable 🐉

> **Starting point:** your complete Day 3 solution — `Creature` ABC, `Dragon`, `Phoenix`, `Unicorn`, `MissionRecord`, `Stable`, `StableIterator`, `MissionService`, `ScrollArchive`, `mission_lock`, `MissionLogger` Protocol.

---

## Overview

You will retrofit eight classic design patterns into the Mythical Creature Stable — one at a time, in order. Each section explains what the pattern is, why it matters, and exactly where to apply it in the code you already have.

Work through them in order. Each one prepares the ground for the next. By the end, your codebase will be structured as a realistic basic service layer.

**Rules:**
- Each pattern goes in its own clearly delimited section — do not mix them.
- Do not modify the Day 3 `Creature` hierarchy or `MissionRecord` dataclass. Only add around them.
- All new classes must have type hints on every method signature.
- Every class and public method must have a one-line docstring.
- Run `python mythical_stable_day5.py` after each pattern and confirm no regressions.

---

## Pattern Map

| # | Category | Pattern | Applied to |
|---|----------|---------|------------|
| 1 | Creational | **Singleton** | `Stable` — one instance only |
| 2 | Creational | **Factory Method** | `CreatureFactory` — centralise construction |
| 3 | Structural | **Repository** | `MissionRepository` — isolate persistence |
| 4 | Structural | **Facade** | `StableFacade` — single entry point |
| 5 | Structural | **Decorator** | `@log_call`, `@timed` — cross-cutting concerns |
| 6 | Behavioral | **Strategy** | `SortStrategy` — pluggable sort algorithms |
| 7 | Behavioral | **Observer** | `EventBus` — decoupled event listeners |
| 8 | Behavioral | **Command** | `CommandHistory` — reversible dispatch actions |

---

## Interview prep

For **every** pattern you implement, be ready to answer these without looking at your code:
- What problem does this pattern solve?
- What would the code look like without it? What goes wrong?
- What are the trade-offs? When would you NOT use it?

---

---

## 1 — Singleton
`CREATIONAL`

### What is it?

The Singleton pattern ensures that a class has exactly **one instance** throughout the lifetime of the program, and provides a global access point to that instance. In Python it is typically implemented by overriding `__new__` and storing the single instance as a class attribute.

### Why does it matter?

Some resources must be shared and must not be duplicated: a database connection pool, a configuration loader, an audit log handle. Creating two instances of such a resource causes hard-to-debug inconsistencies. Singleton makes that impossibility explicit and enforced.

### Where to implement it in the Stable

The stable has one physical location. There should be exactly **one `Stable` instance** shared across the whole application. Right now nothing stops a developer from accidentally instantiating a second `Stable` and registering creatures into it — those creatures would be invisible to `MissionService`.

- Make `Stable` a Singleton using `__new__` so that `Stable()` always returns the same object.
- Add a `reset()` classmethod that clears the instance — essential for test isolation so each test starts clean.
- Verify: call `Stable()` twice and assert both variables are the same object with `is`.

### Your tasks

1. Override `__new__` on `Stable` to store and return a single `_instance` class attribute.
2. Add `Stable.reset()` to destroy the singleton — use it in test `setUp()` so tests don't bleed into each other.
3. Print `id(stable_a)` and `id(stable_b)` after two `Stable()` calls and confirm they are identical.
4. **Discuss:** when would you NOT use a Singleton? *(hint: thread safety, testability, hidden coupling)*

### Implementation hints

```python
class Stable:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None
```

---

## 2 — Factory Method
`CREATIONAL`

### What is it?

The Factory Method pattern **centralises object creation** behind a single interface. Instead of calling `Dragon(...)` or `Phoenix(...)` directly, callers pass a type string (or enum) to a factory, which handles construction. Adding a new creature type requires touching only the factory — nothing else changes.

### Why does it matter?

Scattered constructor calls are a maintenance hazard. If the `Dragon` signature changes, every call site must be updated. A factory creates objects in one place, validates inputs in one place, and can be extended without modifying client code — a direct application of the **Open/Closed Principle**.

### Where to implement it in the Stable

The stable currently receives fully-built `Creature` objects. In a real system, creature data arrives from an external source (a database row, a JSON payload, a CSV import). A `CreatureFactory` that accepts a type string and a dictionary of attributes is the clean solution.

- `CreatureFactory.create('Dragon', name='Frostbite', origin='Nordic Realms', power_level=95, element='ice')`
- `CreatureFactory.create('Phoenix', name='Ember', origin='Ashlands', power_level=80)`
- Raise `ValueError` for unknown species so bad data fails fast at the factory boundary.

### Your tasks

1. Create a `CreatureFactory` class with a `static create(species, **kwargs)` method.
2. Support `'Dragon'`, `'Phoenix'`, and `'Unicorn'` — map each string to its constructor.
3. Raise a clear `ValueError` for unrecognised species.
4. Add a `from_dict(data: dict)` convenience method that extracts `'species'` from the dict and delegates to `create()`.
5. Replace all direct constructor calls in your demo script with `CreatureFactory.create()`.

### Implementation hints

```python
class CreatureFactory:
    _registry = {'Dragon': Dragon, 'Phoenix': Phoenix, 'Unicorn': Unicorn}

    @staticmethod
    def create(species: str, **kwargs) -> Creature:
        cls = CreatureFactory._registry.get(species)
        if cls is None:
            raise ValueError(f'Unknown species: {species!r}')
        return cls(**kwargs)

    @staticmethod
    def from_dict(data: dict) -> Creature:
        species = data.pop('species')
        return CreatureFactory.create(species, **data)
```

---

## 3 — Repository
`STRUCTURAL`

### What is it?

The Repository pattern **isolates all data-access logic** behind an abstract interface. Business logic talks only to the interface; whether data is stored in memory, in a file, or in a PostgreSQL database is an implementation detail that the service layer never sees.

### Why does it matter?

Without a repository, storage logic leaks into service classes. That makes tests slow (they hit a real database), makes the service hard to read (business logic tangled with persistence), and makes swapping storage backends a nightmare. A repository creates a clean seam between the *what* (business rules) and the *how* (storage mechanics).

### Where to implement it in the Stable

`MissionRecord` objects are currently stored in a plain `dict` inside `MissionService`. That couples the service to an in-memory store. Introduce a `MissionRepository` abstraction so `MissionService` never touches storage directly.

- `MissionRepository` (Protocol): `save(record)`, `find_by_creature(name)`, `find_all()`, `delete(name)`.
- `InMemoryMissionRepository`: stores records in a `dict` — used in tests and the demo.
- `FileMissionRepository` *(stretch)*: serialises records to a JSON file on each write.
- `MissionService` receives a `MissionRepository` via injection — it never creates one internally.

### Your tasks

1. Define a `MissionRepository` Protocol with `save()`, `find_by_creature()`, `find_all()`, `delete()`.
2. Implement `InMemoryMissionRepository` satisfying that interface.
3. Update `MissionService.__init__` to accept a `MissionRepository` and remove its internal `dict`.
4. Verify: swap `InMemoryMissionRepository` for a `FileMissionRepository` without changing `MissionService`.
5. **Bonus:** implement `find_overdue()` that returns all records where `is_overdue` is `True`.

### Implementation hints

```python
class MissionRepository(Protocol):
    def save(self, record: MissionRecord) -> None: ...
    def find_by_creature(self, name: str) -> MissionRecord | None: ...
    def find_all(self) -> list[MissionRecord]: ...
    def delete(self, creature_name: str) -> None: ...

class InMemoryMissionRepository:
    """In-memory implementation — used for tests and prototyping."""

    def __init__(self) -> None:
        self._store: dict[str, MissionRecord] = {}

    def save(self, record: MissionRecord) -> None:
        self._store[record.creature_name] = record

    def find_by_creature(self, name: str) -> MissionRecord | None:
        return self._store.get(name)

    def find_all(self) -> list[MissionRecord]:
        return list(self._store.values())

    def delete(self, creature_name: str) -> None:
        self._store.pop(creature_name, None)
```

---

## 4 — Facade
`STRUCTURAL`

### What is it?

The Facade pattern provides a **single, simplified entry point** to a subsystem made up of multiple collaborating objects. Clients call the facade; they never need to know that a `Stable`, a `MissionRepository`, a `MissionService`, and a `MissionLogger` exist and must be wired together.

### Why does it matter?

As a system grows, wiring collaborators together becomes verbose and error-prone. Every caller must know the construction order, which dependencies go where, and which object exposes which method. A facade moves all of that wiring to one place, leaving callers with a clean, intention-revealing API.

### Where to implement it in the Stable

Your demo script already manually constructs a `Stable`, creatures, a logger, and a `MissionService` before it can do anything. A `StableFacade` hides that complexity — a caller just imports `StableFacade` and calls `dispatch()`, `recall()`, and `roster()`.

- `StableFacade.__init__` wires up: `Stable` (singleton), `InMemoryMissionRepository`, `ConsoleMissionLogger`, `MissionService`.
- `StableFacade.register(species, **kwargs)` — delegates to `CreatureFactory` then `Stable.add()`.
- `StableFacade.dispatch(name, destination, days)` — delegates to `MissionService.dispatch()`.
- `StableFacade.recall(name)` — delegates to `MissionService.recall()`.
- `StableFacade.roster()` — returns a formatted summary of available creatures and active missions.

### Your tasks

1. Create `StableFacade`. Its `__init__` builds and wires all internal collaborators.
2. Implement `register()`, `dispatch()`, `recall()`, and `roster()` as thin delegation methods.
3. Rewrite your entire demo block using only the facade — it should fit in ~10 lines.
4. Confirm that no caller outside `StableFacade` ever imports `MissionService`, `Stable`, or any logger directly.

### Implementation hints

```python
class StableFacade:
    """Single entry point to the stable subsystem."""

    def __init__(self, logger: MissionLogger | None = None) -> None:
        self._stable  = Stable()
        self._repo    = InMemoryMissionRepository()
        self._logger  = logger or ConsoleMissionLogger()
        self._service = MissionService(self._stable, self._repo, self._logger)

    def register(self, species: str, **kwargs) -> None:
        """Create and register a creature via the factory."""
        self._stable.add(CreatureFactory.create(species, **kwargs))

    def dispatch(self, name: str, destination: str, days: int, notes: str = "") -> MissionRecord:
        """Send a creature on a mission."""
        return self._service.dispatch(name, destination, days, notes)
```

---

## 5 — Decorator
`STRUCTURAL`

### What is it?

The Decorator pattern **attaches additional responsibilities** to a function or object without modifying it. In Python, the `@` syntax is a first-class implementation of this pattern: a decorator is a callable that wraps another callable and returns the wrapper.

### Why does it matter?

Cross-cutting concerns — logging, timing, access control, retrying — repeat across many functions. Duplicating that logic inside every function violates DRY and makes it hard to change later. Decorators extract the concern once and apply it at the call site declaratively.

### Where to implement it in the Stable

`MissionService.dispatch()` and `recall()` are high-value operations. Adding `@log_call` and `@timed` to them gives observability without touching the business logic inside those methods.

- `@log_call`: prints the function name and arguments before the call, and the return value after.
- `@timed`: measures execution time with `time.perf_counter()` and prints elapsed milliseconds.
- `@functools.wraps` **must** be applied inside every decorator to preserve `__name__` and `__doc__` — without it, introspection breaks.
- Stack both decorators on `dispatch()` and observe the output order.

### Your tasks

1. Write a `@log_call` decorator using `functools.wraps`. It should print the decorated function's name, its `*args` and `**kwargs`, and its return value.
2. Write a `@timed` decorator using `functools.wraps` and `time.perf_counter()`.
3. Apply both to `MissionService.dispatch()` and `MissionService.recall()`.
4. Print `dispatch.__name__` and `dispatch.__doc__` and confirm they reflect the original method, not the wrapper — this is what `@functools.wraps` guarantees.
5. **Discuss:** what is the difference between the Decorator *design pattern* and a Python *decorator*? *(They share a name but are not identical concepts.)*

### Implementation hints

```python
import functools
import time

def log_call(fn):
    """Log function name, arguments, and return value on every call."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f'[CALL]   {fn.__name__}  args={args[1:]}  kwargs={kwargs}')
        result = fn(*args, **kwargs)
        print(f'[RETURN] {fn.__name__} → {result}')
        return result
    return wrapper

def timed(fn):
    """Print elapsed time in milliseconds on every call."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = (time.perf_counter() - t0) * 1000
        print(f'[TIMED]  {fn.__name__} took {elapsed:.2f} ms')
        return result
    return wrapper
```

---

## 6 — Strategy
`BEHAVIORAL`

### What is it?

The Strategy pattern defines a **family of interchangeable algorithms** and lets callers swap them at runtime without changing the context that uses them. The context holds a reference to a strategy object and delegates the varying behaviour to it.

### Why does it matter?

When a method needs to behave differently depending on a choice — sort by name, sort by power, sort by availability — a chain of `if/elif` blocks is the naive solution. It grows with every new option and cannot be extended without modifying the method. Strategy turns each option into an object, and makes extension trivial: add a class, nothing else changes.

### Where to implement it in the Stable

The `Stable`'s iteration order is currently fixed. A stable master might want to view creatures sorted by power, by name, or by availability. A `SortStrategy` plugged into `Stable.sorted()` makes sorting interchangeable at runtime.

- `SortStrategy` Protocol: a single method `sort(creatures: list[Creature]) -> list[Creature]`.
- `SortByPower`: descending `power_level` — already the `StableIterator` default.
- `SortByName`: alphabetical by `creature.name`.
- `SortByAvailability`: in-stable creatures first, then those on missions.
- `Stable.available_by_power()` becomes `Stable.sorted(strategy: SortStrategy)`.

### Your tasks

1. Define a `SortStrategy` Protocol with a `sort(creatures)` method.
2. Implement `SortByPower`, `SortByName`, and `SortByAvailability`.
3. Add a `sorted(strategy: SortStrategy)` method to `Stable` that returns a sorted list.
4. Demonstrate runtime swapping: call `stable.sorted(SortByName())` then `stable.sorted(SortByPower())` and print both results.
5. **Bonus:** add `SortByMissionReturn` that sorts on-mission creatures by their expected `return_date` (requires access to the `MissionRepository`).

### Implementation hints

```python
class SortStrategy(Protocol):
    def sort(self, creatures: list[Creature]) -> list[Creature]: ...

class SortByPower:
    """Sort creatures by power_level descending."""
    def sort(self, creatures: list[Creature]) -> list[Creature]:
        return sorted(creatures, key=lambda c: c.power_level, reverse=True)

class SortByName:
    """Sort creatures alphabetically by name."""
    def sort(self, creatures: list[Creature]) -> list[Creature]:
        return sorted(creatures, key=lambda c: c.name)

class SortByAvailability:
    """Sort in-stable creatures first, then those on missions."""
    def sort(self, creatures: list[Creature]) -> list[Creature]:
        return sorted(creatures, key=lambda c: (not c._in_stable, c.name))
```

---

## 7 — Observer
`BEHAVIORAL`

### What is it?

The Observer pattern (also called **Publish/Subscribe** or **Event Bus**) lets multiple independent listeners react to events without being coupled to the publisher. The publisher emits named events; each listener subscribes to the events it cares about and is called automatically.

### Why does it matter?

Without Observer, a service that needs to notify multiple things on dispatch — log it, check for overdue missions, trigger an alert — must call each one explicitly, and importing each notifier couples `MissionService` to all of them. Observer removes that coupling: the service just publishes an event, and listeners self-register.

### Where to implement it in the Stable

`MissionService` already uses an injected logger. But logging is just one reaction to a dispatch event. An `EventBus` lets any number of independent listeners — an `AuditLogger`, an `OverdueChecker`, a `RoyalNotifier` — subscribe to `'mission_dispatched'` and `'mission_recalled'` without `MissionService` knowing they exist.

- `EventBus`: `subscribe(event_name, listener_fn)`, `publish(event_name, payload)`.
- `'mission_dispatched'` event carries the `MissionRecord` as payload.
- `'mission_recalled'` event carries the `creature_name` string as payload.
- `AuditLogger` listener: prints a timestamped audit line on every event.
- `OverdueChecker` listener: on `'mission_recalled'`, checks if the record was overdue and prints a warning.

### Your tasks

1. Implement `EventBus` with `subscribe(event, fn)` and `publish(event, payload)`. Store subscribers in a `dict[str, list[callable]]`.
2. Wire `EventBus` into `MissionService`: inject it via `__init__`, call `self._bus.publish()` at the end of `dispatch()` and `recall()`.
3. Write an `AuditLogger` function *(not a class — a plain function is a valid listener)* that prints a timestamped entry.
4. Write an `OverdueChecker` function that checks the record's `is_overdue` on `'mission_recalled'`.
5. Subscribe both listeners and confirm they are both called on every dispatch and recall, in subscription order.

### Implementation hints

```python
class EventBus:
    """Publish/subscribe event bus — decouples publishers from listeners."""

    def __init__(self) -> None:
        self._listeners: dict[str, list] = {}

    def subscribe(self, event: str, fn) -> None:
        self._listeners.setdefault(event, []).append(fn)

    def publish(self, event: str, payload) -> None:
        for fn in self._listeners.get(event, []):
            fn(payload)

# Listener functions — plain functions are valid listeners
def audit_logger(payload) -> None:
    from datetime import datetime
    print(f'[AUDIT {datetime.now():%H:%M:%S}] {payload}')

def overdue_checker(record: MissionRecord) -> None:
    if record.is_overdue:
        print(f'⚠️  OVERDUE: {record.creature_name} was due back on {record.return_date}')
```

---

## 8 — Command
`BEHAVIORAL`

### What is it?

The Command pattern **encapsulates a request as an object**. Each command object knows how to execute an action and, crucially, how to undo it. A `CommandHistory` stack stores executed commands and enables undo/redo by replaying or reversing them in order.

### Why does it matter?

Once an action is an object, it becomes composable, storable, and reversible. A stable master who accidentally dispatches the wrong creature can undo the last command rather than manually recreating the previous state. This is the foundation of every undo/redo system, transaction log, and macro recorder.

### Where to implement it in the Stable

Dispatching and recalling creatures are natural commands. `DispatchCommand` executes a dispatch and can undo it with a recall. `RecallCommand` executes a recall and can undo it with a re-dispatch. `CommandHistory.undo_last()` pops and reverses the last executed command.

- `Command` Protocol: `execute() -> None` and `undo() -> None`.
- `DispatchCommand(service, name, destination, days)`: `execute()` calls `service.dispatch()`, `undo()` calls `service.recall()`.
- `RecallCommand(service, name)`: `execute()` calls `service.recall()`, `undo()` re-dispatches (store record data at construction time).
- `CommandHistory`: a stack (`list`) of executed commands. `execute(cmd)` runs and pushes; `undo_last()` pops and undoes.

### Your tasks

1. Define a `Command` Protocol with `execute()` and `undo()`.
2. Implement `DispatchCommand` and `RecallCommand`.
3. Implement `CommandHistory` with `execute(cmd)` and `undo_last()`. `undo_last()` must raise `IndexError` (or print a warning) if the history is empty.
4. Demonstrate: dispatch Frostbite, dispatch Ember, undo last (Ember returns), undo last (Frostbite returns). Print stable state after each step.
5. **Bonus:** add `redo_last()` — this requires a separate redo stack.

### Implementation hints

```python
class Command(Protocol):
    def execute(self) -> None: ...
    def undo(self) -> None: ...

class DispatchCommand:
    """Dispatch a creature on a mission. Undoable with recall."""

    def __init__(self, service: MissionService, name: str, destination: str, days: int) -> None:
        self._service     = service
        self._name        = name
        self._destination = destination
        self._days        = days

    def execute(self) -> None:
        self._service.dispatch(self._name, self._destination, self._days)

    def undo(self) -> None:
        self._service.recall(self._name)

class CommandHistory:
    """Stack of executed commands. Supports single-level undo."""

    def __init__(self) -> None:
        self._stack: list[Command] = []

    def execute(self, cmd: Command) -> None:
        cmd.execute()
        self._stack.append(cmd)

    def undo_last(self) -> None:
        if not self._stack:
            raise IndexError('Nothing to undo.')
        self._stack.pop().undo()
```

---

*Mythical Creature Stable — Day 5: Design Patterns*
