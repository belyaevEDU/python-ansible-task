# belyaev.script_config docker_install Role

Role for installing Docker on Ubuntu machines.

## Requirements

No prerequisites

## Role Variables

docker_install_ubuntu_codename - the host machine's ubuntu version codename. docker's ubuntu apt repository "suite" parameter is the codename

## Example Playbook

```yaml
- name: Install docker
  hosts: vms
  roles:
    - role: belyaev.script_config.docker_install
```
