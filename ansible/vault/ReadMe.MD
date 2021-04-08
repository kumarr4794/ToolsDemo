# ANSIBLE VAULT 

Ansible Vault is feature of ansible thats enables us to keep/store sensitive data such as 
    - apikey
    - passwords
    - ssh keys etc.. instead of keeping in plaintext in roles and playbooks.
USAGE : ansible-vault [Functions] [filename.ext]
 
# Functions : 
    
 1. create : To create ansible vault file in encrypted format. USAGE:  [ansible-vault create vault-pass.yml] - set a pwd and content in file

 2. view : to view data of encrypted file. 
 USAGE:  [ansible-vault view vault-pass.yml]

 3. edit : To Edit encrypted file
 USAGE:  [ansible-vault edit vault-pass.yml] -> pwd -> edit 

 4. encrypt : To convert plain text to encrypted format.
USAGE:  [ansible-vault encrypt vault-pass.yml] -> pwd

 5. decrypt : to decrypt an encrypted file. 
USAGE:  [ansible-vault decrypt vault-pass.yml] -> pwd

# OPTIONS : 
--ask-vault-pass : To provide password while running playbook.

--vault-password-file: to pass a vault password through a file.

