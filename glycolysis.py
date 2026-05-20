import matplotlib.pyplot as plt

starting_glucose = int(input("Enter number of glucose molecules: "))
glucose = starting_glucose
ATP = 0
NADH = 0
pyruvate = 0
ATP_history = []

def record_state():
    ATP_history.append(ATP)

def investment():
    global ATP
    ATP -= 2 * starting_glucose

def splitting():
    global glucose
    global pyruvate
    glucose = 0
    pyruvate += 2 * starting_glucose

def payoff():
    global ATP
    global NADH
    ATP += 4 * starting_glucose
    NADH += 2 * starting_glucose

def print_totals(stage):
    print("---------------")
    print(stage)
    print(f"Glucose: {glucose}")
    print(f"ATP: {ATP}")
    print(f"NADH: {NADH}")
    print(f"Pyruvate: {pyruvate}")

print_totals("Initial State")
record_state()

investment()
print_totals("Investment Phase")
record_state()

splitting()
print_totals("Splitting Phase")
record_state()

payoff()
print_totals("Payoff Phase")
record_state()

stages = ["Initial", "Investment", "Splitting", "Payoff"]

plt.plot(stages, ATP_history, marker="o")
plt.grid(True)
plt.title("ATP Change During Glycolysis")
plt.xlabel("Stage")
plt.ylabel("ATP")
plt.show()

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))

# Text boxes
plt.text(0.5, 0.85, "Glucose", ha="center", va="center",
         bbox=dict(boxstyle="round", facecolor="white"))

plt.text(0.5, 0.55, "Splitting Phase\n2 × 3-carbon molecules", ha="center", va="center",
         bbox=dict(boxstyle="round", facecolor="white"))

plt.text(0.5, 0.25, "2 Pyruvate", ha="center", va="center",
         bbox=dict(boxstyle="round", facecolor="white"))

# Arrows
plt.annotate("-2 ATP used",
             xy=(0.5, 0.62), xytext=(0.5, 0.78),
             arrowprops=dict(arrowstyle="->"),
             ha="center")

plt.annotate("+4 ATP\n+2 NADH",
             xy=(0.5, 0.32), xytext=(0.5, 0.48),
             arrowprops=dict(arrowstyle="->"),
             ha="center")

# Final summary
plt.text(0.5, 0.08, "Net yield per glucose: +2 ATP, +2 NADH, 2 Pyruvate",
         ha="center", va="center")

plt.axis("off")
plt.title("Simplified Glycolysis Flow")
plt.tight_layout()
plt.show()