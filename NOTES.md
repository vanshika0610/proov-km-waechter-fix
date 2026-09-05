# What I checked, and what the agent got wrong

## What the agent got wrong
The agent initially described the missing-reading fallback as defaulting to 0 km,
which would have left the original bug in place for high-odometer cars. I caught
that the correct fallback is the car's own odometer value (meaning 0 km since
last service), not 0. I also verified the km-to-miles fix made arithmetic sense
— dividing by 1.60934 rather than multiplying.

## What I checked before I accepted its work
I ran `py verify.py` after each fix and confirmed all code checks passed.
I also read km_wachter.py directly to confirm SERVICE_INTERVAL_KM is still 15000
and WARN_AT_PERCENT is still 80, and checked settings.cfg to make sure both values
match.

## What the data actually said
Total mileage and age looked like the obvious predictors but turned out to be
noise — correlation ~0.002 and ~0.001 respectively. The actual predictors were
km_since_service (r=0.40), avg_daily_km (r=0.25), and load_factor (r=0.22).
Cars with high scores had a 38% breakdown rate vs 5% for low-score cars, a 7x
separation. Four cars in the top-10 risk list had not yet been flagged by the
80% km rule.