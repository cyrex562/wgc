# wg and wg-quick notes

## wg command

### wg show/show all/show {interface}

```
interface: wg0
  public key: MjcAYLV8clQ3Ne0MvJOmYe/vuifWL6zl3bZB3j5kM0Y=
  private key: (hidden)
  listening port: 51820

peer: DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=
  endpoint: 141.156.187.31:51820
  allowed ips: 10.70.0.10/32, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24, 192.168.5.0/24, 192.168.100.0/29
  latest handshake: 1 minute, 22 seconds ago
  transfer: 4.28 GiB received, 400.60 MiB sent

peer: KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=
  endpoint: 138.88.198.140:51820
  allowed ips: 10.70.0.3/32, 10.10.0.0/30, 10.30.0.0/30
  latest handshake: 1 minute, 50 seconds ago
  transfer: 353.88 MiB received, 4.26 GiB sent

peer: ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=
  endpoint: 172.108.148.130:51820
  allowed ips: 10.70.0.11/32
  latest handshake: 21 hours, 14 minutes, 22 seconds ago
  transfer: 47.59 MiB received, 18.99 MiB sent

peer: PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=
  allowed ips: 10.70.0.4/32

peer: 2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=
  allowed ips: 10.70.0.5/32

peer: UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=
  allowed ips: 10.70.0.6/32

peer: EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=
  allowed ips: 10.70.0.7/32

peer: zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=
  allowed ips: 10.70.0.8/32

peer: mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=
  allowed ips: 10.70.0.9/32
```  
  
### wg show interfaces
 
```
wg0
```
 
### wg show all public-key
 
```
wg0     MjcAYLV8clQ3Ne0MvJOmYe/vuifWL6zl3bZB3j5kM0Y=
```
 
### wg show {interface} public-key
 
```
MjcAYLV8clQ3Ne0MvJOmYe/vuifWL6zl3bZB3j5kM0Y=
```
 
### wg show all private-key
 
```
wg0     0M65FdUSXxhukM1OkSa4qhIvXGmaEOnD1mgrx5KBJ2w=
```
 
### wg show {interface} private-key
 
```
0M65FdUSXxhukM1OkSa4qhIvXGmaEOnD1mgrx5KBJ2w=
```
 
### wg show all listen-port
 
```
 wg0     51820
```
 
### wg show {interface} listen-port
 
```
51820
```
 
### wg show all fwmark 
 
```
wg0     off
```
 
### wg show {interface} fwmark
 
```
off
```
 
### wg show all peers
 
```
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=
wg0     PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=
wg0     2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=
wg0     UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=
wg0     EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=
wg0     zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=
wg0     mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=
wg0     DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=
wg0     ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=
```
 
### wg show {interface} peers
 
```
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=
```

### wg show all preshared-keys

```
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    (none)
wg0     PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    (none)
wg0     2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    (none)
wg0     UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    (none)
wg0     EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    (none)
wg0     zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    (none)
wg0     mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    (none)
wg0     DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    (none)
wg0     ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    (none)
```

### wg show {interface} preshared-keys

```
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    (none)
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    (none)
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    (none)
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    (none)
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    (none)
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    (none)
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    (none)
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    (none)
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    (none)
```

### wg show all endpoints

```
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    138.88.198.140:51820
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    (none)
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    (none)
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    (none)
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    (none)
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    (none)
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    (none)
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    141.156.187.31:51820
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    172.108.148.130:51820
```

### wg show wg0 endpoints

```
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    138.88.198.140:51820
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    (none)
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    (none)
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    (none)
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    (none)
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    (none)
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    (none)
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    141.156.187.31:51820
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    172.108.148.130:51820
```

### wg show all allowed-ips

```
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    10.70.0.3/32 10.10.0.0/30 10.30.0.0/30
wg0     PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    10.70.0.4/32
wg0     2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    10.70.0.5/32
wg0     UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    10.70.0.6/32
wg0     EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    10.70.0.7/32
wg0     zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    10.70.0.8/32
wg0     mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    10.70.0.9/32
wg0     DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    10.70.0.10/32 192.168.1.0/24 192.168.2.0/24 192.168.3.0/24 192.168.5.0/24 192.168.100.0/29
wg0     ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    10.70.0.11/32
```

### wg show wg0 allowed-ips

```
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    10.70.0.3/32 10.10.0.0/30 10.30.0.0/30
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    10.70.0.4/32
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    10.70.0.5/32
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    10.70.0.6/32
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    10.70.0.7/32
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    10.70.0.8/32
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    10.70.0.9/32
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    10.70.0.10/32 192.168.1.0/24 192.168.2.0/24 192.168.3.0/24 192.168.5.0/24 192.168.100.0/29
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    10.70.0.11/32
```

