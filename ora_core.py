"""
ORA Core — Mini PoC
Implémente LOCK, REM, AUTOPROMPT, AUDIT + CLI.
"""

import uuid
import argparse

class Lock:
    def __init__(self, admin_only: bool=False):
        self.admin_only = admin_only
    def allowed(self) -> bool:
        return not self.admin_only

class REM:
    def __init__(self):
        self.memory: list[str] = []
    def retrieve_context(self, _user_input: str) -> list[str]:
        return self.memory[-2:]
    def update(self, user_input: str, result: str) -> None:
        self.memory.append(f"Q:{user_input[:160]}")
        self.memory.append(f"A:{result[:160]}")

class AutoPrompt:
    def __init__(self, iterations: int=3):
        self.iterations = int(iterations)
    def run(self, user_input: str, ctx: list[str]) -> str:
        text = user_input.strip()
        for i in range(self.iterations):
            text = self._improve(text, ctx, i+1)
        return text
    def _improve(self, text: str, ctx: list[str], step: int) -> str:
        insight = f" |ctx:{ctx[0][:24]}..." if ctx else ""
        return f"[step{step}] {text}{insight}"

class Auditor:
    def __init__(self, enabled: bool=True):
        self.enabled = enabled
    def log(self, topic: str, event: str, data: dict):
        if not self.enabled:
            return
        fp = uuid.uuid4().hex[:8]
        print(f"[AUDIT] {topic}:{event} #{fp} {data}")

class ORACore:
    def __init__(self, *, admin_only=False, iterations=3, audit=True):
        self.lock = Lock(admin_only=admin_only)
        self.rem = REM()
        self.autoprompt = AutoPrompt(iterations=iterations)
        self.audit = Auditor(enabled=audit)

    def cycle(self, user_input: str) -> str:
        if not self.lock.allowed():
            self.audit.log("LOCK","blocked",{"reason":"admin_only"})
            return "[LOCK] Action bloquée (admin_only)."
        ctx = self.rem.retrieve_context(user_input)
        self.audit.log("REM","retrieve",{"ctx_len":len(ctx)})
        result = self.autoprompt.run(user_input, ctx)
        self.audit.log("AUTOPROMPT","run",{"iterations":self.autoprompt.iterations})
        self.rem.update(user_input, result)
        self.audit.log("REM","update",{})
        return result

def main():
    p = argparse.ArgumentParser(description="ORA Core — Mini PoC")
    p.add_argument("text", nargs="*", help="Texte d'entrée")
    p.add_argument("--iterations", type=int, default=3)
    p.add_argument("--admin-only", action="store_true")
    p.add_argument("--no-audit", action="store_true")
    args = p.parse_args()

    core = ORACore(admin_only=args.admin_only, iterations=args.iterations, audit=not args.no_audit)
    user_input = " ".join(args.text) or "Bonjour ORA"
    print(core.cycle(user_input))

if __name__ == "__main__":
    main()
