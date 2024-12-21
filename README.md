**`group_vars/consul.yml`**, which contains default variables for Consul's installation and configuration:

---

### `group_vars/consul.yml`

```yaml
# Consul version to install
consul_version: "1.16.0"

# Directory where the Consul binary will be installed
consul_install_dir: "/usr/local/bin"

# Directory for Consul configuration files
consul_config_dir: "/etc/consul.d"

# Consul systemd service file location
consul_service_file: "/etc/systemd/system/consul.service"

# Consul data directory for storing state
consul_data_dir: "/opt/consul/data"

# Consul user and group (created for running the service)
consul_user: "consul"
consul_group: "consul"

# Address to bind Consul to (use 0.0.0.0 to bind to all interfaces)
consul_bind_addr: "0.0.0.0"

# Consul server settings
consul_server: true
consul_bootstrap_expect: 3

# UI settings
consul_ui: true

# Retry join addresses (empty by default, to be filled with other nodes)
consul_retry_join:
  - "192.168.1.10"
  - "192.168.1.11"
  - "192.168.1.12"
```

---

## Explanation of Parameters

1. **`consul_version`**: Defines the version of Consul to download and install. You can change it to match your preferred version.
2. **`consul_install_dir`**: The directory where the Consul binary will be placed (typically `/usr/local/bin` for binaries).
3. **`consul_config_dir`**: The directory for storing Consul's configuration files (HCL format).
4. **`consul_service_file`**: Location for the systemd service unit file.
5. **`consul_data_dir`**: Directory where Consul stores its state, such as leader election and persistent cluster data.
6. **`consul_user` / `consul_group`**: Defines the system user and group under which the Consul service will run.
7. **`consul_bind_addr`**: The address that Consul binds to. Using `0.0.0.0` ensures Consul listens on all network interfaces.
8. **`consul_server`**: Specifies whether this node is a server node.
9. **`consul_bootstrap_expect`**: Number of servers to wait for in a quorum. Set to match the number of Consul server nodes.
10. **`consul_ui`**: Whether the Consul web UI should be enabled.
11. **`consul_retry_join`**: A list of other nodes to attempt to join, helping the cluster discover peers.

---
