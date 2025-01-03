from jinja2 import Template

template_content = """
[Unit]
Description=Consul Service
After=network.target

[Service]
Type=simple
User={{ consul_user }}
{% if role_type == 'client' %}
ExecStart={{ consul_install_dir }}/consul agent -config {{ consul_config_dir }}/client.hcl
{% else %}
ExecStart={{ consul_install_dir }}/consul agent -config {{ consul_config_dir }}/server.hcl
{% endif %}
Restart=on-failure

[Install]
WantedBy=multi-user.target
"""

template = Template(template_content)
rendered = template.render(
    consul_user="consul",
    role_type="client",
    consul_install_dir="/usr/local/bin",
    consul_config_dir="/etc/consul.d"
)
print(rendered)
