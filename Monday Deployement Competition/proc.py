import os
with open(os.path.join('C:\\Users\\akhil\\Downloads\\streamlit1','Procfile'), "w") as file1:
    toFile = 'web: sh setup.sh && streamlit run Monday.py'    
    file1.write(toFile)