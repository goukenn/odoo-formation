"""
Mythical Creature Stable — Day 3 Solution
==========================================
Covers all Day 3 concepts:
  Exercise 1 — @dataclass, __post_init__, __eq__ / __hash__
  Exercise 2 — Composition, __len__ / __contains__ / __iter__ / __getitem__
  Exercise 3 — Custom iterator (__iter__ / __next__)
  Exercise 4 — Dependency injection, MissionService
  Exercise 5 — Context managers (__enter__/__exit__ + contextlib)
  Exercise 6 — Protocol (structural subtyping)

Builds on the Day 2 solution: Creature (ABC), Dragon, Phoenix, Unicorn,
LegendaryDragon, LoggableMixin are assumed to be available and imported.
They are reproduced here in full so this file runs standalone.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Iterator, Protocol


# ==============================================================================
# DAY 2 BASE — reproduced here so the file is self-contained
# ==============================================================================

class Creature(ABC):
    """Abstract base for all stable creatures. Enforces mission interface."""

    _total_creatures: int = 0

    def __init__(self, name: str, species: str, origin: str, power_level: float) -> None:
        self.name = name
        self.species = species
        self.__origin = origin
        self._power_level: float | None = None
        self.power_level = power_level
        self._in_stable: bool = True
        Creature._total_creatures += 1

    @abstractmethod
    def mission_duration_days(self) -> int: ...

    @abstractmethod
    def describe_abilities(self) -> str: ...

    def send_on_mission(self) -> None:
        self._in_stable = False

    def return_to_stable(self) -> None:
        self._in_stable = True

    @property
    def power_level(self) -> float:
        return self._power_level

    @power_level.setter
    def power_level(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError(f"power_level must be a number, got {type(value).__name__}.")
        if not (0 <= value <= 100):
            raise ValueError(f"power_level must be between 0 and 100, got {value}.")
        self._power_level = float(value)

    @property
    def origin(self) -> str:
        return self.__origin

    @classmethod
    def get_total_creatures(cls) -> int:
        return cls._total_creatures

    @staticmethod
    def is_valid_species(species: str) -> bool:
        return species in ["Dragon", "Ice Dragon", "Phoenix", "Griffin", "Unicorn", "Basilisk"]

    def __str__(self) -> str:
        status = "in stable" if self._in_stable else "on mission"
        return f"{self.name} the {self.species} (origin: {self.origin}) [{status}]"

    def __repr__(self) -> str:
        return (
            f"Creature(name={self.name!r}, species={self.species!r}, "
            f"origin={self.origin!r}, power_level={self.power_level!r})"
        )


class Dragon(Creature):
    def __init__(self, name: str, origin: str, power_level: float, element: str = "fire") -> None:
        super().__init__(name=name, species="Dragon", origin=origin, power_level=power_level)
        self.element = element

    def mission_duration_days(self) -> int:
        return 14

    def describe_abilities(self) -> str:
        return (
            f"{self.name} breathes {self.element} and flies at great speed, "
            f"capable of destroying fortifications in a single pass."
        )

    def __str__(self) -> str:
        status = "in stable" if self._in_stable else "on mission"
        return f"{self.name} the Dragon [{self.element}] (origin: {self.origin}) [{status}]"

    def __repr__(self) -> str:
        return (
            f"Dragon(name={self.name!r}, origin={self.origin!r}, "
            f"power_level={self.power_level!r}, element={self.element!r})"
        )


class Phoenix(Creature):
    def __init__(self, name: str, origin: str, power_level: float) -> None:
        super().__init__(name=name, species="Phoenix", origin=origin, power_level=power_level)
        self.resurrection_count: int = 0

    def mission_duration_days(self) -> int:
        return 7

    def describe_abilities(self) -> str:
        return (
            f"{self.name} is wreathed in an aura of living flame and resurrects "
            f"upon death (resurrections so far: {self.resurrection_count})."
        )

    def resurrect(self) -> None:
        self.resurrection_count += 1
        print(f"🔥 {self.name} rises from the ashes! Resurrection #{self.resurrection_count}.")

    def __repr__(self) -> str:
        return (
            f"Phoenix(name={self.name!r}, origin={self.origin!r}, "
            f"power_level={self.power_level!r}, resurrection_count={self.resurrection_count!r})"
        )


class Unicorn(Creature):
    def __init__(self, name: str, origin: str, power_level: float) -> None:
        super().__init__(name=name, species="Unicorn", origin=origin, power_level=power_level)

    def mission_duration_days(self) -> int:
        return 3

    def describe_abilities(self) -> str:
        return (
            f"{self.name} can heal wounds, neutralise poison, and outrun "
            f"any mount — but must not be sent out alone if weakened."
        )

    def send_on_mission(self) -> None:
        if self.power_level < 50:
            raise RuntimeError(
                f"{self.name} has power level {self.power_level} — too low for a solo mission."
            )
        super().send_on_mission()

    def __repr__(self) -> str:
        return (
            f"Unicorn(name={self.name!r}, origin={self.origin!r}, "
            f"power_level={self.power_level!r})"
        )


# ==============================================================================
# EXERCISE 1 — @dataclass, __post_init__, __eq__ / __hash__
# ==============================================================================

@dataclass
class MissionRecord:
    """Immutable record of a single creature mission.

    Two records are considered duplicates if they share the same creature_name
    and departure_date — regardless of destination or duration. This lets the
    stable detect if a creature is double-booked on the same day.

    __eq__ and __hash__ are defined manually (not via frozen=True) to
    demonstrate the relationship: defining __eq__ silently sets __hash__ to
    None, making the object unhashable unless __hash__ is also defined.
    """

    creature_name: str
    destination: str
    departure_date: date
    duration_days: int
    notes: str = field(default="")
    _active: bool = field(default=True, init=False, repr=False)

    def __post_init__(self) -> None:
        if not self.destination.strip():
            raise ValueError("destination must not be empty.")
        if not isinstance(self.duration_days, int) or self.duration_days <= 0:
            raise ValueError(f"duration_days must be a positive integer, got {self.duration_days!r}.")

    # --- computed properties ---

    @property
    def return_date(self) -> date:
        """Expected return date based on departure and duration."""
        return self.departure_date + timedelta(days=self.duration_days)

    @property
    def is_overdue(self) -> bool:
        """True if the expected return date has passed and the mission is still active."""
        return self._active and self.return_date < date.today()

    def close(self) -> None:
        """Mark this record as closed (creature has returned)."""
        self._active = False

    # --- equality by identity: same creature, same departure date ---

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MissionRecord):
            return NotImplemented
        return self.creature_name == other.creature_name and self.departure_date == other.departure_date

    def __hash__(self) -> int:
        # Must be defined together with __eq__.
        # If __eq__ is defined and __hash__ is not, Python sets __hash__ = None,
        # making the object unhashable (cannot be stored in sets or used as dict keys).
        return hash((self.creature_name, self.departure_date))

    def __str__(self) -> str:
        status = "ACTIVE" if self._active else "CLOSED"
        overdue = " ⚠️  OVERDUE" if self.is_overdue else ""
        return (
            f"[{status}{overdue}] {self.creature_name} → {self.destination} "
            f"({self.departure_date} to {self.return_date})"
        )


# ==============================================================================
# EXERCISE 2 — Composition & container special methods
# ==============================================================================

class Stable:
    """A container for Creature objects.

    Composition over inheritance: Stable *has* a list of creatures — it does
    not *extend* list. This gives full control over the public interface:
    add() enforces uniqueness, remove() is by name, and the iteration order
    is defined by the class, not by list's internal ordering.

    Special methods make Stable feel native to Python:
      len(stable), "Frostbite" in stable, stable["Ember"], for c in stable
    """

    def __init__(self) -> None:
        self._creatures: list[Creature] = []

    # --- mutation ---

    def add(self, creature: Creature) -> None:
        """Register a creature. Raises ValueError if a creature with the same name already exists."""
        if creature.name in self:
            raise ValueError(f"A creature named '{creature.name}' is already registered.")
        self._creatures.append(creature)

    def remove(self, name: str) -> None:
        """Remove a creature by name. Raises KeyError if not found."""
        creature = self[name]
        self._creatures.remove(creature)

    def find(self, name: str) -> Creature:
        """Return the creature with the given name. Raises KeyError if not found."""
        for creature in self._creatures:
            if creature.name == name:
                return creature
        raise KeyError(f"No creature named '{name}' in the stable.")

    # --- container special methods ---

    def __len__(self) -> int:
        return len(self._creatures)

    def __contains__(self, name: object) -> bool:
        """Support: 'Frostbite' in stable"""
        if not isinstance(name, str):
            return False
        return any(c.name == name for c in self._creatures)

    def __iter__(self) -> Iterator[Creature]:
        """Support: for creature in stable"""
        return iter(self._creatures)

    def __getitem__(self, name: str) -> Creature:
        """Support: stable['Ember']"""
        return self.find(name)

    def available_by_power(self) -> "StableIterator":
        """Return a StableIterator over creatures currently in the stable, by power descending."""
        return StableIterator(self._creatures)

    def __repr__(self) -> str:
        names = [c.name for c in self._creatures]
        return f"Stable({len(self)} creatures: {names})"


# ==============================================================================
# EXERCISE 3 — Custom iterator (__iter__ / __next__)
# ==============================================================================

class StableIterator:
    """Iterates over creatures that are currently in the stable, strongest first.

    Filtering and sorting happen at construction time — the snapshot is fixed
    when the iterator is created, not lazily on each __next__ call. This means
    sending a creature on a mission mid-iteration will not affect the current
    traversal.

    Stable is an *iterable* (it has __iter__ returning a new iterator each
    time). StableIterator is an *iterator* — it has __iter__ returning self,
    and __next__ advancing state. The distinction matters: an iterable can be
    traversed multiple times; an iterator is single-use.
    """

    def __init__(self, creatures: list[Creature]) -> None:
        available = [c for c in creatures if c._in_stable]
        self._snapshot: list[Creature] = sorted(
            available, key=lambda c: c.power_level, reverse=True
        )
        self._index: int = 0

    def __iter__(self) -> StableIterator:
        return self

    def __next__(self) -> Creature:
        if self._index >= len(self._snapshot):
            raise StopIteration
        creature = self._snapshot[self._index]
        self._index += 1
        return creature


# ==============================================================================
# EXERCISE 6 — Protocol (defined before Exercise 4 so it can type MissionService)
# ==============================================================================

class MissionLogger(Protocol):
    """Structural interface for mission loggers.

    Any class with log_departure() and log_return() satisfies this Protocol —
    no inheritance required. mypy checks compliance statically.

    Protocol vs ABC:
      ABC    — requires inheritance, checked at instantiation, can carry
               shared implementation and state. Use when subclasses share code.
      Protocol — no inheritance, checked by static analysis only (mypy),
               no implementation. Use to describe what an object must do
               without constraining what it must be.
    """

    def log_departure(self, record: MissionRecord) -> None: ...
    def log_return(self, creature_name: str) -> None: ...


# ==============================================================================
# EXERCISE 4 — Dependency injection & MissionService
# ==============================================================================

class ConsoleMissionLogger:
    """Logs mission events to stdout. Satisfies MissionLogger structurally."""

    def log_departure(self, record: MissionRecord) -> None:
        print(f"⚔️  DEPARTED  | {record.creature_name} → {record.destination} "
              f"| back by {record.return_date}")

    def log_return(self, creature_name: str) -> None:
        print(f"🏠 RETURNED  | {creature_name} is back in the stable.")


class FileMissionLogger:
    """Appends mission events to a file. Satisfies MissionLogger structurally."""

    def __init__(self, filepath: str) -> None:
        self._filepath = filepath

    def log_departure(self, record: MissionRecord) -> None:
        with open(self._filepath, "a") as f:
            f.write(
                f"DEPARTED | {record.creature_name} → {record.destination} "
                f"| {record.departure_date} → {record.return_date}\n"
            )

    def log_return(self, creature_name: str) -> None:
        with open(self._filepath, "a") as f:
            f.write(f"RETURNED | {creature_name}\n")


class SilentLogger:
    """No-op logger for use in tests. Satisfies MissionLogger with zero side effects."""

    def log_departure(self, record: MissionRecord) -> None:
        pass

    def log_return(self, creature_name: str) -> None:
        pass


class MissionService:
    """Orchestrates creature dispatching and recall.

    Dependency injection: the logger is passed in — MissionService never
    creates it internally. Swap ConsoleMissionLogger for SilentLogger in
    tests and the service behaves identically with no console/file output.

    Design note for Day 5: this class is a natural candidate for the
    Facade pattern — it coordinates Stable, MissionRecord, and MissionLogger
    behind a single interface.
    """

    def __init__(self, stable: Stable, logger: MissionLogger) -> None:
        self._stable = stable
        self._logger = logger
        self._active: dict[str, MissionRecord] = {}  # creature_name → record

    def dispatch(
        self,
        creature_name: str,
        destination: str,
        duration_days: int,
        notes: str = "",
    ) -> MissionRecord:
        """Send a creature on a mission and create a MissionRecord for it."""
        if creature_name in self._active:
            raise RuntimeError(f"{creature_name} is already on an active mission.")

        creature = self._stable[creature_name]

        with mission_lock(creature):
            record = MissionRecord(
                creature_name=creature_name,
                destination=destination,
                departure_date=date.today(),
                duration_days=duration_days,
                notes=notes,
            )
            creature.send_on_mission()
            self._active[creature_name] = record
            self._logger.log_departure(record)

        return record

    def recall(self, creature_name: str) -> None:
        """Return a creature from its mission and close the record."""
        if creature_name not in self._active:
            raise KeyError(f"{creature_name} has no active mission.")

        creature = self._stable[creature_name]
        record = self._active.pop(creature_name)
        record.close()
        creature.return_to_stable()
        self._logger.log_return(creature_name)

    def active_missions(self) -> list[MissionRecord]:
        """Return all currently open mission records."""
        return list(self._active.values())


# ==============================================================================
# EXERCISE 5 — Context managers
# ==============================================================================

# --- Part A: __enter__ / __exit__ ---

class ScrollArchive:
    """File-backed mission archive managed as a context manager.

    __enter__ opens the file and returns self so the 'as' clause works.
    __exit__ always closes the file — returning False ensures exceptions
    propagate normally rather than being suppressed.

    Returning True from __exit__ would silently swallow any exception raised
    inside the 'with' block — almost never the right choice.
    """

    def __init__(self, filepath: str) -> None:
        self._filepath = filepath
        self._file = None

    def __enter__(self) -> ScrollArchive:
        self._file = open(self._filepath, "a", encoding="utf-8")
        print(f"📜 Scroll opened: {self._filepath}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self._file:
            self._file.close()
            self._file = None

        if exc_type is None:
            print("📜 Scroll sealed.")
        else:
            print(f"⚠️  Scroll sealed after error: {exc_val}")

        return False  # do not suppress exceptions

    def _require_open(self) -> None:
        if self._file is None or self._file.closed:
            raise RuntimeError("Scroll is not open. Use 'with ScrollArchive(...) as scroll:'.")

    def write_departure(self, record: MissionRecord) -> None:
        """Append a departure entry. Must be called inside a 'with' block."""
        self._require_open()
        self._file.write(
            f"DEPARTED | {record.creature_name} → {record.destination} "
            f"| {record.departure_date} → {record.return_date}\n"
        )

    def write_return(self, creature_name: str) -> None:
        """Append a return entry. Must be called inside a 'with' block."""
        self._require_open()
        self._file.write(f"RETURNED | {creature_name}\n")


# --- Part B: contextlib.contextmanager ---

@contextmanager
def mission_lock(creature: Creature) -> Iterator[Creature]:
    """Lightweight context manager that prevents a creature being double-dispatched.

    Uses @contextmanager instead of a full class because the logic is simple:
    set a flag, yield, clear it. A finally block guarantees the lock is
    released even if an exception is raised inside the 'with' block.

    This is equivalent in effect to __enter__ (set flag, yield creature)
    and __exit__ (clear flag in finally).
    """
    if getattr(creature, "_locked", False):
        raise RuntimeError(f"{creature.name} is already being processed.")

    creature._locked = True
    try:
        yield creature
    finally:
        creature._locked = False


# ==============================================================================
# DEMO
# ==============================================================================

if __name__ == "__main__":

    # --- Setup ---
    frostbite = Dragon("Frostbite", "Nordic Realms", 95, element="ice")
    ember     = Phoenix("Ember", "Ashlands", 80)
    stardust  = Unicorn("Stardust", "Silver Meadows", 72)
    tinsel    = Unicorn("Tinsel", "Soft Glades", 30)

    # ---------- Exercise 1: MissionRecord ----------
    print("=" * 60)
    print("EXERCISE 1 — MissionRecord (@dataclass, __eq__, __hash__)")
    print("=" * 60)

    r1 = MissionRecord("Frostbite", "Frozen Peaks", date(2025, 1, 10), 14)
    r2 = MissionRecord("Frostbite", "Northern Pass", date(2025, 1, 10), 7)
    r3 = MissionRecord("Ember", "Ashlands", date(2025, 1, 10), 7)

    print(f"r1 == r2 (same creature + date): {r1 == r2}")           # True
    print(f"hash(r1) == hash(r2):            {hash(r1) == hash(r2)}")  # True
    records: set[MissionRecord] = {r1, r2, r3}
    print(f"len({{r1, r2, r3}}): {len(records)} (r1 and r2 are duplicates)")  # 2

    try:
        MissionRecord("X", "", date.today(), 5)
    except ValueError as e:
        print(f"Empty destination blocked: {e}")

    try:
        MissionRecord("X", "Somewhere", date.today(), -3)
    except ValueError as e:
        print(f"Negative duration blocked: {e}")

    # ---------- Exercise 2: Stable (composition + special methods) ----------
    print("\n" + "=" * 60)
    print("EXERCISE 2 — Stable (composition, container special methods)")
    print("=" * 60)

    stable = Stable()
    stable.add(frostbite)
    stable.add(ember)
    stable.add(stardust)
    stable.add(tinsel)

    print(repr(stable))
    print(f"len(stable): {len(stable)}")
    print(f"'Frostbite' in stable: {'Frostbite' in stable}")
    print(f"'Gollum' in stable:    {'Gollum' in stable}")
    print(f"stable['Ember']: {stable['Ember']}")

    print("\nAll creatures:")
    for creature in stable:
        print(f"  {creature}")

    try:
        stable.add(frostbite)
    except ValueError as e:
        print(f"\nDuplicate blocked: {e}")

    # ---------- Exercise 3: StableIterator ----------
    print("\n" + "=" * 60)
    print("EXERCISE 3 — StableIterator (custom __iter__ / __next__)")
    print("=" * 60)

    frostbite.send_on_mission()
    print("Frostbite is on mission — should not appear below.")
    print("Available creatures by power (descending):")
    for c in stable.available_by_power():
        print(f"  {c.name} — power: {c.power_level}")

    # Iterator is single-use; a new call gives a fresh one
    it = stable.available_by_power()
    all_available = list(it)
    print(f"Count available: {len(all_available)}")
    print(f"Re-iterating (fresh): {[c.name for c in stable.available_by_power()]}")

    frostbite.return_to_stable()

    # ---------- Exercise 4: MissionService (dependency injection) ----------
    print("\n" + "=" * 60)
    print("EXERCISE 4 — MissionService (dependency injection)")
    print("=" * 60)

    service = MissionService(stable, ConsoleMissionLogger())
    rec = service.dispatch("Frostbite", "Frozen Peaks", 14, notes="Recon mission")
    print(f"Active missions: {service.active_missions()}")
    service.recall("Frostbite")
    print(f"Active missions after recall: {service.active_missions()}")

    # Swap logger — MissionService code is untouched
    file_path = "/tmp/stable_missions.log"
    file_service = MissionService(stable, FileMissionLogger(file_path))
    file_service.dispatch("Ember", "Volcanic Rift", 7, notes="Retrieve dragon egg")
    file_service.recall("Ember")
    print(f"\nFile log written to {file_path}")
    with open(file_path) as f:
        print(f.read().strip())

    # ---------- Exercise 5A: ScrollArchive (context manager class) ----------
    print("\n" + "=" * 60)
    print("EXERCISE 5A — ScrollArchive (__enter__ / __exit__)")
    print("=" * 60)

    rec1 = MissionRecord("Stardust", "Silver Forest", date.today(), 3)
    rec2 = MissionRecord("Tinsel",   "Meadow Keep",   date.today(), 5)
    archive_path = "/tmp/scroll_archive.txt"

    with ScrollArchive(archive_path) as scroll:
        scroll.write_departure(rec1)
        scroll.write_departure(rec2)
        scroll.write_return("Stardust")

    # Usage outside 'with' block raises RuntimeError
    try:
        scroll.write_departure(rec1)
    except RuntimeError as e:
        print(f"Out-of-context write blocked: {e}")

    # Exception inside 'with' — file still closes
    print("\nSimulating crash inside 'with' block:")
    try:
        with ScrollArchive(archive_path) as scroll:
            scroll.write_departure(rec1)
            raise ValueError("Simulated dispatch failure!")
            scroll.write_departure(rec2)   # never reached
    except ValueError:
        pass  # exception propagates normally (__exit__ returns False)

    print(f"Archive content:")
    with open(archive_path) as f:
        print(f.read().strip())

    # ---------- Exercise 5B: mission_lock (contextlib) ----------
    print("\n" + "=" * 60)
    print("EXERCISE 5B — mission_lock (@contextmanager)")
    print("=" * 60)

    with mission_lock(frostbite) as c:
        print(f"{c.name} locked during block: {c._locked}")
    print(f"{frostbite.name} released after block: {frostbite._locked}")

    # Lock released even on exception
    try:
        with mission_lock(ember):
            raise RuntimeError("Dispatch failure!")
    except RuntimeError:
        pass
    print(f"{ember.name} released after exception: {ember._locked}")

    # ---------- Exercise 6: Protocol ----------
    print("\n" + "=" * 60)
    print("EXERCISE 6 — Protocol (structural subtyping)")
    print("=" * 60)

    # SilentLogger satisfies MissionLogger with no inheritance
    silent_service = MissionService(stable, SilentLogger())
    silent_service.dispatch("Stardust", "Enchanted Glade", 3)
    print("SilentLogger: dispatch completed with no output.")
    silent_service.recall("Stardust")

    # BrokenLogger — missing log_return — fails at the call site, not at construction
    class BrokenLogger:
        def log_departure(self, record: MissionRecord) -> None:
            print(f"BrokenLogger: {record.creature_name} departed.")
        # log_return intentionally missing

    broken_service = MissionService(stable, BrokenLogger())  # type: ignore[arg-type]
    broken_service.dispatch("Frostbite", "Northern Pass", 5)
    try:
        broken_service.recall("Frostbite")  # AttributeError here — not at construction
    except AttributeError as e:
        print(f"Protocol violation caught at runtime: {e}")
        # With mypy, this would be caught statically before running.
        # Run: mypy mythical_stable_day3.py
        # to see the type error on the BrokenLogger assignment above.
        stable["Frostbite"].return_to_stable()  # restore stable state manually

    print("\nAll exercises completed successfully.")
