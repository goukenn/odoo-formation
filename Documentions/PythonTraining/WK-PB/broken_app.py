"""
HR Bonus & Notification System — v2.3
======================================
Handles bonus calculations and employee notifications.
Works in production. Do not touch without talking to Dave.
"""

import csv
import json
import smtplib
import datetime
import logging
from io import StringIO
from typing import List

logging.basicConfig(level=logging.INFO)

# ── Simulated database ────────────────────────────────────────────────────────

EMPLOYEES_DB = [
    {"id": 1, "name": "Alice Martin",  "role": "engineer",   "salary": 60000, "perf": 92, "seniority": 5, "email": "alice@company.com",  "active": True},
    {"id": 2, "name": "Bob Smith",     "role": "manager",    "salary": 80000, "perf": 78, "seniority": 3, "email": "bob@company.com",    "active": True},
    {"id": 3, "name": "Carol White",   "role": "intern",     "salary": 24000, "perf": 85, "seniority": 1, "email": "carol@company.com",  "active": True},
    {"id": 4, "name": "Dave Brown",    "role": "engineer",   "salary": 65000, "perf": 55, "seniority": 2, "email": "dave@company.com",   "active": True},
    {"id": 5, "name": "Eve Davis",     "role": "manager",    "salary": 90000, "perf": 95, "seniority": 8, "email": "eve@company.com",    "active": True},
    {"id": 6, "name": "Frank Lee",     "role": "contractor", "salary": 0,     "perf": 88, "seniority": 0, "email": "frank@ext.com",      "active": True,  "day_rate": 450, "days_worked": 120},
    {"id": 7, "name": "Grace Hall",    "role": "engineer",   "salary": 58000, "perf": 74, "seniority": 1, "email": "grace@company.com",  "active": False},
]

SMTP_CONFIG = {
    "host": "smtp.company.com",
    "port": 587,
    "user": "hr@company.com",
    "pass": "s3cr3t",
}


# ── Models ────────────────────────────────────────────────────────────────────

class Employee:
    def __init__(self, data: dict):
        self.id        = data["id"]
        self.name      = data["name"]
        self.role      = data["role"]
        self.salary    = data["salary"]
        self.perf      = data["perf"]
        self.seniority = data["seniority"]
        self.email     = data["email"]
        self.active    = data.get("active", True)

    def get_annual_cost(self) -> float:
        return self.salary

    def get_display_name(self) -> str:
        return self.name


class ContractEmployee(Employee):
    def __init__(self, data: dict):
        super().__init__(data)
        self.day_rate    = data.get("day_rate", 0)
        self.days_worked = data.get("days_worked", 0)

    def get_annual_cost(self) -> float:
        # Cost already invoiced — not an annual projection like the parent
        return self.day_rate * self.days_worked

    def get_display_name(self) -> str:
        return f"[EXT] {self.name}"


# ── Main class ────────────────────────────────────────────────────────────────

