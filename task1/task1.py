import os

from web_parser import spbu_get_main, spbu_get_student, spbu_get_univer,  \
					   msu_get_science, msu_get_news, msu_get_main

from docs_parser import pdf_get_lines, docx_get_lines, save_doc_as_docx

 
SPBU = "https://spbu.ru/"
MSU = "https://www.msu.ru/"


links_spbu = {
    'student' : SPBU+'studentam',
    'univer': SPBU+'universitet',
    'main' : SPBU+''
}

links_msu = {
    'main' : MSU+'',
    'science' : MSU+'science/',
    'news' : MSU+'news/25-e-zasedanie-uchenogo-soveta-mnots-mgu.html'
}


# doc to docx convert
files = os.listdir(path="./files/")
for file in files:
    filename, file_extension = os.path.splitext(file)
    if file_extension == '.doc':
        save_doc_as_docx(file)
    

# parse .docx anf .pdf
for file in files:
    filename, file_extension = os.path.splitext(file)
    if file_extension == '.pdf':
        pdf_get_lines(file)
            
    if file_extension == '.docx':
        docx_get_lines(file)


# parse web
spbu_get_main(links_spbu['main'])

spbu_get_student(links_spbu['student'])

spbu_get_univer(links_spbu['univer'])
    

msu_get_main(links_msu['main'])

msu_get_science(links_msu['science'])

msu_get_news(links_msu['news'])

print("Done")