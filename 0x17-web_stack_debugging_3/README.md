test to confirm the error

```
root@818be76fd383:/# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Tue, 07 Nov 2023 15:28:03 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
```

find running processes

```
root@818be76fd383:/# ps -faux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root       601  0.0  0.0  18168  3304 pts/1    Ss   15:21   0:00 /bin/bash
root       658  0.0  0.0  15560  2216 pts/1    R+   15:30   0:00  \_ ps -faux
root       586  0.0  0.0  18168  3312 pts/0    Ss+  15:20   0:00 /bin/bash
root         1  0.0  0.0  17956  2764 ?        Ss   15:19   0:00 /bin/bash ./etc/sandbox_run.sh
root        14  0.0  0.0  61380  5264 ?        S    15:19   0:00 /usr/sbin/sshd -D
root        63  0.0  0.0   4444  1628 ?        S    15:19   0:00 /bin/sh /usr/bin/mysqld_safe
mysql      443  0.0  0.4 574652 67268 ?        Sl   15:19   0:00  \_ /usr/sbin/mysqld --basedir=/usr -root       134  0.0  0.1 276396 21812 ?        Ss   15:19   0:00 /usr/sbin/apache2 -k start
www-data   233  0.0  0.1 278092 18036 ?        S    15:19   0:00  \_ /usr/sbin/apache2 -k start
www-data   621  0.0  0.1 276788 16684 ?        S    15:21   0:00  \_ /usr/sbin/apache2 -k start
```

attatch strace to a running service worker and curl in another terminal

```
root@818be76fd383:/# strace -p 621
Process 621 attached
accept4(3, {sa_family=AF_INET, sin_port=htons(47362), sin_addr=inet_addr("127.0.0.1")}, [16], SOCK_CLOEXEC) = 11
getsockname(11, {sa_family=AF_INET, sin_port=htons(80), sin_addr=inet_addr("127.0.0.1")}, [16]) = 0
fcntl(11, F_GETFL)
```

find the latest process to exit with error

```
stat("/var/www/html/wp-includes/default-filters.php", {st_mode=S_IFREG|0644, st_size=25220, ...}) = 0
stat("/var/www/html/wp-includes/l10n.php", {st_mode=S_IFREG|0644, st_size=43130, ...}) = 0
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7fff9c166c60) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7fff9c166b30) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7fff9c168d60) = -1 ENOENT (No such file or directory)
open("/var/www/html/wp-includes/class-wp-locale.phpp", O_RDONLY) = -1 ENOENT (No such file or directory)
```

locate settings file with the erroneous value

```
root@818be76fd383:/# cd /var/www/html
root@818be76fd383:/var/www/html# ls
index.php        wp-admin              wp-config.php  wp-links-opml.php  wp-settings.php
license.txt      wp-blog-header.php    wp-content     wp-load.php        wp-signup.php
readme.html      wp-comments-post.php  wp-cron.php    wp-login.php       wp-trackback.php
wp-activate.php  wp-config-sample.php  wp-includes    wp-mail.php        xmlrpc.php
root@818be76fd383:/var/www/html# cd wp-includes/
```

backup suspect file and test fix

```
root@818be76fd383:/var/www/html# cp wp-settings.php test
root@818be76fd383:/var/www/html# sed -i 's/phpp/php/g' test
root@818be76fd383:/var/www/html# diff -y test wp-settings.php
```

general fix to correct all instances of the error value on the file

```
root@818be76fd383:/var/www/html# sed -i 's/phpp/php/g' wp-settings.php
```

restart apache2

```
root@818be76fd383:/var/www/html# sudo service apache2 restart
 * Restarting web server apache2                                                                                 [ OK ]
```

test check if the fix worked

```
root@818be76fd383:/var/www/html# curl -sI 127.0.0.1
HTTP/1.1 200 OK
Date: Tue, 07 Nov 2023 15:41:21 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8
```

** all is well **
