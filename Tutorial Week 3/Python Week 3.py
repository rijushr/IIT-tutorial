# Alarm logic for car seatbelt system
# IIT Tutorial Week 3 

# Input signals (1 = HIGH, 0 = LOW)
# Change these values to test the circuit
DRIV  = 1   # Driver seat occupied
PASS  = 1   # Passenger seat occupied
BELTD = 0   # Driver seatbelt unfastened (active-LOW)
BELTP = 0   # Passenger seatbelt unfastened (active-LOW)
IGN   = 1   # Ignition ON

# Boolean expression via sum of products (SOP)
# Note: This expression is very inefficient, but works
# (No simplifications applied)
# Students should use this to verify their understanding
# of the logic and for troubleshooting purposes

alarm = (DRIV and not PASS and not BELTD and not BELTP and IGN) or \
        (DRIV and not PASS and not BELTD and BELTP and IGN) or \
        (DRIV and PASS and not BELTD and not BELTP and IGN) or \
        (DRIV and PASS and not BELTD and BELTP and IGN) or \
        (DRIV and PASS and BELTD and not BELTP and IGN)

# Testing the logic
if alarm:
    alarmSignal = 0   # Alarm ON (LOW)
else:
    alarmSignal = 1   # Alarm OFF (HIGH)

# Display the result
print("Alarm signal (0 = ON, 1 = OFF):", alarmSignal)