class EmployeeManager:
    """Manages employees, bonuses, reports and notifications."""

    def __init__(self):
        self.employees: List[Employee] = []
        self.log: List[str] = []
        self._load()

    # ── Loading ───────────────────────────────────────────────────────────────

    def _load(self):
        for d in EMPLOYEES_DB:
            if d["role"] == "contractor":
                self.employees.append(ContractEmployee(d))
            else:
                self.employees.append(Employee(d))

    # ── Bonus calculation ─────────────────────────────────────────────────────

    def calculate_bonus(self, emp: Employee) -> float:
        """Calculate annual bonus based on role and performance score."""
        b = 0
        if emp.role == "engineer":
            if emp.perf >= 90:
                b = emp.salary * 0.15
            elif emp.perf >= 70:
                b = emp.salary * 0.08
            else:
                b = 0
            if emp.seniority > 3:
                b += 500
        elif emp.role == "manager":
            if emp.perf >= 85:
                b = emp.salary * 0.20
            elif emp.perf >= 65:
                b = emp.salary * 0.12
            else:
                b = emp.salary * 0.05
            if emp.seniority > 5:
                b += 1500
        elif emp.role == "intern":
            if emp.perf >= 80:
                b = 1000
            else:
                b = 0
        elif emp.role == "contractor":
            b = 0
        return b

    # ── Reporting ─────────────────────────────────────────────────────────────

    def generate_report(self, fmt: str, include_inactive: bool = False) -> str:
        """Generate a bonus report. Supported formats: csv, html, json."""
        data = []
        for emp in self.employees:
            if not include_inactive and not emp.active:
                continue
            b = self.calculate_bonus(emp)
            data.append((emp, b))

        if fmt == "csv":
            out = StringIO()
            w = csv.writer(out)
            w.writerow(["ID", "Name", "Role", "Salary", "Bonus", "Total"])
            for emp, b in data:
                w.writerow([
                    emp.id, emp.name, emp.role,
                    emp.salary, round(b, 2), round(emp.salary + b, 2),
                ])
            self.log.append(f"{datetime.datetime.now()} - CSV report generated")
            logging.info("CSV report generated")
            return out.getvalue()

        elif fmt == "html":
            rows = ""
            for emp, b in data:
                rows += (
                    f"<tr><td>{emp.id}</td><td>{emp.name}</td><td>{emp.role}</td>"
                    f"<td>{emp.salary}</td><td>{round(b, 2)}</td>"
                    f"<td>{round(emp.salary + b, 2)}</td></tr>"
                )
            return f"""<html><body>
<h1>Bonus Report — {datetime.date.today()}</h1>
<table border='1'>
<tr><th>ID</th><th>Name</th><th>Role</th><th>Salary</th><th>Bonus</th><th>Total</th></tr>
{rows}
</table></body></html>"""

        elif fmt == "json":
            result = [
                {"id": emp.id, "name": emp.name, "bonus": round(b, 2)}
                for emp, b in data
            ]
            self.log.append(f"{datetime.datetime.now()} - JSON report generated")
            return json.dumps(result, indent=2)

        else:
            raise ValueError(f"Unknown format: {fmt}")

    # ── Notifications ─────────────────────────────────────────────────────────

    def send_notifications(self, dry_run: bool = False):
        """Send bonus notification emails to all active employees."""
        for emp in self.employees:
            if not emp.active:
                continue

            b = self.calculate_bonus(emp)

            if b == 0:
                body = (
                    f"Dear {emp.name},\n\n"
                    "Unfortunately you did not qualify for a bonus this year.\n\n"
                    "HR Team"
                )
            else:
                body = (
                    f"Dear {emp.name},\n\n"
                    f"Congratulations! Your bonus this year is €{round(b, 2)}.\n\n"
                    "HR Team"
                )

            subject = "Your Annual Bonus"

            if not dry_run:
                try:
                    server = smtplib.SMTP(SMTP_CONFIG["host"], SMTP_CONFIG["port"])
                    # server.login(SMTP_CONFIG["user"], SMTP_CONFIG["pass"])
                    # server.sendmail(SMTP_CONFIG["user"], emp.email, body)
                    logging.info(f"Email sent to {emp.email}")
                except Exception as e:
                    logging.error(f"Failed to send to {emp.email}: {e}")
            else:
                print(f"[DRY RUN] To: {emp.email}")
                print(f"[DRY RUN] Subject: {subject}")
                print(f"[DRY RUN] {body[:80]}...\n")

            self.log.append(f"{datetime.datetime.now()} - Notified {emp.email}")

    # ── Stats ─────────────────────────────────────────────────────────────────

    def get_stats(self):
        """Print a summary of the bonus campaign."""
        total = sum(self.calculate_bonus(e) for e in self.employees)
        avg   = total / len(self.employees) if self.employees else 0
        top   = max(self.employees, key=lambda e: self.calculate_bonus(e))

        print(f"Total bonuses : €{round(total, 2)}")
        print(f"Average bonus : €{round(avg, 2)}")
        print(f"Top performer : {top.name} (€{round(self.calculate_bonus(top), 2)})")
        # TODO: add median
        # TODO: breakdown by department

    # ── Costs ─────────────────────────────────────────────────────────────────

    def print_total_workforce_cost(self):
        """Print total annual cost of the workforce."""
        total = sum(e.get_annual_cost() for e in self.employees)
        print(f"Total workforce cost: €{round(total, 2)}")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mgr = EmployeeManager()

    print("=== CSV Report ===")
    print(mgr.generate_report("csv"))

    print("=== Stats ===")
    mgr.get_stats()

    print("=== Workforce Cost ===")
    mgr.print_total_workforce_cost()

    print("\n=== Dry-run Notifications ===")
    mgr.send_notifications(dry_run=True)
