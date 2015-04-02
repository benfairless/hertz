Database layout
===============

Below is a summary of the database layout

#### Table: monitoring_jobs

| Name       | Type     | Description                                          |
|------------|----------|------------------------------------------------------|
| job_id     | text     | Unique identifier of job                             |
| baseline   | boolean  | Is job set as baseline                               |

##### SQL:
```sql
-- Table: monitoring_jobs

-- DROP TABLE monitoring_jobs;

CREATE TABLE monitoring_jobs
(
  job_id bytea, -- Unique identifier of job
  baseline boolean -- Is job set as baseline?
)
WITH (
  OIDS=FALSE
);
ALTER TABLE monitoring_jobs
  OWNER TO postgres;
COMMENT ON COLUMN monitoring_jobs.job_id IS 'Unique identifier of job';
COMMENT ON COLUMN monitoring_jobs.baseline IS 'Is job set as baseline?';
```

#### Table: monitoring_data_raw

| Name       | Type     | Description                                          |
|------------|----------|------------------------------------------------------|
| job_id     | text     | Unique identifier for job                            |
| hostname   | text     | Hostname of machine                                  |
| timestamp  | datetime | Second-based timestamp for entry                     |
| poll_time  | integer  | Time in seconds the data is aggregated from          |
| mem_swpd   | integer  | Virtual memory used                                  |
| mem_free   | integer  | Idle memory                                          |
| mem_buff   | integer  | Memory used as buffers                               |
| mem_cache  | integer  | Memory used as cache                                 |
| swap_in    | integer  | Memory swapped in per second                         |
| swap_out   | integer  | Memory swapped out per second                        |
| blocks_in  | integer  | Blocks received from block device per second (1024B) |
| blocks_out | integer  | Blocks sent to block device per second (1024B)       |
| cpu_int    | integer  | CPU interrupts per second                            |
| cpu_cs     | integer  | CPU context switches per second                      |
| cpu_usr    | integer  | Time spent running non-kernel code (%)               |
| cpu_sys    | integer  | Time spent running kernel code (%)                   |
| cpu_idle   | integer  | Time spent idle (%)                                  |
| cpu_wait   | integer  | Time spent waiting for IO (%)                        |
| proc_run   | integer  | Number of runnable processes                         |
| proc_blk   | integer  | Number of blocked processes                          |

##### SQL:
```sql
-- Table: monitoring_data

-- DROP TABLE monitoring_data;

CREATE TABLE monitoring_data
(
  job_id bytea,
  mem_swpd bigint DEFAULT 0, -- Virtual memory used (KiB)
  mem_free bigint DEFAULT 0, -- Idle memory (KiB)
  mem_buff bigint DEFAULT 0, -- Memory used as buffers (bytes)
  mem_cache bigint DEFAULT 0, -- Memory used as cache (bytes)
  swap_in bigint DEFAULT 0, -- Memory swapped in (bytes/s)
  swap_out bigint DEFAULT 0, -- Memory swapped out (bytes/s)
  blocks_in bigint DEFAULT 0, -- Data received from block device (KiB/s)
  blocks_out bigint DEFAULT 0, -- Data received from block device (KiB/s)
  cpu_int smallint DEFAULT 0, -- CPU interrupts (interrupts/s)
  cpu_cs smallint DEFAULT 0, -- CPU Context Switches (CS/s)
  cpu_usr numeric(3,0), -- Time spent running non-kernel code (%)
  cpu_sys numeric(3,0), -- Time spent running kernel code (%)
  cpu_idle numeric(3,0), -- Time spent idle (%)
  cpu_wait numeric(3,0), -- Time spent waiting for IO (%)
  proc_run smallint DEFAULT 0, -- Number of runnable processes
  proc_blk smallint DEFAULT 0 -- Number of blocked processes
)
WITH (
  OIDS=FALSE
);
ALTER TABLE monitoring_data
  OWNER TO postgres;
COMMENT ON COLUMN monitoring_data.mem_swpd IS 'Virtual memory used (bytes)';
COMMENT ON COLUMN monitoring_data.mem_free IS 'Idle memory (bytes)';
COMMENT ON COLUMN monitoring_data.mem_buff IS 'Memory used as buffers (bytes)';
COMMENT ON COLUMN monitoring_data.mem_cache IS 'Memory used as cache (bytes)';
COMMENT ON COLUMN monitoring_data.swap_in IS 'Memory swapped in (bytes/s)';
COMMENT ON COLUMN monitoring_data.swap_out IS 'Memory swapped out (bytes/s)';
COMMENT ON COLUMN monitoring_data.blocks_in IS 'Data received from block device (KiB/s)';
COMMENT ON COLUMN monitoring_data.blocks_out IS 'Data received from block device (KiB/s)';
COMMENT ON COLUMN monitoring_data.cpu_int IS 'CPU interrupts (interrupts/s)';
COMMENT ON COLUMN monitoring_data.cpu_cs IS 'CPU Context Switches (CS/s)';
COMMENT ON COLUMN monitoring_data.cpu_usr IS 'Time spent running non-kernel code (%)';
COMMENT ON COLUMN monitoring_data.cpu_sys IS 'Time spent running kernel code (%)';
COMMENT ON COLUMN monitoring_data.cpu_idle IS 'Time spent idle (%)';
COMMENT ON COLUMN monitoring_data.cpu_wait IS 'Time spent waiting for IO (%)';
COMMENT ON COLUMN monitoring_data.proc_run IS 'Number of runnable processes';
COMMENT ON COLUMN monitoring_data.proc_blk IS 'Number of blocked processes';
```
