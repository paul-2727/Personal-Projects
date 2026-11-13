# 🏗️ Homelab Infrastructure & DevOps Showcaseo

Acest repository demonstrează construirea și administrarea unui homelab complet, securizat și declarativ, folosind principii moderne de DevOps și Infrastructure as Code (IaC).

## 🎯 Viziunea Proiectului
Transformarea unui server fizic remote (aflat în spatele unui CGNAT) într-o platformă multi-tenant fiabilă, capabilă să găzduiască servicii pentru uz personal, cât și pentru prieteni/familie, totul în timp ce demonstrează competențe avansate de Securitate, Rețelistică și Automatizare.

## 🏛️ Arhitectura

```mermaid
graph TD
    User((Utilizator)) -->|HTTPS| CF[Cloudflare Edge]
    Admin((Admin)) -->|Mesh VPN| TS[Tailscale]

    CF -->|Secure Tunnel| CFd[Cloudflared Container]
    TS -.->|SSH / Direct| VMs

    subgraph Proxmox VE 9 [Host Proxmox VE 9]
        CFd -->|Proxy| Traefik[Traefik v3.6]

        Traefik -->|SSO Auth| Authelia[Authelia SSO + 2FA]

        subgraph VM 100 [VM 100 - INFRA]
            Authelia
            Prometheus[Prometheus]
            Grafana[Grafana]
        end

        subgraph VM 101 [VM 101 - ZONA COMUNĂ]
            Vaultwarden[Vaultwarden]
            Firefly[Firefly III]
        end

        subgraph VM 102 [VM 102 - ZONA PERSONALĂ]
            Empty[Rezervat pentru GPU Passthrough]
        end

        Traefik --> VM 100
        Traefik --> VM 101
    end
```

## 🛠️ Stack-ul Tehnologic

*   **Virtualizare:** Proxmox VE 9 (instalat remote prin conversie din Debian 13 fără acces fizic).
*   **Infrastructure as Code (IaC):** Terraform (Provider `bpg/proxmox`) pentru clonarea și provizionarea VM-urilor dintr-un template Cloud-Init.
*   **Rețelistică & Securitate:**
    *   **Cloudflare Tunnels & Zero Trust** (expunere publică securizată, ocolind CGNAT-ul).
    *   **Tailscale** (Mesh VPN pentru accesul de administrare și fallback SSH).
    *   **Authelia** (Single Sign-On, protejând toate serviciile expuse public, cu autentificare 2FA/TOTP).
*   **Reverse Proxy:** Traefik v3.6 (rutare dinamică, middleware pentru Authelia și redirectări HTTPS).
*   **Observabilitate:** Prometheus, Grafana, cAdvisor, Node Exporter (rulează în containere Docker pe VM 100).
*   **Aplicații (VM 101):** Vaultwarden (Password Manager), Firefly III (Personal Finance Manager).

## 🔒 Caracteristici Cheie (Highlights)

*   **Anti-Lockout Strategy:** Acces multi-path garantat (Tailscale SSH pentru administrare + Cloudflare Tunnel pentru acces web).
*   **Zero Trust Architecture:** Serviciile nu sunt expuse direct; toate cererile trec prin Cloudflare și sunt interceptate de Authelia (2FA).
*   **CGNAT Bypass:** Furnizorul de internet folosește Carrier-Grade NAT, astfel încât accesul public este realizat exclusiv prin tuneluri outbound.
*   **GitOps Ready:** Configurațiile serviciilor sunt izolate în containere Docker, iar infrastructura de bază este versionată prin Terraform.

## 🚀 Cum se implementează (Terraform)
*Notă: Acest repo este un showcase. Implementarea necesită un host Proxmox configurat.*

1. Clonează repository-ul.
2. Setează token-ul API Proxmox ca variabilă de mediu: 
   `export TF_VAR_proxmox_api_token="terraform@pve!provider=UUID-UL_TAU"`
3. Inițializează și aplică:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

---
*Created with ❤️ for DevOps, Automation & Security.*
