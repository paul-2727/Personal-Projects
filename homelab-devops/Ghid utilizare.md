# 🌐 Ghid de Utilizare - Serviciile Homelab-ului

Bine ai venit! Acesta este „cloud-ul” nostru privat. Toate datele tale sunt stocate pe serverul nostru de acasă, în siguranță, fără să fie trimise către companii mari precum Google sau Facebook. 

Mai jos găsești lista serviciilor disponibile, cum să le accesezi și câteva detalii importante.

---

## 🔐 1. Authelia (Poarta de acces)
Pentru majoritatea serviciilor, vei fi redirecționat mai întâi către pagina noastră de securitate, **Authelia**.
*   **Link:** `https://auth.cpaul.stream`
*   **Cum funcționează:** Introduci numele de utilizator și parola, iar apoi un cod de 6 cifre generat de aplicația de pe telefon (Google Authenticator / Authy). Aceasta este o măsură de securitate (2FA) care ne protejează datele.

---

## ✅ Servicii Active (Disponibile acum)

### 🔑 Vaultwarden (Manager de Parole)
*   **Link:** `https://vault.cpaul.stream`
*   **Descriere:** Un seif digital securizat (alternativă gratuită la LastPass sau 1Password). Aici poți salva toate parolele, cardurile bancare și notițele secrete. 
*   **Cum îl folosești:**
    1. Accesează link-ul și creează-ți un cont (dacă ai primit invitație).
    2. Instalează aplicația **Bitwarden** pe telefon (Android/iOS) sau extensia pe browser (Chrome/Firefox).
    3. La setările aplicației, alege opțiunea **"Self-hosted"** (Server propriu) și introdu link-ul de mai sus.
*   **⚠️ Detalii importante:** Parola ta principală (Master Password) este singura cheie către acest seif. **Dacă o uiți, nimeni (nici măcar administratorul) nu o poate recupera!** Ține-o minte sau scrie-o pe o hârtie pusă într-un loc sigur.

### 💰 Firefly III (Manager Financiar)
*   **Link:** `https://firefly.cpaul.stream`
*   **Descriere:** O aplicație pentru gestionarea bugetului personal, urmărirea cheltuielilor, facturilor și economiilor.
*   **Cum îl folosești:** Accesează link-ul, loghează-te și creează-ți conturile (ex: "Cont bancar", "Portofel"). Poți începe să adaugi cheltuieli zilnice.
*   **⚠️ Detalii importante:** Datele financiare sunt strict private și criptate.

### 🍿 Jellyfin (Server Media)
*   **Link:** `https://jellyfin.cpaul.stream`
*   **Descriere:** Netflix-ul nostru personal. Aici poți viziona filme și seriale direct din browser sau de pe televizor.
*   **Cum îl folosești:**
    1. Accesează link-ul (aici te loghezi direct cu user-ul și parola de Jellyfin primite de la administrator, nu prin Authelia).
    2. Pentru o experiență mai bună, descarcă aplicația **Jellyfin** pe Smart TV, telefon sau tabletă și conectează-te folosind același link.
*   **⚠️ Detalii importante:** Serverul are o placă video dedicată, așa că filmele vor rula fluent, fără să îți consume din bateria telefonului.

---

## 🚧 Servicii Viitoare (În curând)

### 🛡️ AdGuard Home (Blocare Reclame)
*   **Descriere:** Un scut pentru întreaga rețea de acasă. Va bloca reclamele și trackerele pentru toate dispozitivele conectate la Wi-Fi (telefoane, laptopuri, televizoare).
*   **Status:** *Se va configura în curând.* (Nu necesită aplicație separată, se setează la nivel de router).

### 🎵 Navidrome (Server de Muzică)
*   **Descriere:** Similar cu Spotify, dar cu muzica ta personală. Îți permite să asculți colecția ta de melodii de oriunde.
*   **Status:** *Planificat.*

---

## 📜 Reguli de Aur ale Homelab-ului
1.  **Nu partaja link-urile și parolele** cu persoane din afara cercului nostru.
2.  **Fii blând cu serverul.** Nu descărca fișiere imense simultan pe mai multe dispozitive.
3.  **Raportează erorile.** Dacă un site nu se încarcă sau ceva pare stricat, anunță administratorul (Paul) cu un mesaj si/sau un screenshot.

**Bine ai venit în echipaj! 🚀**
