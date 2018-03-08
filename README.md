Dealing with NTU alcohol data and get the import part

Yu-Che Lin @ National Taiwan University

Step1.

    Each fitbit has its token, use curl to get the fitbit's data
    
Step2.

    python search_step.py ${MONTH} ${TEST}  
    
Step3.

    python search_heart.py ${MONTH} ${TEST}
    
Step4.

    python boost.py ${MONTH} ${TEST}
    
Step5.

    python json_to_csv.py dataset step_${TEST}_${MONTH}.txt step_${TEST}_${MONTH}.csv 
    
Step6.
    
    python json_to_csv.py dataset heart_${TEST}_${MONTH}_concate.txt heart_${TEST}_${MONTH}.csv
    
Step7.

    python mkglobal.py ${MONTH} ${TEST}
    
Step8. 

    python global.py ${MONTH} ${TEST}
    
Step9.

    python merge.py ${step} ${heart} ${output}
