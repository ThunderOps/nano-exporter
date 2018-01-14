# Raiblocks Prometheus exporter

To get started install the exporter.

```bash
pip install raiblocks-exporter
```

Then run `raiblocks-exporter` and `curl http://localhost:9410/metrics`.

Additional options can be found under help.

```bash
# raiblocks-exporter --help
usage: raiblocks-exporter [-h] [-l LISTEN] [-n HOST] [-p PORT]

Prometheus exporter for Raiblocks.

optional arguments:
  -h, --help  show this help message and exit
  -l LISTEN   address on which to expose metrics (default ":9410")
  -n HOST     address of Raiblocks server (default "localhost")
  -p PORT     RPC port of Raiblocks server (default "7076")
```

The following metrics are exposed.

```bash
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 289902592.0
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 23498752.0
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1515953669.29
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.51
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 7.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1048576.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="2",minor="7",patchlevel="5",version="2.7.5"} 1.0
# HELP rpc_version Version of RPC
# TYPE rpc_version gauge
rpc_version 1.0
# HELP store_version Version of store
# TYPE store_version gauge
store_version 10.0
# HELP available_supply Available supply
# TYPE available_supply gauge
available_supply 1.33248289219696e+38
# HELP block_count Number of blocks
# TYPE block_count gauge
block_count 4998081.0
# HELP block_count_unchecked Number of unchecked blocks
# TYPE block_count_unchecked gauge
block_count_unchecked 14.0
# HELP block_count_open Number of open blocks
# TYPE block_count_open gauge
block_count_open 317475.0
# HELP block_count_send Number of send blocks
# TYPE block_count_send gauge
block_count_send 2513195.0
# HELP block_count_change Number of change blocks
# TYPE block_count_change gauge
block_count_change 12843.0
# HELP block_count_receive Number of receive blocks
# TYPE block_count_receive gauge
block_count_receive 2154568.0
# HELP frontier_count Number of frontiers
# TYPE frontier_count gauge
frontier_count 317476.0
```