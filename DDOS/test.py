# import asyncio
# import aiohttp
# import time
# import statistics

# # ===========================
# # CONFIGURATION
# # ===========================
# TARGET_URL = "www.facebook.com"  # <-- REPLACE ONLY IF YOU OWN THE SERVER
# CONCURRENCY = 200            # number of simultaneous connections
# TOTAL_REQUESTS = 1_000_000    # 1 million requests
# REQUEST_TIMEOUT = 1000         # seconds per request
# # ===========================


# class Stats:
#     def __init__(self):
#         self.latencies = []
#         self.status = {}
#         self.errors = 0

#     def add_success(self, code, t):
#         self.latencies.append(t)
#         self.status[code] = self.status.get(code, 0) + 1

#     def add_error(self):
#         self.errors += 1

#     def report(self):
#         print("\n========== REPORT ==========")
#         print(f"Successful requests: {len(self.latencies)}")
#         print(f"Errors: {self.errors}")
#         print("Status codes:")
#         for s, c in sorted(self.status.items()):
#             print(f"  {s}: {c}")

#         if not self.latencies:
#             print("No successful requests.")
#             return

#         ms = [x * 1000 for x in self.latencies]
#         print(f"Min: {min(ms):.2f} ms")
#         print(f"Max: {max(ms):.2f} ms")
#         print(f"Mean: {statistics.mean(ms):.2f} ms")
#         print(f"Median: {statistics.median(ms):.2f} ms")
#         print(f"90th percentile: {statistics.quantiles(ms, n=10)[8]:.2f} ms")
#         print(f"99th percentile: {statistics.quantiles(ms, n=100)[98]:.2f} ms")


# async def make_request(session, stats):
#     try:
#         start = time.perf_counter()
#         async with session.get(TARGET_URL, timeout=REQUEST_TIMEOUT) as resp:
#             elapsed = time.perf_counter() - start
#             stats.add_success(resp.status, elapsed)
#     except:
#         stats.add_error()


# async def worker(session, stats, sem):
#     global REMAINING
#     while REMAINING > 0:
#         async with sem:
#             REMAINING -= 1
#             await make_request(session, stats)


# async def main():
#     global REMAINING
#     REMAINING = TOTAL_REQUESTS

#     stats = Stats()
#     sem = asyncio.Semaphore(CONCURRENCY)

#     async with aiohttp.ClientSession() as session:
#         tasks = [asyncio.create_task(worker(session, stats, sem)) 
#                  for _ in range(CONCURRENCY)]
#         await asyncio.gather(*tasks)

#     stats.report()


# if __name__ == "__main__":
#     asyncio.run(main())



dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'b': 20, 'c': 30, 'd': 40}
dict_a['Nak']='12'
del dict_a['a']
print(dict_a)
result = {**dict_a, **dict_b}
print(result)   