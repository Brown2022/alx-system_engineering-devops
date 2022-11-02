<h1>0x17. Web stack debugging #3</h1>
<h2>Tasks</h2>
<h3>0-strace_is_your_friend.pp</h3>
Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

- strace can attach to a current running process
- You can use tmux to run strace in one window and curl in another one
Requirements:

- Your 0-strace_is_your_friend.pp file must contain Puppet code
- You can use whatever Puppet resource type you want for you fix

[web server](https://alx-intranet.hbtn.io/concepts/17)
[wikipedia page about web server](https://en.wikipedia.org/wiki/Web_server)
[web server](https://www.techtarget.com/whatis/definition/Web-server)
[What is a Web Server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)
[web stack debugging](https://alx-intranet.hbtn.io/concepts/68)
[Youtube video First 5 Commands When I Connect on a Linux Server](https://www.youtube.com/watch?v=1_gqlbADaAw)

Web stack debugging
Intro
Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.
[non exhaustive guide to debugging](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/45dffb0b1da8dc2ce47e340d7f88b05652c0f486.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221102T124210Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c13028b8dedd9ee22a0a8c21af4f05c9e5b0bcb30a1bebd6bf890fcae5d80545)

<h2>School specific</h2>

If you are struggling to get something right that is run on the checker, like a Bash script or a piece of code, keep in mind that you can simulate the flow by starting a Docker container with the distribution that is specified in the requirements and by running your code. Check the Docker concept page for more info.

<h3>Test and verify your assumptions</h3>

The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:

- Is the web server started? - You can check using the service manager, also double check by checking process list.
- On what port should it listen? - Check your web server configuration
- Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
- It is listening on the correct server IP? - netstat is also your friend here
- Is there a firewall enabled?
- Have you looked at logs? - usually in /var/log and tail -f is your friend
- Can I connect to the HTTP port from the location I am browsing from? - curl is your friend

There is a good chance that at this point you will already have found part of the issue.

Get a quick overview of the machine state
Youtube video First 5 Commands When I Connect on a Linux Server

When you connect to a server/machine/computer/container you want to understand what’s happened recently and what’s happening now, and you can do this with [5 commands](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/) in a minute or less:

w

- shows server [uptime](https://www.techtarget.com/whatis/definition/uptime-and-downtime) which is the time during which the server has been continuously running
- shows which users are connected to the server
- load average will give you a good sense of the server health - (read more about load [here](https://scoutapm.com/blog/understanding-load-averages)and [here](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html))

<h3>history</h3>

- ows which commands were previously run by the user you are currently connected to
- you can learn a lot about what type of work was previously performed on the machine, and what could have gone wrong with it
- where you might want to start your debugging work

<h3>top</h3>

- shows what is currently running on this server
- order results by CPU, memory utilization and catch the ones that are resource intensive

<h3>df</h3>

- shows disk utilization

<h3>netstat</h3>

- what port and IP your server is listening on
- what processes are using sockets
- try netstat -lpn on a Ubuntu machine

<h3>Machine</h3>

Debugging is pretty much about verifying assumptions, in a perfect world the software or system we are working on would be working perfectly, the server is in perfect shape and everybody is happy. But actually, it NEVER goes this way, things ALWAYS fail (it’s tremendous!).

For the machine level, you want to ask yourself these questions:

- Does the server have free disk space? - df
- Is the server able to keep up with CPU load? - w, top, ps
- Does the server have available memory? free
- Are the server disk(s) able to keep up with read/write IO? - htop

If the answer is no for any of these questions, then that might be the reason why things are not going as expected. There are often 3 ways of solving the issue:

- free up resources (stop process(es) or reduce their resource consumption)
-  ncrease the machine resources (adding memory, CPU, disk space…)
- distributing the resource usage to other machines

<h3>Network issue</h3>

For the machine level, you want to ask yourself these questions:

- Does the server have the expected network interfaces and IPs up and running? ifconfig
- Does the server listen on the sockets that it is supposed to? netstat (netstat -lpd or netstat -lpn)
- Can you connect from the location you want to connect from, to the socket you want to connect to? telnet to the IP + PORT (telnet 8.8.8.8 80)
- Does the server have the correct firewall rules? iptables, ufw:
	- iptables -L
	- sudo ufw status

<h3>Process issue</h3>

If a piece of Software isn’t behaving as expected, it can obviously be because of above reasons… but the good news is that there is more to look into (there is ALWAYS more to look into actually).

- Is the software started? init, init.d:
	- service NAME_OF_THE_SERVICE status
	- /etc/init.d/NAME_OF_THE_SERVICE status
- Is the software process running? pgrep, ps:
	- pgrep -lf NAME_OF_THE_PROCESS
	- ps auxf
- Is there anything interesting in the logs? look for log files in /var/log/ and tail -f is your friend

<h3>Debugging is fun</h3>

Debugging can be frustrating, but it will definitely be part of your job, it requires experience and methodology to become good at it. The good news is that bugs are never going away, and the more experienced you become, trickier bugs will be assigned to you! Good luck :)
