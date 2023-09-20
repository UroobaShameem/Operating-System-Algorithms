class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_ratio = 0
        self.start_time = 0
        self.end_time = 0

    def calculate_response_ratio(self, total_waiting_time):
        self.response_ratio = (total_waiting_time + self.burst_time) / self.burst_time

def hrrn_scheduling(processes):
    current_time = 0
    total_waiting_time = 0
    completed_processes = []
    gantt_chart = []

    while processes:
        runnable_processes = [p for p in processes if p.arrival_time <= current_time]

        if not runnable_processes:
            current_time += 1
            gantt_chart.append('IDLE')
            continue

        runnable_processes.sort(key=lambda x: x.response_ratio, reverse=True)
        current_process = runnable_processes[0]

        if current_process.burst_time <= 1:
            current_time += 1
            current_process.burst_time -= 1
            current_process.end_time = current_time
            current_process.turnaround_time = current_process.end_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            total_waiting_time += current_process.waiting_time
            completed_processes.append(current_process)
            processes.remove(current_process)
            gantt_chart.append(f'P{current_process.pid}')
        else:
            current_time += 1
            current_process.burst_time -= 1
            gantt_chart.append(f'P{current_process.pid}')

        for p in processes:
            if p in runnable_processes:
                p.calculate_response_ratio(total_waiting_time)

    return completed_processes, gantt_chart

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for Process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for Process {i + 1}: "))
        processes.append(Process(i + 1, arrival_time, burst_time))

    completed_processes, gantt_chart = hrrn_scheduling(processes)

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tStart Time\tEnd Time")
    for process in completed_processes:
        print(
            f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t"
            f"{process.turnaround_time}\t\t{process.start_time}\t\t{process.end_time}"
        )

    avg_waiting_time = sum(process.waiting_time for process in completed_processes) / num_processes
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")

    print("\nGantt Chart:")
    print(" | ".join(gantt_chart))

