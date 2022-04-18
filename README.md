# TOBIASlab
Run tobias pipeline on colab  
I need to fix this documentation.  


```

pip install git+https://github.com/LucasSilvaFerreira/TOBIASlab.git
```


####`run_tobias(BAM_FILE_A, BAM_FILE_B, PEAKS_USE, BAM_FILE_A_TAG_NAME, BAM_FILE_B_TAG_NAME, CORES=4, GENOME_FILE='hg19.fa', MOTIF='JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt',DEBUG=False):`

`Description:`  
This function will run TOBIAS on the two bam files and the peak file.  
The TOBIAS functions used will be:  
    -ATACorrect  
    -FootprintScores  
    -BINDetect  
`Parameters:`  
 ```BAM_FILE_A: str  
      -The path to the first bam file.  
```

 ``` BAM_FILE_B: str  
      -The path to the second bam file. 
 ```
 
```__PEAKS_USE: str__  
    -The path to the peak file.  ```
```__BAM_FILE_A_TAG_NAME: str__  
    -The name of the first sample  ```
```__BAM_FILE_B_TAG_NAME: str__ 
    -The name of the second sample  ```
```__CORES: int__   
    -The number of cores to use.  ```
```__GENOME_FILE: str__  
    -The path to the genome file. Default is hg19.fa  ```
__MOTIF: str__
    -The path to the motif file. The default is JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt  
__DEBUG: bool__  
    -If true, the TOBIAS output will be printed to the screen. if false, the command will run.  
`Returns:`     
  -None    
`Example:`    
 `run_tobias('/path/to/bam/file_A.bam',
            '/path/to/bam/file_B.bam',
            '/path/to/peak/file.bed',
            'sample_A',
            'sample_B',
             4,
            'JASPAR2022_CORE_vertebrates_non-redundant_pfms_jaspar.txt', False)`
''' 
