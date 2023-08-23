# Checklist 1

### Forensics Helps
- `iconv -t UTF-16 <file.txt>` (Returns the file in UTF-16 format)
- `xxd <file.txt>` (Returns the hex of the file)
- `xxd UTF-16 <file.txt>` (Returns the hex of the file in UTF-16 format)
- `sha256sum <file.txt>` (Returns the sha256 hash of the file)
- `file <file.txt>` (Returns the file type)
- `strings <file.txt>` (Returns the strings in the file)

### Grep Help
- `grep <string> <file.txt>` (Returns the lines with the string in the file)
- `grep -v <string> <file.txt>` (Returns the lines without the string in the file)
- `grep -i <string> <file.txt>` (Returns the lines with the string in the file, ignoring case)
- `grep -r <string> <file.txt>` (Returns the lines with the string in the file, recursively)
- `grep -w <string> <file.txt>` (Returns the lines with the string in the file, only whole words)
- `grep -A <number> <string> <file.txt>` (Returns the lines with the string in the file, with <number> lines after)

- [ ]  Screen timeout policy set to 5 minutes or less
    - Command: `gsettings set org.gnome.desktop.session idle-delay 300`
- [ ]  Automatic screen lock enabled
    - Command: `gsettings set org.gnome.desktop.screensaver lock-enabled true`
- [ ]  The system is configured to automatically check for updates
    - Command: Use GUI for auto updates
- [ ]  Disabled automatic login
    - Command: `sudo sed -i 's/AutomaticLoginEnable=True/AutomaticLoginEnable=False/' /etc/gdm3/custom.conf`
- [ ]  The root account is locked
    - Command: `sudo passwd -l root`
- [ ]  Prohibited MP3 files removed
    - Command: `locate *.mp3`
- [ ]  Uncomplicated Firewall (UFW) protection is enabled
    - Command: `sudo ufw enable`
- [ ]  NFS has been disabled or removed
    - Command: `sudo systemctl stop nfs-kernel-server nfs-server nfsdcld nfs-mountd nfs-idmapd nfs-blkmap && sudo systemctl disable nfs-kernel-server nfs-server nfsdcld nfs-mountd nfs-idmapd nfs-blkmap`
- [ ]  Nginx has been disabled or removed
    - Command: `sudo systemctl stop nginx && sudo systemctl disable nginx`
- [ ]  Apache service is enabled
    - Command: `sudo systemctl enable apache2`
- [ ]  The UFW application profile for Apache has been configured as "Apache Secure"
    - Command:
        
        ```bash
        sudo ufw app update Apache
        sudo ufw allow 'Apache Secure'
        ```
        
- [ ]  SSH Server is started
    - Command: `sudo systemctl start ssh && sudo systemctl enable ssh`
- [ ]  Removed insecure sudoers rule
    - Command: `sudo vim /etc/sudoers` (remove any `ALL=(ALL:ALL) NOPASSWD: ALL` lines)
- [ ]  IPv4 TIME-WAIT ASSASSINATION protection enabled
    - Command: `echo "net.ipv4.tcp_rfc1337 = 1" | sudo tee -a /etc/sysctl.conf`
- [ ]  IPv4 TCP SYN cookies are enabled
    - Command: `echo "net.ipv4.tcp_syncookies = 1" | sudo tee -a /etc/sysctl.conf`
- [ ]  IPv4 forwarding has been disabled
    - Command: `sudo sysctl -w net.ipv4.ip_forward=0`
- [ ]  IPv4 source routing is disabled
    - Command:
        
        ```bash
        echo "net.ipv4.conf.all.send_redirects = 0" | sudo tee -a /etc/sysctl.conf
        echo "net.ipv4.conf.all.accept_source_route = 0" | sudo tee -a /etc/sysctl.conf
        
        ```
        
- [ ]  Martian packet logging is enabled
    - Command: `echo "net.ipv4.conf.all.log_martians = 1" | sudo tee -a /etc/sysctl.conf`
- [ ]  Linux kernel has been updated
    - Command: `uname -r` (Check the kernel version)
    - If update is needed do:
    
    ```bash
    sudo apt update
    sudo apt upgrade
    
    sudo apt search linux-image-generic
    sudo apt install linux-image-generic-version
    
    sudo reboot
    
    #check update
    uname -r
    ```
    
- [ ]  Source address verification enabled
    - Command:
        
        ```
        echo "net.ipv4.conf.default.rp_filter = 1" | sudo tee -a /etc/sysctl.conf
        echo "net.ipv4.conf.all.rp_filter = 1" | sudo tee -a /etc/sysctl.conf
        
        ```
        
