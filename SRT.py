class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def srt_scheduling(processes):
    current_time = 0
    completed_processes = []
    remaining_processes = list(processes)
    gantt_chart = []

    while remaining_processes:
        runnable_processes = [p for p in remaining_processes if p.arrival_time <= current_time]

        if not runnable_processes:
            current_time += 1
            gantt_chart.append('IDLE')
            continue

        shortest_process = min(runnable_processes, key=lambda x: x.remaining_time)

        if shortest_process.remaining_time == shortest_process.burst_time:
            shortest_process.start_time = current_time

        shortest_process.remaining_time -= 1
        current_time += 1
        gantt_chart.append(f'P{shortest_process.pid}')

        if shortest_process.remaining_time == 0:
            shortest_process.completion_time = current_time
            shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time
            shortest_process.waiting_time = shortest_process.turnaround_time - shortest_process.burst_time
            completed_processes.append(shortest_process)
            remaining_processes.remove(shortest_process)

    return completed_processes, gantt_chart

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for Process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        processes.append(Process(i + 1, arrival_time, burst_time))

    completed_processes, gantt_chart = srt_scheduling(processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tStart Time\tCompletion Time")
    for process in completed_processes:
        print(
            f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t"
            f"{process.turnaround_time}\t\t{process.start_time}\t\t{process.completion_time}"
        )

    avg_waiting_time = sum(process.waiting_time for process in completed_processes) / num_processes
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")

    print("\nGantt Chart:")
    print(" | ".join(gantt_chart))
