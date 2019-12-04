# ansible-ttp
Ansible filter plugin for template text parser (TTP)

# Sample Template

- catalyst2960_template_ttp2.txt

```
<macro>
def check_port_status(data):
    if "down" in data["port_status"]:
        data["status"] = "x"
    else:
        data["status"] = "o"
    return data

def check_stp_option(data):
    if "portfast" in data["stp_option"]:
        data["portfast"] = "o"
    else:
        data["portfast"] = "x"
    return data
</macro>

<group name="l2_interfaces" exclude="ip_setting, no_ip_setting" macro="check_port_status, check_stp_option" del="port_status, stp_option">
interface {{ port_no }}
 description {{ description | ORPHRASE }}
 switchport access vlan {{ vlan | default("1") }}
 switchport trunk allowed vlan {{ vlan }}
 switchport mode {{ mode | default("access") }}
 duplex {{ duplex | default("auto") }}
 speed {{ speed | default("auto") }}
 shut{{ port_status | default("up") }}
 spanning-tree {{ stp_option | default("none") }}
 ip {{ ip_setting | ORPHRASE }}
 no ip {{ no_ip_setting | ORPHRASE }}
!{{ _end_ }}
</group>
```

# Sample Ansible Playbook

```
---

- hosts: cisco
  gather_facts: no
  connection: network_cli

  tasks:
    - name: run show command on remote devices
      ios_command:
        commands: show running-config
      register: result

    - name: display parsed output
      debug:
        msg: "{{ result.stdout[0] | parse_cli_ttp('catalyst2960_template_ttp2.txt') }}"
```

# Sample Output

```
$ ansible-playbook -i inventory_2960.ini playbook_ttp.yml

PLAY [cisco] *************************************************************************************************

TASK [run show command on remote devices] ********************************************************************
ok: [hqdist1A]

TASK [display parsed output] *********************************************************************************
ok: [hqdist1A] => {
    "msg": [
        {
            "l2_interfaces": [
                {
                    "description": "<< Connect hqdist1 and hqdist2 >>",
                    "duplex": "auto",
                    "mode": "trunk",
                    "port_no": "Port-channel1",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "1,101"
                },
                {
                    "description": "<< To hqborder1 Fa1 >>",
                    "duplex": "full",
                    "mode": "access",
                    "port_no": "FastEthernet0/1",
                    "portfast": "x",
                    "speed": "100",
                    "status": "o",
                    "vlan": "200"
                },
                {
                    "description": "<< To hqborder2 Fa1 >>",
                    "duplex": "full",
                    "mode": "access",
                    "port_no": "FastEthernet0/2",
                    "portfast": "x",
                    "speed": "100",
                    "status": "o",
                    "vlan": "202"
                },
                {
                    "description": "<< To hqaccess1 Fa0/23 >>",
                    "duplex": "full",
                    "mode": "access",
                    "port_no": "FastEthernet0/3",
                    "portfast": "x",
                    "speed": "100",
                    "status": "o",
                    "vlan": "100"
                },
                {
                    "duplex": "auto",
                    "mode": "trunk",
                    "port_no": "FastEthernet0/4",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/5",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/6",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/7",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/8",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/9",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/10",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/11",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/12",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "203"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/13",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "100"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/14",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/15",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/16",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/17",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/18",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/19",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/20",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/21",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "FastEthernet0/22",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "x",
                    "vlan": "1"
                },
                {
                    "description": "<< To hqdist2 Fa0/23 >>",
                    "duplex": "auto",
                    "mode": "trunk",
                    "port_no": "FastEthernet0/23",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "1,101"
                },
                {
                    "description": "<< To hqdist2 Fa0/24 >>",
                    "duplex": "auto",
                    "mode": "trunk",
                    "port_no": "FastEthernet0/24",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "1,101"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "GigabitEthernet0/1",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "1"
                },
                {
                    "duplex": "auto",
                    "mode": "access",
                    "port_no": "GigabitEthernet0/2",
                    "portfast": "x",
                    "speed": "auto",
                    "status": "o",
                    "vlan": "1"
                }
            ]
        }
    ]
}

PLAY RECAP ***************************************************************************************************
hqdist1A                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