- [ ]  ICMP redirect acceptance disabled
    - Command:
        
        ```
        echo "net.ipv4.conf.all.accept_redirects = 0" | sudo tee -a /etc/sysctl.conf
        echo "net.ipv6.conf.all.accept_redirects = 0" | sudo tee -a /etc/sysctl.conf
        
        ```
        
- [ ]  Prohibited software ophcrack has been removed
    - Command: `sudo apt-get remove ophcrack`
- [ ]  Prohibited software hydra has been removed
    - Command: `sudo apt-get remove hydra`
- [ ]  Prohibited software john the ripper has been removed
    - Command: `sudo apt-get remove john`
- [ ]  Prohibited software nmap has been removed
    - Command: `sudo apt-get remove nmap`
- [ ]  Prohibited software snort has been removed
    - Command: `sudo apt-get remove snort`
- [ ]  Prohibited software wireshark has been removed
    - Command: `sudo apt-get remove wireshark`
- [ ]  Block dangerous and deceptive content enabled in Firefox
    - Command: Open Firefox and edit its settings
- [ ]  SSH root login has been disabled
    - Command: `sudo vim /etc/ssh/sshd_config` (set "PermitRootLogin no")
- [ ]  SSH does not permit empty passwords
    - Command: `sudo vim /etc/ssh/sshd_config` (set "PermitEmptyPasswords no")
- [ ]  APT secure repository checks enabled
    - Command: (Ensure secure sources.list configuration) — Run Script
- [ ]  Malicious script 'sabotage' removed
    - Command: `rm /lib/.core/sabotage`
    - Tips for finding:
    
    ```bash
    # Check Running processes
    ps aux
    # Sort by ports
    netstat -lpeanut
    # View installed packages
    dpkg -l
    # Read Syslog
    tail -n 50 /var/log/syslog
    # Check Auths
    tail -n 50 /var/log/auth.log
    # Check Webserver
    tail -n 50 /var/log/apache2/access.log
    tail -n 50 /var/log/apache2/error.log
    # Use Anti Virus
    sudo apt install clamav
    clamscan -r /
    # View Services
    systemctl list-units --type=service
    # VIew Chron Jobs
    crontab -l
    # Use tripwire to monitor files
    sudo apt install tripwire
    # Odd file perms
    ls -l /path/to/file
    ```
- [ ]  Malicious PAM backdoor removed
    - Command: `sudo vim /etc/pam.d/common-auth` (Edit the file and remove suspicious entry)
- [ ]  Account lockout policy configured
    - Command: `sudo vim /etc/pam.d/common-auth` (Edit the file and configure faillock)
- [ ]  A secure maximum password age has been set
    - Command: `sudo vim /etc/login.defs` (Edit the file and set PASS_MAX_DAYS)
- [ ]  A secure minimum password age has been set
    - Command: `sudo vim /etc/login.defs` (Edit the file and set PASS_MIN_DAYS)
- [ ]  A minimum password length has been set
    - Command: `sudo vim /etc/security/pwquality.conf` (Edit the file and set minlen)
- [ ]  Password credit complexity checks added
    - Command: `sudo vim /etc/security/pwquality.conf` (Edit the file and set credit values)
- [ ]  Password dictionary check enabled
    - Command: `sudo vim /etc/security/pwquality.conf` (Edit the file and set dictcheck)
- [ ]  Password username check enabled
    - Command: `sudo vim /etc/security/pwquality.conf` (Edit the file and set usercheck)
- [ ]  Password encryption method set to SHA512
    - Command: `sudo vim /etc/login.defs` (Edit the file and set ENCRYPT_METHOD)
- [ ]  A secure number of login retries is configured
    - Command: `sudo vim /etc/login.defs` (Edit the file and set LOGIN_RETRIES)
- [ ]  A secure password history policy is configured
    - Command: `sudo vim /etc/pam.d/common-password` (Edit the file and configure pam_unix)
- [ ]  Removed unauthorized program Google Chrome
    - Command: `sudo apt-get remove google-chrome-stable`
- [ ]  GRUB signature checks enabled
    - Command: `sudo vim /etc/grub.d/40_custom` (Edit the file and add check_signatures)
- [ ]  Unauthorized superuser wheatley removed from GRUB
    - Command: `sudo vim /etc/grub.d/40_custom` (Edit the file and remove wheatley password)
- [ ]  /etc/shadow is not world-readable
    - Command: `chmod 600 /etc/shadow`
- [ ]  /etc/passwd is not world-writable
    - Command: `chmod 600 /etc/passwd`
- [ ]  cp is not a SUID binary
    - Command: `chmod chmod 4755 /bin/cp /usr/bin/cp`
- [ ]  Removed insecure /etc/hosts entries
    - Command: `sudo vim /etc/hosts` (Edit the file and remove insecure entries)
