# TOBIASlab
This are simple commands  to run DE TOBIAS analysis on colab!  
Check the tobias documentation to have additional analysis using the metafiles generated on this pipeline.  

from tobiaslab import install_tobias_colab , run_tobias  



```

pip install git+https://github.com/LucasSilvaFerreira/TOBIASlab.git
```

```python
  Description:
        This function will run TOBIAS on the two bam files and the peak file.
        The TOBIAS functions used will be:
            -ATACorrect
            -FootprintScores
            -BINDetect
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
        
  ```
  ```python
  # Run this on the top of your colab.
  install_tobias_colab():
```
```

  This function will install TOBIAS on a Google Colab.
  The conda install can reinitialize the environment. It can be needed run this function twice before run the pipeline
  This command will download the hg19 genome and the hg19 regions blacklist

```  

  
  ```python
    Example:
        run_tobias('/path/to/bam/file_A.bam',
                    '/path/to/bam/file_B.bam',
                    '/path/to/peak/file.bed',
                    'sample_A',
                    'sample_B',
                    treatment_x_control,
                     4,
                    'JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt', False)
 ```
