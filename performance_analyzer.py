#!/usr/bin/env python3
import re
from collections import defaultdict
import argparse

def parse_log(logfile):
    total_cycles = 0
    opcode_counts = defaultdict(int)
    stall_cycles = 0

    with open(logfile, 'r') as f:
        for line in f:
            line = line.strip()

            # Cycle counter
            cycle_match = re.search(r"cycle\s+(\d+)", line)
            if cycle_match:
                total_cycles = max(total_cycles, int(cycle_match.group(1)))

            # Stall
            if "STALL" in line.upper():
                stall_cycles += 1
                continue

            # Instruction
            op_match = re.search(r"\]\s*([A-Z0-9_]+)\s+executed", line)
            if op_match:
                opcode = op_match.group(1).upper()
                opcode_counts[opcode] += 1

    return total_cycles, opcode_counts, stall_cycles

def compute_metrics(total_cycles, opcode_counts, stall_cycles, freq):
    total_instructions = sum(opcode_counts.values())
    cpi = total_cycles / total_instructions if total_instructions > 0 else 0
    ipc = total_instructions / total_cycles if total_cycles > 0 else 0
    exec_time = total_cycles / (freq * 1e9)
    return cpi, ipc, exec_time, total_instructions

def report(total_cycles, opcode_counts, stall_cycles, cpi, ipc, exec_time):
    print("----- CPU PERFORMANCE REPORT -----")
    print(f"Total Cycles           : {total_cycles}")
    print(f"Total Instructions     : {sum(opcode_counts.values())}")
    print(f"Stall Cycles           : {stall_cycles}")
    print(f"Average CPI            : {cpi:.3f}")
    print(f"Average IPC            : {ipc:.3f}")
    print(f"Execution Time (sec)   : {exec_time:.9f}")
    print("\nInstruction Breakdown:")
    for op, count in sorted(opcode_counts.items(), key=lambda x: -x[1]):
        print(f"  {op:8} : {count}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("logfile")
    parser.add_argument("--clock", type=float, default=1.0, help="Clock frequency in GHz")
    args = parser.parse_args()

    total_cycles, opcode_counts, stall_cycles = parse_log(args.logfile)
    cpi, ipc, exec_time, total_inst = compute_metrics(
        total_cycles, opcode_counts, stall_cycles, args.clock
    )
    report(total_cycles, opcode_counts, stall_cycles, cpi, ipc, exec_time)

if __name__ == "__main__":
    main()

