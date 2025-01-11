# Data-Science-From-Scratch
**Repository Description**:   Notes and Python code from *Data Science From Scratch* by Joel Grus, covering foundational data science concepts and implementations.

# Installing Anaconda

Here’s a step-by-step guide to install Anaconda:

---

### **Step 1: Update System Packages**
Open a terminal and update your package lists and installed packages:
```bash
sudo apt update && sudo apt upgrade -y
```

---

### **Step 2: Download the Anaconda Installer**
1. Visit the [official Anaconda download page](https://www.anaconda.com/download/success).
2. Copy the download link for the Linux installer.

Alternatively, use `wget` to download it directly:
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2023.11-Linux-x86_64.sh
```

---

### **Step 3: Verify the Installer (Optional but Recommended)**
To ensure the file is downloaded correctly:
1. Get the SHA256 checksum from the Anaconda website for the installer version.
2. Run the following command to generate the checksum:
   ```bash
   sha256sum Anaconda3-2023.11-Linux-x86_64.sh
   ```
3. Compare the output with the checksum on the website. They should match.

---

### **Step 4: Run the Installer**
1. Start the installation process by running:
   ```bash
   bash Anaconda3-2023.11-Linux-x86_64.sh
   ```
2. Follow the prompts:
   - Press `Enter` to review the license agreement, then type `yes` to accept it.
   - Confirm the installation location or press `Enter` for the default (`~/anaconda3`).

---

### **Step 5: Initialize Anaconda**
Once installation completes, initialize Anaconda by running:
```bash
conda init
```

---

### **Step 6: Activate Changes**
Close and reopen your terminal or activate the base environment directly:
```bash
source ~/.bashrc
```

---

### **Step 7: Test Installation**
To confirm Anaconda is installed, check the version:
```bash
conda --version
```

---

### **Step 8: Update Anaconda (Optional)**
Update Anaconda to ensure you have the latest packages:
```bash
conda update -n base -c defaults conda
```

---

### **Step 9: Clean Up (Optional)**
You can delete the installer file to save space:
```bash
rm Anaconda3-2023.11-Linux-x86_64.sh
```

---

### **Optional: Prevent Auto-Activation**
If you prefer not to activate the base environment every time a terminal starts, run:
```bash
conda config --set auto_activate_base false
```

---