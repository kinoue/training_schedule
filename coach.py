def marathon_training_schedule(target_minutes, weeks_to_train, unit):
    distance = 42.195 if unit == 'km' else 26.2
    target_pace = target_minutes / distance

    # Starting paces and mileage
    long_run_pace = target_pace * 1.2
    tempo_run_pace = target_pace * 1.1
    easy_run_pace = target_pace * 1.15
    weekly_mileage = 20  # Example starting point

    pace_improvement_rate = 0.01  # Weekly improvement rate

    # Initialize the full training schedule
    full_schedule = []

    for week in range(1, weeks_to_train + 1):
        # Analyze last week's training if not the first week
        if week > 1:
            weekly_mileage *= 1.10

        # Generate training schedule for the current week
        week_schedule = {
            'Long Run': (weekly_mileage * 0.35, long_run_pace),
            'Tempo Run': (weekly_mileage * 0.20, tempo_run_pace),
            'Easy Runs': (weekly_mileage - (weekly_mileage * 0.35 + weekly_mileage * 0.20), easy_run_pace)
        }

        # Update paces for next week
        long_run_pace -= long_run_pace * pace_improvement_rate
        tempo_run_pace -= tempo_run_pace * pace_improvement_rate
        easy_run_pace -= easy_run_pace * pace_improvement_rate

        # Add the week's schedule to the full training schedule
        full_schedule.append(week_schedule)

    return full_schedule