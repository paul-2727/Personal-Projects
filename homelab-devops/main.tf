resource "proxmox_virtual_environment_vm" "vm_101" {
  name        = "VM101-COMMON"
  description = "Zona Comuna - Family & Friends"
  tags        = ["terraform", "common"]
  node_name   = "DebianServer"
  vm_id       = 101

  clone {
    vm_id = 9000
    full  = true
  }

  scsi_hardware = "virtio-scsi-pci"

  disk {
    datastore_id = "local"
    interface    = "scsi0"
    size         = 32
  }

  cpu {
    cores = 2
    type  = "host"
  }

  memory {
    dedicated = 2048
  }

  network_device {
    bridge = "vmbr0"
    model  = "virtio"
  }

  initialization {
    datastore_id = "local"
    ip_config {
      ipv4 {
        address = "192.168.1.101/24"
        gateway = "192.168.1.1"
      }
    }
    user_account {
      keys     = [file("~/.ssh/id_ed25519.pub")]
      username = "paul"
      password = "httcv" 
    }
  }

  agent {
    enabled = false
  }

  provisioner "local-exec" {
    command = "ssh -o StrictHostKeyChecking=no root@100.110.249.27 'qm set ${self.vm_id} --boot order=scsi0'"
  }
}

resource "proxmox_virtual_environment_vm" "vm_102" {
  name        = "VM102-PERSONAL"
  description = "Zona Personala - Admin Only"
  tags        = ["terraform", "personal"]
  node_name   = "DebianServer"
  vm_id       = 102

  clone {
    vm_id = 9000
    full  = true
  }

  scsi_hardware = "virtio-scsi-pci"

  disk {
    datastore_id = "local"
    interface    = "scsi0"
    size         = 32
  }

  cpu {
    cores = 2
    type  = "host"
  }

  memory {
    dedicated = 4096
  }

  network_device {
    bridge = "vmbr0"
    model  = "virtio"
  }

  initialization {
    datastore_id = "local"
    ip_config {
      ipv4 {
        address = "192.168.1.102/24"
        gateway = "192.168.1.1"
      }
    }
    user_account {
      keys     = [file("~/.ssh/id_ed25519.pub")]
      username = "paul"
      password = "httcv" 
    }
  }

  agent {
    enabled = false
  }

  provisioner "local-exec" {
    command = "ssh -o StrictHostKeyChecking=no root@100.110.249.27 'qm set ${self.vm_id} --boot order=scsi0'"
  }
}

