# Socks Proxy Setup

More detailed instructions for setting up the socks proxy (somewhat manually) are [here](https://github.com/department-of-veterans-affairs/va.gov-team/blob/master/platform/engineering/internal-tools.md#configure-the-socks-proxy) but you can also set it up with the config below and the `socks.sh` script in this directory. This config will only work for access from outside the VA network.

First, copy the following into your `~/.ssh/config` file:

```
## Extra VA config
### Upstream, check for updates if something isn't or stopped working
### https://github.com/department-of-veterans-affairs/devops/blob/master/ssh/config
### Access to SOCKS proxy from public internet, by way of dev jumpbox
Host socks
   HostName 172.31.2.171
   IdentityFile ~/.ssh/vetsgov_id_rsa
   IdentitiesOnly no
   ProxyCommand ssh -l dsva -A 52.222.32.121 -W %h:%p
   User socks
```

Make sure there isn't an `IdentitiesOnly yes` directive set at the top level or in a `Host *` directive in your config file - this seems to cause the proxy to fail on authentication.

Once this is saved, try the following commands:
```
$ ssh-add -K ~/.ssh/vetsgov_id_rsa
$ ssh socks -D 2001 -N
```
You may have to accept keys for servers from various IP addresses.

Once you've [confirmed the proxy works](https://github.com/department-of-veterans-affairs/va.gov-team/blob/master/platform/engineering/internal-tools.md#test-and-use-the-socks-proxy), then you can use the socks command, as follows:
```
$ ./socks.sh on  # turn on socks proxy
$ ./socks.sh     # check status
$ ./socks.sh off # turn off socks proxy
```
The script assumes you have stored your key at `~/.ssh/vetsgov_id_rsa` - if you put it elsewhere you can override the environment variable in the script before invoking it.

You'll still need to configure your browser, [details here](https://github.com/department-of-veterans-affairs/va.gov-team/blob/master/platform/engineering/internal-tools.md#chrome--firefox).
