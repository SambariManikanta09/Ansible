Generate the CA files on the ansible control machine 

openssl req -newkey rsa:2048 -nodes -keyout files/ca_key.pem -x509 -days 365 -out files/ca_cert.pem -subj "/C=US/ST=State/L=City/O=Organization/OU=IT/CN=CA

Generate the Nomad Encryption key 

python3 -c "import os; print(os.urandom(32).hex())" 

- paste in the groups_vars/nomad.yml file