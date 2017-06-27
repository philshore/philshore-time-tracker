Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 80, host:8600

  config.vm.synced_folder ".", "/home/ubuntu/src", create: true

  config.vm.provision "shell", path: "install.sh"

end

