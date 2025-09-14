# 3x-ui-ansible

This repo based on [gitlab/hcsweet/3x-ui-ansible](https://gitlab.com/hcsweet/3x-ui-ansible)

## General Info

This is an ansible configuration for quick 3x-ui installation.

### Important notes

* It will block root password access to your server, use ssh keys

### Features

* quick and easy to use
* HTTPS support with cert autorenewal
* secure default setup

### What docker images are used

* [3x-ui](https://github.com/MHSanaei/3x-ui)
* [caddy-docker-proxy](https://github.com/lucaslorentz/caddy-docker-proxy)

## How to use

### General requirements

* domain name with a DNS A record

### Server requirements

* Ubuntu 22.04
* Default SSH port is 22 and it's open
* User `ansible` with full passwordless sudo
* Public SSH key is added for user `ansible`

### Commands for remote server configuration
```
sudo useradd -m -s /bin/bash ansible
sudo echo 'ansible ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/ansible
sudo mkdir /home/ansible/.ssh
sudo echo 'YOUR_SSH_PUB_KEY' >> /home/ansible/.ssh/authorized_keys
sudo chown -R ansible:ansible /home/ansible/.ssh/
sudo chmod 600 /home/ansible/.ssh/authorized_keys
```

### Step by step guide to use manually

* clone the repo
* copy `ansible/inventory.example.yml` to `ansible/inventory.yml`
* update `ansible/inventory.yml`
* run deploy playbook

#### inventory.yml settings to change

* `ansible_host`
* `proxy_domain_name`
* `allowed_ip`

#### Command to run manually

```
git clone git@github.com:thunder-spb/3x-ui-ansible.git
cd ansible/
ansible-playbook --private-key ~/.ssh/ansible --inventory inventory.yml main.yml
```

### How to access the UI panel

* `http://PROXY_HOST:2053/` (accessible only from ALLOW_IP)
* `https://PROXY_DOMAIN:2020/` (accessible only from ALLOW_IP and self)

Default user:password is `admin`:`admin`.



