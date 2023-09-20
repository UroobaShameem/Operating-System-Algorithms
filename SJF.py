def sjf_scheduling(processes):  #function for Shortest Job First algo implementation
    n = len(processes)  # n= number of processes

    total_waiting_time = 0
    total_turnaround_time = 0

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i, (process_id, burst_time) in enumerate(processes):    #loop that generates index no also for each process id and burst time
        waiting_time = 0    #set waiting time 0 for current process
        for j in range(i):  #loop to calculate wait time for previous processes
            waiting_time += processes[j][1] #add burst time of previous to wait time of current
        turnaround_time = waiting_time + burst_time #turnarount for current process

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        print(f"{process_id}\t{burst_time}\t\t{waiting_time}\t\t{turnaround_time}")

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

    # Generate Gantt Chart
    gantt_chart = ""
    current_time = 0
    for i, (process_id, burst_time) in enumerate(processes):
        waiting_time = 0
        for j in range(i):
            waiting_time += processes[j][1]
        gantt_chart += f"{process_id} | "
        current_time += burst_time + waiting_time

    print("\nGantt Chart:")
    print(gantt_chart[:-2])  # Remove the trailing ' | '

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        process_id = input(f"Enter Process {i + 1} ID: ")
        burst_time = int(input(f"Enter Burst Time for {process_id}: "))
        processes.append((process_id, burst_time))

    # Sort the processes based on burst time while keeping process IDs unchanged
    processes.sort(key=lambda x: x[1])

    sjf_scheduling(processes)
