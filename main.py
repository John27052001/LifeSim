from logic import run_simulation
from personas import get_persona

def ask_user_choices():
    print("🌱 Welcome to LifeSim — Simulate Your Future")
    print("Answer a few questions to build your life path.\n")

    persona = input("Choose your persona (The Dreamer / The Hustler / The Balanced One): ").strip().lower()
    career = input("Career path (engineer / founder / freelancer): ").strip().lower()
    lifestyle = input("Lifestyle (balanced / burnout / chilled): ").strip().lower()
    habits = input("Financial habit? (spender / saver / investor): ").strip().lower()

    return {
        "career": career,
        "lifestyle": lifestyle,
        "habits": habits,
        "persona": get_persona(persona)
    }

if __name__ == "__main__":
    user_input = ask_user_choices()
    print("\n🔮 Simulating your future...\n")
    report = run_simulation(user_input)
    print(report)
    with open("lifesim_report.txt", "w") as f:
        f.write(report)
        print("\n📄 Your LifeSim report was saved to 'lifesim_report.txt'")

