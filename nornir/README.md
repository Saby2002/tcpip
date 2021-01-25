# Nornir 
- Pluggable multithread framework with inventory management to help operate collections of deviices. 
- Because it written with Python and meant to be used with Python

# Why Nornir ?
- Order of Magnitude faster than YAML-Based alternative
- Intergated with Python framework like flask, django, click etc
- Earier to extend
- Leverage linters, debuggers and loggers and IDE of python
- Cleaner Logic

# Installation Required 
- pip install nornir


# Three ways to configure Nornir
- (1) With a configuration file
- (2) Directly with a code
- Combination with both 1 and 2 

# Inventory Management
- The inventory is arguably the most important piece of Nornir. Everything revolves around it. 

	- Hosts File
		- Hosts contain a mapping about each existing host, how to connect to them and may also contain to them  and may also contain user defined data. 
		- It also describes group membership and data may be inherited from parent groups or defaults
	- Groups file
		- Similar to hosts
	- Defaults files
		- You can define here default values that will be used when a certain data point is not defined by a host or a host or any of its parents groups.

# Filtering Inventory Hosts
- Nornir doesnt have the concept of "roles" or "classes" or anything like that. 
- Instead it provides different mechanism for you to classify and filter hosts so you can implement the mechanism that fits the workflow better
- The purpose of filtering is to execute at the group of Task. 

	- Three Mechanism to select devices : 
		- Simple Filtering 
		- Advance Filtering
		- Functions

## Simple Filtering 


