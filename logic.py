import random

# 🃏 Random life event generator
def random_life_event(year):
    events = {
        1: ["You met a mentor who inspired you.", "You learned a new skill that changed your path."],
        2: ["You traveled to a new country and gained perspective.", "You launched a side project."],
        3: ["You burned out but rediscovered your passion.", "You found unexpected peace in routine."],
        4: ["You were offered a big promotion — you took it!", "You reconnected with an old friend who changed your mindset."],
        5: ["You invested in yourself — and it paid off.", "You helped someone and it shaped your purpose."]
    }
    return random.choice(events.get(year, ["Nothing major happened this year."]))

# 🔮 Main simulation engine
def run_simulation(user):
    career = user["career"]
    lifestyle = user["lifestyle"]
    habits = user["habits"]
    relationship = user.get("relationship", "single").lower()
    persona = user.get("persona", {}).get("traits", {})

    # Initial stats
    happiness = 50
    stress = 50
    money = 50
    career_growth = 50

    # Time-series tracking
    happiness_list = []
    stress_list = []
    career_list = []
    money_list = []

    log = []
    log.append(f"🎭 Persona: {user['persona']['name']}")
    log.append(f"🧬 {user['persona']['traits']['description']}\n")

    for year in range(1, 6):
        log.append(f"\n📆 Year {year}:")

        # Career logic
        if career == "engineer":
            career_growth += 8
            stress += 5 if lifestyle == "burnout" else 2
        elif career == "founder":
            career_growth += 12
            stress += 8
            happiness -= 2
        elif career == "freelancer":
            career_growth += 6
            happiness += 4
            stress += 3

        # Lifestyle logic
        if lifestyle == "burnout":
            happiness -= 5
            stress += 6
        elif lifestyle == "balanced":
            happiness += 5
            stress -= 4
        elif lifestyle == "chilled":
            happiness += 4
            career_growth -= 2

        # Financial habit logic
        if habits == "spender":
            money -= 3
        elif habits == "saver":
            money += 5
        elif habits == "investor":
            money += random.randint(-2, 10)

        # Relationship logic
        if year == 2:
            if relationship == "in a relationship":
                happiness += 5
                stress -= 3
                log.append("💑 Your partner supported you during a tough time.")
            elif relationship == "breakup":
                happiness -= 7
                stress += 6
                log.append("💔 You went through a breakup and it shook your stability.")

        # Persona traits
        happiness += persona.get("happiness_boost", 0)
        stress += persona.get("stress_penalty", 0)
        career_growth += persona.get("growth_modifier", 0)

        # Clamp values
        happiness = max(0, min(100, happiness))
        stress = max(0, min(100, stress))
        money = max(0, min(100, money))
        career_growth = max(0, min(100, career_growth))

        # Store graph data
        happiness_list.append(happiness)
        stress_list.append(stress)
        career_list.append(career_growth)
        money_list.append(money)

        # Log stats
        log.append(f"  • Career Progress: {career_growth}%")
        log.append(f"  • Happiness Level: {happiness}/100")
        log.append(f"  • Stress Level: {stress}/100")
        log.append(f"  • Money Level: {money}/100")

        # Year 3 burnout trigger
        if year == 3 and lifestyle == "burnout" and stress > 80:
            log.append("⚠️ You experienced burnout and took a sabbatical.")
            stress -= 30
            happiness += 10
            career_growth -= 5

        # Random event
        event = random_life_event(year)
        log.append(f"  🌟 {event}")

    # Final summary
    log.append("\n📊 Final Life Summary:")
    log.append(f"  • Career Success: {career_growth}/100")
    log.append(f"  • Happiness Overall: {happiness}/100")
    log.append(f"  • Financial Health: {money}/100")

    if happiness > 75 and career_growth > 70:
        log.append("✅ You lived a successful and fulfilling 5-year path!")
    elif stress > 85:
        log.append("⚠️ Consider changing your pace — high stress caught up with you.")
    else:
        log.append("🌀 Life had ups and downs — but you kept going!")

    return "\n".join(log), happiness_list, stress_list, career_list, money_list
