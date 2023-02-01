import PyPDF2
import re
import pandas as pd

def read_resume():
    file_name = input('Enter the file location with name: ')
    pdf_open = open(file_name, 'rb')
    pdf_read = PyPDF2.PdfReader(pdf_open)
    npdf = len(pdf_read.pages)

    global content_pdf
    content_pdf = ''
    for page in range(npdf):
        content_pdf += (pdf_read.pages[page]).extract_text().lower()
    content_pdf = re.sub('\n', '', content_pdf)
    content_pdf = re.sub(' ', '', content_pdf)
    return content_pdf

def skill_search():
    print('Enter each skill with a comma(,). Eg. machine learning, data science, python')
    search_keywords = input('Enter the skill to be searched: \n')
    search_keywords = re.sub(' ', '', search_keywords).lower()
    skills = re.split(',', search_keywords)
    df_skill = pd.DataFrame(skills, columns=['skill'])

    match_list = []
    for i in range(len(skills)):
        si = re.findall(skills[i], content_pdf)
        if len(si) == 0:
            match_list.append('Not Found')
        else:
            match_list.append('Found')
    df_match = pd.DataFrame(match_list, columns=['match'])

    res = pd.concat([df_skill, df_match], axis=1)

    total_skill = len(res)
    found = len(res[res['match'] == 'Found'])
    info = f'{found} skill found out of {total_skill} skills'

    print(res)
    print(info)

if __name__=='__main__':
    read_resume()
    skill_search()
