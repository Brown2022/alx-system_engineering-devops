<h1>0x18. Webstack monitoring</h1>
<h2>Materials</h2>
[Monitoring](https://alx-intranet.hbtn.io/concepts/13)
[Server](https://alx-intranet.hbtn.io/concepts/67)
[web erver monitoring](https://www.sumologic.com/glossary/server-monitoring/)
[What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
[System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
[Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
[Module ngx_http_upstream_module](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#var_upstream_connect_time)

<h3>0. Sign up for Datadog and install datadog-agent</h3>
For this task head to [datadog](https://www.datadoghq.com/) and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.

[image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221104T111543Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=90f1a7f1743a15a407f7ab134b6ef68fb733c4a45128423d8838b41d7bbf894d)
- Sign up for Datadog - Please make sure you are using the US website of Datagog (.com)
- Install datadog-agent on web-01
- Create an application key
- Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
- Your server web-01 should be visible in Datadog under the host name XX-web-01
		- You can validate it by using this API
		- If needed, you will need to update the hostname of your server
<h3>1. Monitor some metrics</h3>
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check.](https://docs.datadoghq.com/integrations/system/)

[image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221104T111543Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=90f1a7f1743a15a407f7ab134b6ef68fb733c4a45128423d8838b41d7bbf894d)
- Set up a monitor that checks the number of read requests issued to the device per second.
- Set up a monitor that checks the number of write requests issued to the device per second.
<h3>2. Create a dashboard</h3>
Now create a dashboard with different metrics displayed in order to get a few different visualizations.

- Create a new dashboard
- Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
- Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use [Datadog’s API](https://docs.datadoghq.com/api/latest/dashboards/#get-all-dashboards)
