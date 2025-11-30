# cpu-performance-analyzer
Python tool for cycle-level CPU performance calculation: CPI, IPC, stall analysis, and execution-time estimation.

# CPU Performance Analyzer

A lightweight Python tool that parses CPU execution logs and computes key performance metrics such as CPI, IPC, stall cycles, and execution time.

---

##  Core Performance Definitions

### **Instruction**
An operation executed by the CPU (e.g., ADD, LOAD, MUL).

### **Cycle**
A single tick of the CPU clock. More cycles = more time consumed.

### **Stall**
A cycle where no useful instruction is executed.  
Typically caused by dependencies, pipeline hazards, or memory delays.

### **CPI — Cycles Per Instruction**
Average number of cycles required per instruction.

