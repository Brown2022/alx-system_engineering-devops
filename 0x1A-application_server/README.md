<h1>0x1A. Application server</h1>
<h2>Task</h2>
<a href="https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04">How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04</a>
<a href="https://docs.gunicorn.org/en/latest/run.html">Running Gunicorn</a>
<a href="https://werkzeug.palletsprojects.com/en/0.14.x/routing/">Be careful with the way Flask manages slash</a>
<a href="https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.route">route</a>
<a href="https://upstart.ubuntu.com/cookbook/">Upstart documentation</a>
<a href=""></a>
<a href=""></a>
<a href=""></a>
<a href="https://en.wikipedia.org/wiki/Web_server">webserver</a>
<a href="https://www.techtarget.com/whatis/definition/Web-server">web server</a>
<a href="https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server">What is a web server</a>
<a href="https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement">
Server</a>
<a href="https://www.youtube.com/watch?v=B1ANfsDyjeA"</a>
<a href="https://www.youtube.com/watch?v=iuqXFC_qIvA&t=33s"</a>
<a href="https://www.youtube.com/watch?v=1_gqlbADaAw"</a>
<a href="https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/"</a>
<a href="https://www.techtarget.com/whatis/definition/uptime-and-downtime">uptime</a>
<a href="https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes">child process</a>
<a href="https://www.gnu.org/software/libc/manual/html_node/Running-a-Command.html">Running a Command</a>
<a href="https://www.youtube.com/watch?v=AZg4uJkEa-4">web server</a>
<a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works">>How the web works</a>
<a href="https://en.wikipedia.org/wiki/Nginx">Nginx</a>
<a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04">How To Set Up Nginx Server Blocks (Virtual Hosts) on Ubuntu 16.04</a>
<a href="https://landingi.com/help/domains-vs-subdomains/">root and subdomain</a>
<a href="https://www.tutorialspoint.com/http/http_methods.htm">http requests</a>
<a href="https://moz.com/learn/seo/redirection">HTTP redirection</a>
<a href="https://en.wikipedia.org/wiki/HTTP_404">Not found HTTP response code</a>
<a href="https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/">Logs files on Linux</a>
reference
<a href="https://datatracker.ietf.org/doc/html/rfc7231">RFC 7231 (HTTP/1.1)</a>
<a href="https://datatracker.ietf.org/doc/html/rfc7540">RFC 7540 (HTTP/2)</a>

<h3>0. Set up development with Python</h3>

Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

<strong>Requirements:</strong>

- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
- Git clone your AirBnB_clone_v2 on your web-01 server.
- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
- Your Flask application object must be named app (This will allow us to run and check your code).

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```
<h3>1. Set up production with Gunicorn</h3>

Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a <a href="https://www.fullstackpython.com/wsgi-servers.html">WSGI</a> entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

Requirements:

- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called app. (This will allow us to run and check your code)
- You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.
- In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.

Terminal 1:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598
```
Terminal 2:

```bash
ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
```

<strong>2. Serve a page with Nginx</strong>
<h3>2-app_server-nginx_config</h3>

Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/

Requirements:

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.
- Include your Nginx config file as 2-app_server-nginx_config.
Notes:

- In order to test this you’ll have to spin up either your production or development application server (listening on port 5000)
- In an actual production environment the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.
- You will probably need to reboot your server (by using the command $ sudo reboot) to have Nginx publicly accessible

<strong>Example:</strong>

<h2>On my server:</h2>
Window 1:

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029
```

<h3>Window 2:</h3>

```bash
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

<h2>On my local terminal:</h2>

```bash
vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$
```

<strong>3. Add a route with query parameters</strong>
<h3>3-app_server-nginx_config</h3>

Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n> should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting Nginx configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of Gunicorn without having multiple terminals open, see tips below.

Requirements:

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) the process listening on port 5001.
- Include your Nginx config file as 3-app_server-nginx_config.
Tips:

- Check out these articles/docs for clues on how to configure Nginx: <a href="https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms#matching-location-blocks">Understanding Nginx Server and Location Block Selection Algorithms</a>, <a href="http://blog.pixelastic.com/2013/09/27/understanding-nginx-location-blocks-rewrite-rules/">Understanding Nginx Location Blocks Rewrite Rules</a>, Nginx Reverse Proxy.
- In order to spin up a Gunicorn instance as a detached process you can use the terminal multiplexer utility tmux. Enter the command tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app' and if successful you should see no output to the screen. You can verify that the process has been created by running pgrep gunicorn to see its PID. Once you’re ready to end the process you can either run tmux a to reattach to the processes, or you can run kill <PID> to terminate the background process by ID.

Example:

<strong>Terminal 1:</strong>

