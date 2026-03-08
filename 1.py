# ============================================================
# 🎓 PERSONALIZED LEARNING PATH GENERATOR
# Powered by Google Gemini Flash 2.0 Preview
# Ready to run on Google Colab
# ============================================================

# ── STEP 1: Install dependencies ──────────────────────────────
# !pip install google-generativeai -q

import google.generativeai as genai
import textwrap

# ── STEP 2: Configure your API Key ────────────────────────────
# Paste your Gemini API key below 👇
API_KEY = "AIzaSyDTIuozum8gLZrlX8BNlKn4PLs-pkKSr-s"

genai.configure(api_key=API_KEY)

# ── STEP 3: Set up the model ───────────────────────────────────
model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview",   # Gemini Flash 2.0 Preview
    generation_config={
        "temperature": 0.8,
        "top_p": 0.95,
        "max_output_tokens": 4096,
    }
)

# ── STEP 4: Core function ──────────────────────────────────────
def generate_learning_path(skill: str, level: str, goal: str, hours_per_week: int) -> str:
    """
    Generate a personalized week-by-week learning curriculum.

    Args:
        skill          : The skill to learn (e.g., "Machine Learning", "React")
        level          : Current level — Beginner / Intermediate / Advanced
        goal           : What you want to achieve (e.g., "get a job", "build a project")
        hours_per_week : How many hours per week you can dedicate

    Returns:
        A formatted learning path string
    """

    prompt = f"""
You are an expert curriculum designer and career coach.

Create a detailed, personalized week-by-week learning path for the following learner:

- **Skill to Learn**: {skill}
- **Current Level**: {level}
- **Goal**: {goal}
- **Available Time**: {hours_per_week} hours per week

Instructions:
1. Generate a realistic plan (4–12 weeks depending on complexity).
2. For each week include:
   - 📌 Week number and theme/title
   - 🎯 Clear learning objectives (bullet points)
   - 📚 Specific free resources (with names — e.g., YouTube channels, docs, courses)
   - 🛠️ A hands-on mini project or exercise
   - ✅ End-of-week milestone to self-assess progress
3. After the weekly plan, add:
   - 💡 Pro Tips section (3–5 tips specific to this skill)
   - 🚀 Resume/Portfolio suggestions for showcasing this skill
4. Keep the tone motivating and practical.
5. Format the output clearly with headers and emojis for readability.

Begin the learning path now:
"""

    print(f"\n⏳ Generating your personalized learning path for '{skill}'...\n")
    print("=" * 65)

    response = model.generate_content(prompt)
    return response.text


# ── STEP 5: Pretty printer ─────────────────────────────────────
def print_learning_path(text: str):
    """Wrap and print the learning path nicely in Colab."""
    for line in text.split("\n"):
        # Preserve empty lines
        if line.strip() == "":
            print()
        else:
            # Wrap long lines at 80 chars
            wrapped = textwrap.fill(line, width=80, subsequent_indent="   ")
            print(wrapped)


# ── STEP 6: Interactive input ──────────────────────────────────
def main():
    print("=" * 65)
    print("  🎓 PERSONALIZED LEARNING PATH GENERATOR")
    print("  Powered by Google Gemini Flash 2.0 Preview")
    print("=" * 65)

    skill = input("\n📘 What skill do you want to learn?\n→ ").strip()

    print("\n📊 What is your current level?")
    print("   1. Beginner (little to no experience)")
    print("   2. Intermediate (some experience, want to go deeper)")
    print("   3. Advanced (experienced, want to master edge cases)")
    level_choice = input("→ Enter 1, 2, or 3: ").strip()
    level_map = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}
    level = level_map.get(level_choice, "Beginner")

    goal = input(
        "\n🎯 What is your goal? (e.g., get a job, build a project, freelance)\n→ "
    ).strip()

    hours_input = input("\n⏱️  How many hours per week can you dedicate?\n→ ").strip()
    try:
        hours_per_week = int(hours_input)
    except ValueError:
        hours_per_week = 5
        print("   (Defaulting to 5 hours/week)")

    # Generate the plan
    result = generate_learning_path(skill, level, goal, hours_per_week)

    # Print it out
    print_learning_path(result)

    # ── STEP 7: Save to file ───────────────────────────────────
    safe_skill = skill.replace(" ", "_").lower()
    filename = f"learning_path_{safe_skill}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"LEARNING PATH: {skill.upper()}\n")
        f.write(f"Level: {level} | Goal: {goal} | Hours/week: {hours_per_week}\n")
        f.write("=" * 65 + "\n\n")
        f.write(result)

    print("\n" + "=" * 65)
    print(f"✅ Learning path saved to: {filename}")
    print("=" * 65)


# ── Run it ──────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