### wg show all latest-handshakes

```
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    1718827837
wg0     PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    0
wg0     2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    0
wg0     UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    0
wg0     EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    0
wg0     zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    0
wg0     mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    0
wg0     DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    1718827868
wg0     ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    1718749444
```

### wg show wg0 latest-handshakes

```
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    1718827957
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    0
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    0
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    0
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    0
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    0
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    0
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    1718827868
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    1718749444
```

### wg show all transfer

```
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    371731450       4579034110
wg0     PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    0       0
wg0     2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    0       0
wg0     UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    0       0
wg0     EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    0       0
wg0     zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    0       0
wg0     mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    0       0
wg0     DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    4598532418      420706072
wg0     ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    49906342        19913310
```

### wg show wg0 transfer

```
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    371740186       4579071036
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    0       0
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    0       0
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    0       0
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    0       0
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    0       0
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    0       0
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    4598569344      420714808
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    49906342        19913310
```

### wg show all persistent-keepalive

```
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    off
wg0     PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    off
wg0     2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    off
wg0     UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    off
wg0     EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    off
wg0     zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    off
wg0     mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    off
wg0     DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    off
wg0     ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    off
```

### wg show wg0 persistent-keepalive

```
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    off
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    off
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    off
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    off
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    off
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    off
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    off
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    off
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    off
```

### wg show all dump

```
wg0     0M65FdUSXxhukM1OkSa4qhIvXGmaEOnD1mgrx5KBJ2w=    MjcAYLV8clQ3Ne0MvJOmYe/vuifWL6zl3bZB3j5kM0Y=     51820   off
wg0     KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    (none)  138.88.198.140:51820    10.70.0.3/32,10.10.0.0/30,10.30.0.0/30   1718828197      371797250       4579213182      off
wg0     PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    (none)  (none)  10.70.0.4/32    0       00       off
wg0     2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    (none)  (none)  10.70.0.5/32    0       00       off
wg0     UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    (none)  (none)  10.70.0.6/32    0       00       off
wg0     EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    (none)  (none)  10.70.0.7/32    0       00       off
wg0     zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    (none)  (none)  10.70.0.8/32    0       00       off
wg0     mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    (none)  (none)  10.70.0.9/32    0       00       off
wg0     DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    (none)  141.156.187.31:51820    10.70.0.10/32,192.168.1.0/24,192.168.2.0/24,192.168.3.0/24,192.168.5.0/24,192.168.100.0/29       1718828229       4598711282      420771312       off
wg0     ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    (none)  172.108.148.130:51820   10.70.0.11/32    1718749444      49906342        19913310        off
```

### wg show wg0 dump

```
0M65FdUSXxhukM1OkSa4qhIvXGmaEOnD1mgrx5KBJ2w=    MjcAYLV8clQ3Ne0MvJOmYe/vuifWL6zl3bZB3j5kM0Y=    51820    off
KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=    (none)  138.88.198.140:51820    10.70.0.3/32,10.10.0.0/30,10.30.0.0/30   1718828197      371814946       4579259260      off
PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=    (none)  (none)  10.70.0.4/32    0       0       0off
2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=    (none)  (none)  10.70.0.5/32    0       0       0off
UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=    (none)  (none)  10.70.0.6/32    0       0       0off
EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=    (none)  (none)  10.70.0.7/32    0       0       0off
zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=    (none)  (none)  10.70.0.8/32    0       0       0off
mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=    (none)  (none)  10.70.0.9/32    0       0       0off
DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=    (none)  141.156.187.31:51820    10.70.0.10/32,192.168.1.0/24,192.168.2.0/24,192.168.3.0/24,192.168.5.0/24,192.168.100.0/29       1718828229      4598757232       420788880       off
ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=    (none)  172.108.148.130:51820   10.70.0.11/32   1718749444       49906342        19913310        off
```

### wg showconf wg0

