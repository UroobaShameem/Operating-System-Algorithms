class Process:
    def __init__(self, pid, arrival_time, execution_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.remaining_time = execution_time
        self.finish_time = 0


def round_robin(processes, quantum_size):
    current_time = 0
    ready_queue = processes.copy()
    finished_processes = []

    while ready_queue:
        current_process = ready_queue.pop(0)

        if current_process.remaining_time <= quantum_size:
            print(f"Running Process {current_process.pid}")
            current_time += current_process.remaining_time
            current_process.remaining_time = 0
            current_process.finish_time = current_time
            finished_processes.append(current_process)
            print(f"Process {current_process.pid} finished at time {current_time}")
        else:
            print(f"Running Process {current_process.pid}")
            current_time += quantum_size
            current_process.remaining_time -= quantum_size
            print(f"Process {current_process.pid} paused after {quantum_size} time units")

        if ready_queue:
            next_process = ready_queue[0]
            if next_process.arrival_time > current_time:
                print(f"Waiting for new process at time {current_time}")
                current_time = next_process.arrival_time

        if current_process.remaining_time > 0:
            print(f"Resuming Process {current_process.pid}")
            ready_queue.append(current_process)

    calculate_metrics(finished_processes)


def calculate_metrics(processes):
    total_turnaround_time = 0
    total_utilization_time = 0

    for process in processes:
        process.turnaround_time = process.finish_time - process.arrival_time
        process.utilization_time = process.execution_time - process.remaining_time

        total_turnaround_time += process.turnaround_time
        total_utilization_time += process.utilization_time

    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_utilization_time = total_utilization_time / len(processes)

    print("\nMetrics:\n")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Average Utilization Time: {avg_utilization_time}")

    Process.avg_turnaround_time = avg_turnaround_time
    Process.avg_utilization_time = avg_utilization_time



def main():
    num_processes = int(input("How many processes do you want to create (3-5): "))
    if num_processes < 3 or num_processes > 5:
        print("Number of processes must be between 3 and 5.")
        return

    processes = []
    for pid in range(1, num_processes + 1):
        if pid == 1:
            arrival_time = 0
            print("Arrival time of Process 1 is 0")
        else:
            arrival_time = int(input(f"Enter arrival time for Process {pid}: "))

        execution_time = int(input(f"Enter execution time for Process {pid} between (1-10) : "))
        execution_time = min(10, execution_time)

        processes.append(Process(pid, arrival_time, execution_time))

    quantum_size = int(input("Enter quantum size between 1-3 : "))
    quantum_size = min(3, quantum_size)

    round_robin(processes, quantum_size)

    # Display process details
    print("\nProcess Control Information:\n")
    print("Quantum Size: \n", quantum_size)
    for process in processes:
        print(f"Process ID: {process.pid}")
        print(f"Execution Time: {process.execution_time}")
        print(f"Turnaround Time: {process.turnaround_time}")
        print(f"Utilization Time: {process.utilization_time}")
        print(f"Finish Time: {process.finish_time}\n")

    print("Average Turnaround Time: ", process.avg_turnaround_time)
    print("Average Utilization Time: ", process.avg_utilization_time)


if __name__ == "__main__":
    main()
