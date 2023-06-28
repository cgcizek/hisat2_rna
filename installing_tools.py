import subprocess

def install_hisat2_samtools():
    # Install HISAT2
    hisat2_install_cmd = ['apt', 'install', '-y', 'hisat2']
    try:
        subprocess.run(hisat2_install_cmd, check=True)
        print('HISAT2 installation completed successfully!')
    except subprocess.CalledProcessError as e:
        print('HISAT2 installation failed:', e)
        return
    
    # Install SAMtools
    samtools_install_cmd = ['apt', 'install', '-y', 'samtools']
    try:
        subprocess.run(samtools_install_cmd, check=True)
        print('SAMtools installation completed successfully!')
    except subprocess.CalledProcessError as e:
        print('SAMtools installation failed:', e)
        return

# Example usage
install_hisat2_samtools()
