import time

def engine_check():
    print("🔧 Engine: Running smoothly.")

def brake_check():
    print("🛑 Brakes: All pads are in good condition.")

def tire_pressure_check():
    print("⚠️ Tire Pressure: Front-left tire slightly low. Recommend refill.")

def battery_status():
    print("🔋 Battery: 82% - functioning well.")

def fuel_efficiency_tip():
    print("💡 Tip: Avoid rapid acceleration to improve fuel efficiency.")

def run_porsche_assistant():
    print("🚗 Starting Porsche AI Assistant...\n")
    time.sleep(1)
    engine_check()
    time.sleep(1)
    brake_check()
    time.sleep(1)
    tire_pressure_check()
    time.sleep(1)
    battery_status()
    time.sleep(1)
    fuel_efficiency_tip()
    print("\n✅ System Check Complete. You’re good to drive!")

# Run the assistant
run_porsche_assistant()
