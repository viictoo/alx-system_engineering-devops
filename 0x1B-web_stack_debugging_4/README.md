run test 735 fails

``` ab -c 100 -n 2000 localhost/```
``` root@78b29b1aff62:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   3.094 seconds
Complete requests:      2000
Failed requests:        735
   (Connect: 0, Receive: 0, Length: 735, Exceptions: 0)
Non-2xx responses:      1265
Total transferred:      1096270 bytes
HTML transferred:       704085 bytes
Requests per second:    646.32 [#/sec] (mean)
Time per request:       154.723 [ms] (mean)
Time per request:       1.547 [ms] (mean, across all concurrent requests)
Transfer rate:          345.97 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   4.6      0      94
Processing:     1  152  50.7    192     295
Waiting:        1  152  50.8    192     295
Total:          3  153  50.6    192     295

Percentage of the requests served within a certain time (ms)
  50%    192
  66%    197
  75%    198
  80%    199
  90%    200
  95%    200
  98%    201
  99%    202
 100%    295 (longest request) ```

nginx logs - too many open files
``` cat /var/log/nginx/error.log ```
``` 2023/11/14 16:44:30 [emerg] 36#0: epoll_create() failed (24: Too many open files)
2023/11/14 16:44:30 [alert] 31#0: worker process 36 exited with fatal code 2 and cannot be respawned
2023/11/14 16:45:32 [crit] 32#0: accept4() failed (24: Too many open files)
2023/11/14 16:45:32 [crit] 32#0: *1 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files), client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
2023/11/14 16:45:32 [crit] 32#0: accept4() failed (24: Too many open files) ```


nginx ulimit using pid
```
root@78b29b1aff62:/# ps aux | grep nginx
root        31  0.0  0.0  85912  2816 ?        Ss   16:44   0:00 nginx: master process /usr/sbin/ngin
www-data    32  0.0  0.0  86256  3604 ?        S    16:44   0:00 nginx: worker process
www-data    33  0.0  0.0  86256  3604 ?        S    16:44   0:00 nginx: worker process
www-data    34  0.0  0.0  86256  3604 ?        S    16:44   0:00 nginx: worker process
root        70  0.0  0.0   8876   792 pts/0    S+   16:53   0:00 grep --color=auto nginx
```

```  root@78b29b1aff62:/# cat /proc/31/limits
Limit                     Soft Limit           Hard Limit           Units
Max cpu time              unlimited            unlimited            seconds
Max file size             unlimited            unlimited            bytes
Max data size             unlimited            unlimited            bytes
Max stack size            8388608              unlimited            bytes
Max core file size        unlimited            unlimited            bytes
Max resident set          unlimited            unlimited            bytes
Max processes             unlimited            unlimited            processe
Max open files            15                   15                   files
Max locked memory         67108864             67108864             bytes
Max address space         unlimited            unlimited            bytes
Max file locks            unlimited            unlimited            locks
Max pending signals       62760                62760                signals
Max msgqueue size         819200               819200               bytes
Max nice priority         0                    0
Max realtime priority     0                    0
Max realtime timeout      unlimited            unlimited            us ```

ulimit location
``` root@78b29b1aff62:/# grep -rH "ulimit" /etc/
/etc/default/nginx:# Set the ulimit variable if you need defaults to change.
/etc/init.d/nginx:      # Set the ulimits
/etc/init.d/nginx:      ulimit $ULIMIT ```

check and change ulimit to max and restart
```  root@78b29b1aff62:/# vi /etc/init.d/nginx
root@78b29b1aff62:/# sudo service nginx restart
 * Restarting nginx nginx                                                                      [ OK ]
root@78b29b1aff62:/# ulimit -a
core file size          (blocks, -c) unlimited
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 62760
max locked memory       (kbytes, -l) 65536
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1048576
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 8192
cpu time               (seconds, -t) unlimited
max user processes              (-u) unlimited
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited  ```


test with 200k requests - no failures
``` root@78b29b1aff62:/# ab -c 100 -n 200000 localhost/

Completed 200000 requests
Finished 200000 requests

Concurrency Level:      100
Time taken for tests:   262.736 seconds
Complete requests:      200000
Failed requests:        0
Total transferred:      170600000 bytes
HTML transferred:       122400000 bytes
Requests per second:    761.22 [#/sec] (mean)
Time per request:       131.368 [ms] (mean)
Time per request:       1.314 [ms] (mean, across all concurrent requests)
Transfer rate:          634.10 [Kbytes/sec] received
  ```

** ALL IS WELL **
