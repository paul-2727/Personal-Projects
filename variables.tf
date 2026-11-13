variable "proxmox_api_token" {
  type      = string
  sensitive = true
}

variable "proxmox_endpoint" {
  type    = string
  default = "https://100.110.249.27:8006/"
}
