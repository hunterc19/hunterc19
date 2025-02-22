**DIY NAS Build with 10GbE (TrueNAS SCALE)**

## **Hardware Components and Costs**

|**Component**|**Selected Option**|**Price**|
|---|---|---|
|**Case**|Rosewill RSV-L4500 (4U, 15-bay)|**$150**|
|**CPU**|AMD Ryzen 7 5700G (8-core, iGPU)|**$165**|
|**Motherboard**|ASUS Pro WS X570-ACE|**$250**|
|**RAM**|Kingston KSM32ED8/16HD (32GB, 2×16GB, ECC)|**$150**|
|**Storage (HDDs)**|4×6TB Seagate IronWolf NAS (RAID-Z2)|**$500**|
|**Boot Drive**|Samsung 870 EVO (250GB SATA)|**$50**|
|**Power Supply**|Seasonic 550W 80+ Gold|**$100**|
|**Networking**|Intel X540-T2 10GbE (Dual-Port)|**$150**|

### **Total Estimated Cost: $1,515**

## **Storage Expansion Plan**

| **Stage**            | **Drives Used**               | **Storage Setup**                       | **Total Usable Storage** |
| -------------------- | ----------------------------- | --------------------------------------- | ------------------------ |
| **Initial Setup**    | **4×6TB (RAID-Z2)**           | **~12TB usable**                        | **~12TB**                |
| **First Expansion**  | **+4×6TB (New RAID-Z2 vdev)** | **Adds ~12TB usable**                   | **~24TB total**          |
| **Second Expansion** | **+4×6TB (New RAID-Z2 vdev)** | **Adds ~12TB usable**                   | **~36TB total**          |
| **Max Expansion**    | **Up to 15 total drives**     | **Can mix RAID-Z2 & Mirrors if needed** | **~42TB+ total**         |

## **Backup Strategy**

- **Plex Media Server → NAS** (Rsync/ZFS snapshots for incremental backups)
- **Windows PCs → NAS** (Windows File History, Rsync, or Veeam for full backups)
- **Macs → NAS** (Time Machine over SMB for automatic backups)
- **Future Expansion:** Add more RAID-Z2 vdevs as needed

## **Next Steps**

- Order parts and begin assembly
- Install TrueNAS SCALE and set up RAID-Z2
- Configure backups and network shares
- Expand storage as needed

_This NAS is built for long-term scalability, enterprise-grade storage reliability, and high-speed 10GbE networking._