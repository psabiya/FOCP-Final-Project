import sys

def process_line(line):
    parts = line.split(",")
    if len(parts) == 3:
        try:
            cat_type, entry_time, exit_time = parts
            return cat_type, int(entry_time), int(exit_time)
        except ValueError:
            return None

def analyze_log(file_path):
    try:
        with open(file_path, "r") as f:
            cat_visits = intruder_attacks = total_time = 0
            durations = []

            for line in f:
                if line.strip() == "END":
                    break

                data = process_line(line.strip())
                if data:
                    cat_type, entry, exit = data
                    if cat_type == "OURS":
                        cat_visits += 1
                        total_time += exit - entry
                        durations.append(exit - entry)
                    else:
                        intruder_attacks += 1
                        print(f"Intruder detected at {exit}! Sound and water attack initiated.")

            hours, minutes = divmod(total_time, 60)
            average_duration = sum(durations) / len(durations) if durations else 0
            longest_visit = max(durations) if durations else 0
            shortest_visit = min(durations) if durations else 0

            print("Log File Analysis")
            print("==================")
            print(f"Cat Visits: {cat_visits}")
            print(f"Intruder Attacks: {intruder_attacks}")
            print(f"Total Time in House: {hours} Hours, {minutes} Minutes")
            print(f"Average Visit Length: {average_duration} Minutes")
            print(f"Longest Visit: {longest_visit} Minutes")
            print(f"Shortest Visit: {shortest_visit} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        file_path = sys.argv[1]
        analyze_log(file_path)

