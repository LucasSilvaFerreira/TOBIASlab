import os 
import subprocess
def run_tobias(BAM_FILE_A, BAM_FILE_B, PEAKS_USE, BAM_FILE_A_TAG_NAME, BAM_FILE_B_TAG_NAME, ANALYSIS_NAME, CORES=4, GENOME_FILE='hg19.fa', MOTIF='JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt',DEBUG=False):
  '''
    Description:
        This function will run TOBIAS on the two bam files and the peak file.
        The TOBIAS functions used will be:
            ATACorrect
            FootprintScores
            BINDetect
    Parameters:
        BAM_FILE_A: str
            The path to the first bam file.
        BAM_FILE_B: str
            The path to the second bam file.
        PEAKS_USE: str
            The path to the peak file.
        BAM_FILE_A_TAG_NAME: str
            The name of the first sample
        BAM_FILE_B_TAG_NAME: str
            The name of the second sample
        ANALYSIS_NAME : str
          a name for the out analysis ex: promoter_h1_x_h3
        CORES: int
            The number of cores to use.
        GENOME_FILE: str
            The path to the genome file. Default is hg19.fa
        MOTIF: str
            The path to the motif file. The default is JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt
        DEBUG: bool
            If true, the TOBIAS output will be printed to the screen. if false, the command will run.
    Returns:    
        None
    Example:
        run_tobias('/path/to/bam/file_A.bam',
                    '/path/to/bam/file_B.bam',
                    '/path/to/peak/file.bed',
                    'sample_A',
                    'sample_B',
                    treatment_x_control,
                     4,
                    'JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt', False)
  '''
  BAM_FILE_A_NAME = '.'.join(BAM_FILE_A.split('/')[-1].split('.')[:-1] )  
  BAM_FILE_B_NAME = '.'.join(BAM_FILE_B.split('/')[-1].split('.')[:-1]   )

  cmd = f'''

  TOBIAS ATACorrect --bam  {BAM_FILE_A} --genome hg19.fa --peaks {PEAKS_USE} --blacklist hg19-blacklist.v2.bed --outdir ATACorrect_BAM_FILE_A --cores {CORES} ;
  TOBIAS ATACorrect --bam  {BAM_FILE_B} --genome hg19.fa --peaks {PEAKS_USE} --blacklist hg19-blacklist.v2.bed --outdir ATACorrect_BAM_FILE_B --cores {CORES} ;
  TOBIAS FootprintScores --signal ATACorrect_BAM_FILE_A/{BAM_FILE_A_NAME}_corrected.bw --regions {PEAKS_USE} --output {BAM_FILE_A_TAG_NAME}_footprints.bw --cores {CORES} ;
  TOBIAS FootprintScores --signal ATACorrect_BAM_FILE_B/{BAM_FILE_B_NAME}_corrected.bw --regions {PEAKS_USE} --output {BAM_FILE_B_TAG_NAME}_footprints.bw --cores {CORES} ;
  TOBIAS BINDetect --motifs {MOTIFS} --signals {BAM_FILE_A_TAG_NAME}_footprints.bw  {BAM_FILE_B_TAG_NAME}_footprints.bw --genome hg19.fa --peaks {PEAKS_USE}  --outdir BINDetect_output_{ANALYSIS_NAME} --cond_names {BAM_FILE_A_TAG_NAME} {BAM_FILE_B_TAG_NAME} --cores {CORES}


  '''
  if DEBUG:
      print(cmd)
  else:
      print(cmd)
      # subprocess.run(cmd, shell=True)
      #!$cmd
      subprocess.run(cmd, shell=True)



def install_tobias_colab():
  '''
  Description:
      This function will install TOBIAS on a Google Colab.
      The conda install can reinitialize the environment. It can be needed run this function twice before run the pipeline
      This command will download the hg19 genome
  '''
  #execute the first time running the session
  subprocess.run('pip install -q condacolab', shell=True)
  import condacolab
  condacolab.install()
  cmd_test = '''git clone https://github.com/loosolab/TOBIAS.git; cd TOBIAS; mamba env update -n base -f tobias_env.yaml ;
  mamba install tobias -c bioconda ;
  mamba install ipykernel ;
  wget http://hgdownload.cse.ucsc.edu/goldenpath/hg19/bigZips/hg19.fa.gz ;
  gunzip -d hg19.fa.gz ;
  wget https://raw.githubusercontent.com/Boyle-Lab/Blacklist/master/lists/hg19-blacklist.v2.bed.gz ;
  gunzip -d hg19-blacklist.v2.bed.gz ;
  wget https://jaspar.genereg.net/download/data/2022/CORE/JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt '''
  subprocess.run(cmd_test, shell=True)

