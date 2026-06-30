import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("performance_results.csv")

plt.figure(figsize=(6,4))
plt.plot(df["clients"], df["avg_delivery_time_ms"], marker='o')
plt.title("Clients vs Average Delivery Time")
plt.xlabel("Number of Clients")
plt.ylabel("Average Delivery Time (ms)")
plt.grid(True)
plt.savefig("clients_vs_delay.png")
plt.close()

plt.figure(figsize=(6,4))
plt.plot(df["clients"], df["throughput_msgs_per_sec"], marker='o')
plt.title("Clients vs Throughput")
plt.xlabel("Number of Clients")
plt.ylabel("Throughput (msgs/sec)")
plt.grid(True)
plt.savefig("clients_vs_throughput.png")
plt.close()

print("Graphs generated successfully.")
