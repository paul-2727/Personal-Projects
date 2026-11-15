# 📝 Jurnal Proiect Homelab - Update 15.11.2026

Acest document reprezintă un rezumat tehnic (runbook) al infrastructurii construite până la data de 15.11.2026.

## 🏗️ 1. Infrastructura de Bază (Proxmox)
*   **Tranziția:** Serverul fizic a fost convertit dintr-o instalare standard Debian 13 (Trixie) în Proxmox VE 9, fără acces fizic (remote).
*   **Rețea:** S-a configurat bridge-ul `vmbr0` cu IP static `192.168.1.128`. S-au reparat problemele de DNS suprascrise de Tailscale.
*   **Acces (Anti-Lockout):** 
    *   Acces principal prin **Tailscale** (Mesh VPN).
    *   Acces de urgență prin **Cloudflare Tunnel** (SSH fallback).
*   **Router (DIGI):** Am identificat că suntem în spatele unui **CGNAT** (Carrier-Grade NAT). Nu se poate face Port Forwarding. Accesul public se face exclusiv prin tuneluri outbound (Cloudflare). Am setat rezervare DHCP și am dezactivat UPnP.

## 💻 2. Mașinile Virtuale (VM-uri)
Toate VM-urile au fost create prin **Terraform** (Infrastructure as Code) folosind un template Cloud-Init.

*   **VM 100 (INFRA):** `192.168.1.100` - Rulează containerele de infrastructură.
*   **VM 101 (COMUN):** `192.168.1.101` - Zona pentru familie/prieteni.
*   **VM 102 (PERSONAL):** `192.168.1.102` - Zona privată, cu acces la GPU.
*   **Ansible:** S-a creat un playbook pentru a instala automat pachetele de bază, Docker-ul și Tailscale pe toate VM-urile (codul este urcat pe GitHub).

## 🌐 3. Servicii și Rutare (Traefik)
*   **Traefik v3.6** rulează pe VM 100 și acționează ca Reverse Proxy.
*   **Cloudflared:** Rulează în Docker pe VM 100 și expune serviciile pe internet (fără a deschide porturi în router).
*   **Rute configurate (dynamic.yml):**
    *   `auth.cpaul.stream` (Authelia - fără SSO)
    *   `vault.cpaul.stream` -> VM 101 (Vaultwarden)
    *   `firefly.cpaul.stream` -> VM 101 (Firefly III)
    *   `grafana.cpaul.stream` -> VM 100 (Grafana)
    *   `jellyfin.cpaul.stream` -> VM 102 (Jellyfin)

## 🔒 4. Securitate (SSO & 2FA)
*   **Authelia:** S-a instalat pe VM 100. Acum acționează ca un portal unic de login (SSO) cu autentificare în doi factori (2FA/TOTP) pentru toate serviciile (cu excepția Jellyfin, care folosește login-ul nativ).
*   **Middleware Traefik:** Am configurat `forwardAuth` pentru Authelia și un middleware special (`force-https`) pentru a forța antetul `X-Forwarded-Proto` și a evita buclele de redirecționare.

## 💾 5. Strategia de Backup (Restic + Backblaze B2)
*   S-a implementat un sistem automat de backup (regula 3-2-1).
*   **Restic** este configurat pe VM 100 și VM 101.
*   **Backblaze B2** (prin API-ul S3) este folosit ca storage offsite.
*   **Baze de date:** Scripturile fac un `dump` (SQLite și MariaDB) înainte de backup pentru a evita coruperea fișierelor.
*   **Automatizare:** Rulează zilnic prin `systemd timer` (păstrează 7 zilnice, 4 săptămânale, 6 lunare).
*   **⚠️ Notă critică:** Parola de criptare Restic este salvată în Vaultwarden și local.

## 🎮 6. GPU Passthrough (NVIDIA GTX 1080)
Acesta a fost cel mai complex pas. Placa video a fost izolată de host și trimisă în VM 102.
*   **BIOS:** S-a activat IOMMU (AMD-Vi), Above 4G Decoding și s-a dezactivat Secure Boot.
*   **Host:** S-au configurat modulele VFIO (`/etc/modprobe.d/vfio.conf`) și s-a blocat driverul Nouveau.
*   **VM 102:** S-a setat BIOS-ul OVMF (UEFI), mașina Q35 și s-a adăugat parametrul `x-vga=1`.
*   **Drivere:** S-au instalat driverele NVIDIA și `nvidia-container-toolkit` în VM. S-a rezolvat conflictul cu modulul `nova` (kernel 7.0+) și lipsa repository-urilor `non-free`.

## 🎬 7. Aplicații Funcționale
1.  **Vaultwarden:** Manager de parole (VM 101).
2.  **Firefly III:** Management financiar (VM 101).
3.  **Grafana + Prometheus:** Monitorizare servere (VM 100).
4.  **Jellyfin:** Server media (VM 102) - **Activează NVENC** pentru transcodare hardware folosind GPU-ul.

## 📌 TODO (Pentru următoarele sesiuni):
- [ ] Instalare **AdGuard Home** (blocare reclame la nivel de rețea).
- [ ] Configurare **AIOps (n8n)** pentru alerte și rapoarte automate.
- [ ] Hardening final: Firewall (UFW/iptables) pe host-ul Proxmox și pe VM-uri.
- [ ] Documentare completă în `README.md` pe GitHub.
