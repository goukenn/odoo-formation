# 🔍 Refactoring Dojo — Participant Worksheet

## The Scenario

> A colleague left this HR bonus notification system before going on leave.
> The code works, but two new requirements just came in:
>
> 1. A new **"freelance"** employee role needs to be supported
> 2. The finance team wants an **Excel export** in addition to CSV/HTML/JSON
>
> Before writing a single line, your team's job is to **understand why
> this code is hard to change** — then fix it.

---

## Phase 1 — Read & Smell (15 min, individual)

Read `broken_app.py` silently. Note anything that feels off, surprising,
or that you'd write differently. Don't look for principles yet — just trust
your instincts as a developer.

**My observations:**

```
1. _______________________________________________________________

2. _______________________________________________________________

3. _______________________________________________________________

4. _______________________________________________________________

5. _______________________________________________________________
```

---

## Phase 2 — Map to Principles (group)

Once the group has shared observations, try to match each smell to one
of these. A smell can match more than one.

| Principle | Short reminder | My smell from the code |
|---|---|---|
| **SRP** | One class = one reason to change | |
| **OCP** | Extend without modifying | |
| **LSP** | Subclasses keep their parent's promises | |
| **ISP** | Don't force classes to implement what they don't need | |
| **Clean Code** | Names, functions, comments, magic numbers | |

---

## Phase 3 — Before you refactor, design first

Answer these questions as a group before touching the code:

**1. How many classes should replace `EmployeeManager`? List them.**

```
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
```

**2. Where would you add the "freelance" bonus rule WITHOUT editing existing classes?**

```
_______________________________________________________________
_______________________________________________________________
```

**3. Where would you add the Excel formatter WITHOUT editing existing classes?**

```
_______________________________________________________________
_______________________________________________________________
```

**4. What is wrong with `ContractEmployee.get_annual_cost()`?**
*(Hint: call it on all employees and sum the results. What does that number mean?)*

```
_______________________________________________________________
_______________________________________________________________
```

---

## Phase 4 — Refactor

Work as a mob or in pairs. One principle at a time.

Suggested order:
1. Rename bad variables / extract magic numbers as constants
2. Fix the LSP violation in `ContractEmployee`
3. Split `EmployeeManager` into focused classes
4. Eliminate the `if/elif` chains with a better structure

**Track your decisions here:**

```
Decision 1: ____________________________________________________
Why: ___________________________________________________________

Decision 2: ____________________________________________________
Why: ___________________________________________________________

Decision 3: ____________________________________________________
Why: ___________________________________________________________
```

---

## ✅ Done? Run this checklist.

```
□ Adding "freelance" required zero changes to existing bonus logic
□ Adding Excel export required zero changes to existing formatters
□ get_annual_cost() always means the same thing, regardless of subclass
□ No class has more than one reason to change
□ Every magic number has a name and lives in one place
□ No function name lies about what it does
```

---

## 💬 Reflection (5 min, individual, after debrief)

**One thing I'll do differently in my own code starting tomorrow:**

```
_______________________________________________________________
_______________________________________________________________
```
