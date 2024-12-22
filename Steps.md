Generate the CA files on the ansible control machine 
mkdir files
openssl req -newkey rsa:2048 -nodes -keyout files/ca_key.pem -x509 -days 365 -out files/ca_cert.pem -subj "/C=US/ST=State/L=City/O=Organization/OU=IT/CN=CA

Install the dependencies 
ansible-galaxy collection install ansible.posix

Refer group_vars/nomad.yml 
Generate the encryption key 