```
[Interface]
ListenPort = 51820
PrivateKey = 0M65FdUSXxhukM1OkSa4qhIvXGmaEOnD1mgrx5KBJ2w=

[Peer]
PublicKey = KCtqXJ0SefRXZcz7wn2/uIBLNZLru/jOXF4yRzkQ0mU=
AllowedIPs = 10.70.0.3/32, 10.10.0.0/30, 10.30.0.0/30
Endpoint = 138.88.198.140:51820

[Peer]
PublicKey = PwmuaCg+V4AbTVGPam3I+leFI7GN8XcoQOsEqmB69FU=
AllowedIPs = 10.70.0.4/32

[Peer]
PublicKey = 2UmfXWDyoleJxGXOByquXmX4xaIPZzoYshJ3X7p8YmQ=
AllowedIPs = 10.70.0.5/32

[Peer]
PublicKey = UD9BrdlnAtEbvrXqopqQUEG6V14erCPgIjAnJJkyWzQ=
AllowedIPs = 10.70.0.6/32

[Peer]
PublicKey = EHurrtk54nIuY2nFGrEQd0DUExtmHaRnTIcNHPYXVVw=
AllowedIPs = 10.70.0.7/32

[Peer]
PublicKey = zw303sVkcE9xZ4yWE4cB7rXRSxkJtY501xFSK+18hTk=
AllowedIPs = 10.70.0.8/32

[Peer]
PublicKey = mKo2UwmYZAU0LzEm7AQqc6jvIr9PwAy2heMcIzdcIA0=
AllowedIPs = 10.70.0.9/32

[Peer]
PublicKey = DEkrDbhUEvxLBtZTK7kNgL//WgB1gBM4N//7wejEWFo=
AllowedIPs = 10.70.0.10/32, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24, 192.168.5.0/24, 192.168.100.0/29
Endpoint = 141.156.187.31:51820

[Peer]
PublicKey = ZOZC+ZpQez60NSU+Xl8n7F9Yd2P9W7YDmlu8WDSu7EI=
AllowedIPs = 10.70.0.11/32
Endpoint = 172.108.148.130:51820
```

### wg genpsk

`BSx4BJwO2RuIs1DwUgZqVaW9SPFTJdkgUXFe0vclCuc=`

### wg genkey

`mBOzQx+vBucfVvOTU1EUIeEJpMV0ief+qWzQ4IRub18=`

### wg set --help

```
Usage: wg set <interface> [listen-port <port>] [fwmark <mark>] [private-key <file path>] [peer <base64 public key> [remove] [preshared-key <file path>] [endpoint <ip>:<port>] [persistent-keepalive <interval seconds>] [allowed-ips <ip1>/<cidr1>[,<ip2>/<cidr2>]...] ]...
```

* set configuration values for specified interface

### wg setconf --help

```
Usage: wg setconf <interface> <configuration filename>
```

* sets <interface> configuration of interface to the contents of <configuration fillename>

### wg addconf --help

```
Usage: wg addconf <interface> <configuration filename>
```

* appends the contents of <configuration file> to the interface <interface>

### wg syncconf

```
wg syncconf <interface> <configuration-filename> 
```

* reads back the existing configuration first and only makes changes that are different between the configuration file and the interface

## wg-compatible configuration file format

* Interface section
	* PrivateKey - base64 private key
	* ListenPort - 16-bit port for listening; if not speicfied, chosen randomly
	* FwMark - a 32-bit fwmark for outgoing packets; disabled if set to 0, "off", or not specified
* Peer Section
	* PublicKey - a base64 public key calculated by wg pubkey from a private key
	* PresharedKey - a base64 preshared key generated by wg genpsk. optional. adds additional layer of symmetric-key cryptography for post-quantum resistance
	* AllowedIPs - a comma-separated list of IPv4 and IPv6 addresses with CIDR masks from which incoming traffic for this peer is allowed. can be specified multiple times
	* Endpoint - an endpoint IP or hostname followed by a colon and then a port number. 
	* PersistentKeepalive - a seconds interval between 1 and 65535 of how often to send authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid.

## wg-quick

### wg-quick up | down | save | strip <CONFIG_FILE | INTERFACE>

* use up to add and set up an interface
	* adds a wireguard interface
	* brings up the itnerface with the supplied IP addresses, sets up MTU and routes, and optionally runs pre/post up scripts
* use down to tear down and remove an interface
	* optionally saves the current configuration
	* removes the interface
	* optionally runs pre/post down scripts
* save
	* saves the configuration of an existing interface without bringing the interface down
* strip
	* output a configuration file with all wg-quick-specific options removed

## wg-quick-compatible configuration file format

* interface
	* Address - a comma-separated list of IPv4/IPv6 addresses
	* DNS - comma-separated liist of IPv4/IPv6 addresses to be set as the interface's DNS servers, or non-IP hostnames to be set as the interface's DNS search domains
		* up: runs resolvconf -a tun.INTERFACE -m 0 -x
		* down: runs resolvconf -d tun.INTERFACE
	* MTU - mtu for the interface; automatically determined if not set
	* Table - which routing table rotues are added to
	* PreUp, PostUp, PreDown, PostDown - script snippets which will be executed by bash(1)
		* special string '%i' is expanded to INTERFACE. May be specified multiple types. executed in order
	* SaveConfig - if set to 'true' the configuration is saved from the current state of the interface upon shutdown
