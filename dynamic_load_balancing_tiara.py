import time
import random

print("=== SIMULASI DYNAMIC LOAD BALANCING ===\n")

# jumlah server
jumlah_server = 4
server = [0] * jumlah_server

# generate task acak
tasks = [random.randint(2, 7) for _ in range(20)]

print("Daftar Task:", tasks)
print("\nProses pembagian tugas:\n")

for i, task in enumerate(tasks):
    # cari server dengan beban paling kecil
    index_server = server.index(min(server))

    print(f"Task ke-{i+1} (beban {task}) -> masuk ke Server {index_server+1}")
    
    # update beban server
    server[index_server] += task
    
    time.sleep(0.2)

print("\n=== HASIL AKHIR ===")
for i, s in enumerate(server):
    print(f"Total beban Server {i+1}: {s}")

# waktu optimal
waktu_optimal = max(server)
print(f"\nWaktu optimal tercapai pada: {waktu_optimal} unit waktu")