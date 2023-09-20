import random
from collections import deque

def create_process(process_num):
    process = {}
    process['Process No.'] = process_num
    T = int(input(f"Enter total time for process {process_num}: "))
    process['Execution Time'] = T
    process['Executed Time'] = 0
    process['Instruction Address'] = [random.randint(process_num * 1000, 1000 + process_num * 1000) for _ in range(T)]
    
    R = input(f"Enter resource name for process {process_num} (or 0 if no resource): ")
    process['Resource Name'] = R if R != '0' else ''
    
    if process['Resource Name'] != '':
        P = int(input(f"Enter position for resource {process_num}: "))
        process['Resource Position'] = P
    
    return process

def print_process_state(process, time, quantum):
    print(f"Time Period: {time}")
    print(f"Running Time: {process['Executed Time']}")
    print(f"Execution Time: {process['Execution Time']}")
    
    if process['Executed Time'] < len(process['Instruction Address']):
        print(f"Instruction Address: {process['Instruction Address'][process['Executed Time']]}")
    else:
        print("All instructions executed.")
    
    print(f"Unique ID: p{process['Process No.']}")
    print(f"Arrival Time: {time + 1}")
    print(f"Blocked State: {'Blocked' if process['Blocked State'] else 'Not Blocked'}")
    
    if process['Executed Time'] == process.get('Resource Position'):
        print(f"Resource Name: {process.get('Resource Name')}")
        
    print(f"Running State: {'Running' if process['Running State'] else 'Not Running'}")
    print(f"Continue Time: {quantum}")
    print("=" * 30)


def main():
    n = int(input("Enter the number of processes: "))
    q = int(input("Enter quantum no.: "))
    processes = [create_process(i + 1) for i in range(n)]

    total_execution_time = sum(p['Execution Time'] for p in processes)
    process_queue = deque(processes)

    current_time = 0
    resource_blocked = False
    resource_blocked_process = None
    resource_blocked_remaining_quantums = 3

    while total_execution_time > 0:
        if process_queue:
            current_process = process_queue.popleft()

            if current_process['Resource Name'] != '':
                resource_blocked = True
                resource_blocked_process = current_process['Resource Name']

            if current_process['Execution Time'] > 0:
                print(f"Executing Process {current_process['Process No.']}:")
                for _ in range(q):
                    if current_process['Execution Time'] > 0:
                        current_process['Execution Time'] -= 1
                        total_execution_time -= 1
                        current_process['Executed Time'] += 1
                        
                        if resource_blocked and current_process['Resource Name'] == resource_blocked_process and current_process['Executed Time'] == current_process.get('Resource Position'):
                            if resource_blocked_remaining_quantums > 0:
                                resource_blocked_remaining_quantums -= 1
                                current_process['Blocked State'] = True
                                current_process['Running State'] = False
                            else:
                                resource_blocked_process = None
                                resource_blocked = False
                                resource_blocked_remaining_quantums = 3
                                current_process['Blocked State'] = False
                                current_process['Running State'] = True
                        else:
                            current_process['Blocked State'] = False
                            current_process['Running State'] = True

                        print_process_state(current_process, current_time + 1, q - 1)

                        current_time += 1

                        if current_process['Execution Time'] == 0:
                            print(f"Process No.: p{current_process['Process No.']} completed!!")
                        else:
                            print(f"Next Instruction: {current_process['Instruction Address'][current_process['Executed Time']]}")
                        print("=" * 30)

                        if current_process['Execution Time'] > 0:
                            process_queue.append(current_process)

    print("All processes have completed.")

if __name__ == "__main__":
    main()
