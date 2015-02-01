# -*- mode: ruby -*-
# vi: set ft=ruby :

box_url = "/Users/stwind/temp/precise64-vanilla.box"

def provision(cfg)

  # https://github.com/mitchellh/vagrant/issues/1673
  cfg.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  cfg.vm.provision "ansible" do |ansible|
    ansible.inventory_path = "ansible/hosts/vagrant"
    ansible.playbook = "ansible/playbooks/site.yml"
    ansible.tags = ["mongodb"]
    ansible.verbose = "v"
    ansible.raw_arguments = ["--extra-vars='init_user=vagrant'",
                             "--module-path=ansible/library"]
  end

end

Vagrant.configure("2") do |config|

  config.vm.define :vagrant01 do |cfg|

    cfg.vm.hostname = "vagrant01"
    cfg.vm.box = "ubuntu"
    cfg.vm.box_url = box_url
    cfg.vm.network :private_network, :ip => "192.168.43.10"
    provision(cfg)

  end

end
