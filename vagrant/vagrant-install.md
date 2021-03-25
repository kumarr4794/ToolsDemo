# Install Vagrant and create ubuntu-based VM using Vagrant

Refer : https://devopscube.com/vagrant-tutorial-beginners/

Download and Install virtualbox :

> https://www.virtualbox.org/wiki/Downloads

Download Vagrant :
https://www.vagrantup.com/downloads


###Vagrant Custom Shared Folder Location :

Example : 
    config.vm.synced_folder "code/", "/app/code"`


## Custom CPU & Memory : 
 Syntax :
  ```
  config.vm.provider "virtualbox" do |vb|
            vb.memory = 2048
            vb.cpus = 1
        end
 ```

##Vagrant Provisioner : 
When you need something [commands/packages to be run inside vm during bootup/everytime]

Syntax : Exmaple of shell script config.
```
config.vm.provision "shell", inline: <<-SHELL 
    apt-get update
    apt-get install -y apache2
    service apache2 start
SHELL
```
# We can have Single and Multi VM in vagrant.

Find Vagrantfile for same /vagrant/single-vm and /vagrant/multi-vm

To ssh into the VMs, you need to use the names web and db.
```
vagrant ssh web
vagrant ssh db
```
