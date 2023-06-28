import subprocess

def align_reads(read1_path, read2_path, reference_genome_index, output_bam):
    sam_output = output_bam.replace('.bam', '.sam')

    # Align reads using hisat2
    hisat2_cmd = [
        'hisat2',
        '-x', reference_genome_index,
        '-1', read1_path,
        '-2', read2_path,
        '-S', sam_output
    ]
    
    try:
        subprocess.run(hisat2_cmd, check=True)
        print('Alignment with HISAT2 completed successfully!')
    except subprocess.CalledProcessError as e:
        print('Alignment with HISAT2 failed:', e)
        return
    
    # Convert SAM to sorted BAM using samtools
    bam_output = output_bam.replace('.bam', '')  # Remove .bam extension
    samtools_sort_cmd = [
        'samtools', 'sort',
        '-o', output_bam,
        '-O', 'BAM',
        sam_output
    ]
    
    try:
        subprocess.run(samtools_sort_cmd, check=True)
        print('Conversion to sorted BAM completed successfully!')
    except subprocess.CalledProcessError as e:
        print('Conversion to sorted BAM failed:', e)
        return
    
    # Index the sorted BAM file using samtools
    samtools_index_cmd = ['samtools', 'index', output_bam]
    
    try:
        subprocess.run(samtools_index_cmd, check=True)
        print('BAM indexing completed successfully!')
    except subprocess.CalledProcessError as e:
        print('BAM indexing failed:', e)
        return

# Example usage
read1_path = 'path/to/read1.fastq'
read2_path = 'path/to/read2.fastq'
reference_genome_index = 'path/to/reference_genome_index'
output_bam = 'path/to/output.bam'

align_reads(read1_path, read2_path, reference_genome_index, output_bam)
