import os
import fitz
import re
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
import docx2txt

resume_headers = ["WORK EXPERIENCE", "JOB EXPERIENCE", "DUTY EXPERIENCE", "EXPERIENCE", "PROFESSIONAL EXPERIENCE",
                  "CAREER SUMMARY", "PROFESSION SUMMARY", "CAREER OBJECTIVE", "PROFESSION OBJECTIVE", "EDUCATION",
                  "TRAINING", "SCHOOLING", "Relevant Courses", "Courses", "Appropriate Courses", "SKILLS", "TOP SKILLS",
                  "TECHNICAL SKILLS", "EXPERTISE", "CERTIFICATIONS", "UNIVERSITY PROJECTS", "CERTIFICATES", "PROJECTS",
                  "ASSIGNMENTS", "OTHER", "ADDITIONAL", "ADDITIONAL INFORMATION", "CONTACT",
                  "HONORS-AWARDS", "LANGUAGES"]

job_description_headers = ["JOB DESCRIPTION", "DESIRED CANDIDATE PROFILE", "QUALIFICATIONS & EXPERIENCE",
                           "PREFERRED EXPERIENCE", "REQUIRED EXPERIENCE", "WHAT ARE WE LOOKING FOR",
                           "TECHNICAL SKILLS", "KNOWLEDGE/SKILLS", "DESIRED COMPETENCIES/SKILLS"]

resume_count = 0
jd_count = 0
clean_data_resume = [[]]
clean_data_jd = [[]]
count = 0
id_temp = 2
result = ""
table_values = []
F = []
L = []
SKILLS = []
WC = []
SC = []


# Functions for pre-processing of the data that is remove urls, punctuations, numbers etc.
def replace_sep(text):
    text = text.replace("|||", ' ')
    return text


def remove_url(text):
    text = re.sub(
        r'(([a-z]{3,6}:\/*)|(^|\s))([a-zA-Z0-9\-]+\.)+[a-z]{2,13}[\.\?\=\&\%\/\w\-\+\#\!\*\^\(\)\@]*\b([^@]|$)', '',
        text)
    return text


def remove_punct(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text


def remove_numbers(text):
    text = re.sub(r'[0-9]', '', text)
    return text


def remove_phone_numbers(text):
    text = re.sub(r'\(\d{3}\)-\d{3}-\d{4}|\d{10}', '', text)
    return text


def convert_lower(text):
    text = text.lower()
    return text


def extra(text):
    text = text.replace("  ", " ")
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'^\n', '', text)
    text = text.strip()
    return text


# Using nltk stop words to remove common words not required in processing like a, an the etc.
Stopwords = set(stopwords.words("english"))


def stop_words(text):
    tweet_tokens = word_tokenize(text)
    filtered_words = [w for w in tweet_tokens if not w in Stopwords]
    return " ".join(filtered_words)


# Applying lemmatization i.e. grouping together the words to analyze as one.
def lemmantization(text):
    tokenized_text = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(a) for a in tokenized_text])
    return text


# Doing the pre-processing of data by the functions defined above
def pre_process(text):
    text = replace_sep(text)
    text = remove_url(text)
    text = remove_punct(text)
    text = remove_numbers(text)
    text = remove_phone_numbers(text)
    text = convert_lower(text)
    text = extra(text)
    text = stop_words(text)
    text = lemmantization(text)
    return text


# Adding preprocessed data onto lists and then putting those lists into Excel
def preprocess_text_in_list(HEADER_LISTS):
    HEADER_CLEAN_LISTS = []
    for i in HEADER_LISTS:
        templist = []
        for j in i:
            text = ''.join(j)
            templist.append(pre_process(text))
        HEADER_CLEAN_LISTS.append(templist)
    return HEADER_CLEAN_LISTS


def get_file_path(x, type):
    file_name = [x]
    check_path(file_name, type)


def get_file_paths(x, type):
    file_names = x
    check_path(file_names, type)


# Detect extension of the input file
def check_path(file_name, type):
    global F, L
    files = {}

    if len(file_name) != 1:
        for i in file_name:
            path = i
            name, extension = os.path.splitext(path)
            F.append(name.split("/")[-1])
            L.append(path)
            files.update({name: extension})
    else:
        path = file_name[0]
        name, extension = os.path.splitext(path)
        F.append(name.split("/")[-1])
        L.append(path)
        files.update({name: extension})
    if type == 1:
        read_resume(files)
    elif type == 2:
        read_job_description(files)


# Read text from job description
def read_job_description(files):
    global jd_count
    jd_count = len(files)
    for i in files:
        if files.get(i) == '.txt':
            with open(i + files.get(i)) as f:
                text = f.read()
                x = text.split("\n")
                templist = []
                for j in x:
                    templist.append(j.replace(":", ""))
                maintext = [i for i in templist if i != ""]
                create_jd_dict(maintext, job_description_headers)
            f.close()
        elif files.get(i) == '.pdf':
            with fitz.open(i + files.get(i)) as f:
                pymupdf_text = ""
                for page in f:
                    pymupdf_text += page.get_text("text")
            maintext = pymupdf_text.split("\n")
            create_jd_dict(maintext, resume_headers)
        elif files.get(i) == '.docx':
            text = docx2txt.process(i + files.get(i))
            x = text.split("\n")
            templist = []
            for i in x:
                templist.append(i.replace(":", ""))
            maintext = [i for i in templist if i != ""]
            create_jd_dict(maintext, resume_headers)


# Read text from resume
def read_resume(files):
    global resume_count
    resume_count = len(files)
    for i in files:
        if files.get(i) == '.pdf':
            with fitz.open(i + files.get(i)) as f:
                pymupdf_text = ""
                for page in f:
                    pymupdf_text += page.get_text("text")
            maintext = pymupdf_text.split("\n")
            create_resume_dict(maintext, resume_headers)
        elif files.get(i) == '.docx':
            text = docx2txt.process(i + files.get(i))
            x = text.split("\n")
            templist = []
            for i in x:
                templist.append(i.replace(":", ""))
            maintext = [i for i in templist if i != ""]
            create_resume_dict(maintext, resume_headers)


# Add text between start and end of two headers onto lists
def add_val(strList, mainList, s, e):
    s1 = s + 1
    while s1 < e:
        if mainList[s1] != "":
            strList.append(mainList[s1])
        s1 += 1


# Create dictionary based on position of headers in resume
def create_resume_dict(x, resume_headers):
    global count
    dict = []
    length = len(x)
    for i in range(length):
        for j in resume_headers:
            doc = x[i].split()
            if len(doc) >= 2:
                if (str(doc[0]) + " " + str(doc[1])).lower() == j.lower():
                    temp_dict = {"text": j, "pos": i}
                    dict.append(temp_dict)
            elif x[i].lower() == j.lower():
                temp_dict = {"text": j, "pos": i}
                dict.append(temp_dict)
            if i <= length - 2:
                if (x[i] + " " + x[i + 1]).lower() == j.lower():
                    temp_dict = {"text": j, "pos": i + 2}
                    dict.append(temp_dict)
    add_resume_val_to_list(dict, x)
    if id_temp == 1:
        count += 1
        find_similar(count)


# Create dictionary based on position of headers in job description
def create_jd_dict(x, job_description_headers):
    global count
    dict = []
    length = len(x)
    for i in range(length):
        for j in job_description_headers:
            doc = x[i].split()
            if len(doc) >= 2:
                if str((str(doc[0]) + " " + str(doc[1])).lower()) in j.lower():
                    temp_dict = {"text": j, "pos": i}
                    dict.append(temp_dict)
            elif x[i].lower() == j.lower():
                temp_dict = {"text": j, "pos": i}
                dict.append(temp_dict)
            if i <= length - 2:
                if str((x[i] + " " + x[i + 1]).lower()) in j.lower():
                    temp_dict = {"text": j, "pos": i + 2}
                    dict.append(temp_dict)
    add_jd_val_to_list(dict, x)
    if id_temp == 0:
        count += 1
        find_similar(count)


# Add text under a header onto list and then on Excel - RESUME
def add_resume_val_to_list(dict, x):
    global clean_data_resume, SKILLS
    WE = []
    CS = []
    E = []
    S = []
    C = []
    P = []
    RC = []
    O = []
    length = len(dict)
    for k in range(length):
        if k != length - 1:
            s = dict[k]["pos"]
            e = dict[k + 1]["pos"]
        else:
            s = dict[k]["pos"]
            e = len(x) - 1
        header_name = dict[k]["text"]

        if header_name == "WORK EXPERIENCE" or header_name == "JOB EXPERIENCE" or header_name == "DUTY EXPERIENCE" or \
                header_name == "EXPERIENCE" or header_name == "PROFESSIONAL EXPERIENCE":
            add_val(WE, x, s, e)
        elif header_name == "CAREER SUMMARY" or header_name == "PROFESSION SUMMARY" or \
                header_name == "CAREER OBJECTIVE" or header_name == "PROFESSION OBJECTIVE":
            add_val(CS, x, s, e)
        elif header_name == "EDUCATION" or header_name == "TRAINING" or header_name == "SCHOOLING":
            add_val(E, x, s, e)
        elif header_name == "SKILLS" or header_name == "EXPERTISE" or header_name == "TECHNICAL SKILLS" or \
                header_name == "TOP SKILLS":
            add_val(S, x, s, e)
        elif header_name == "CERTIFICATIONS" or header_name == "CERTIFICATES":
            add_val(C, x, s, e)
        elif header_name == "PROJECTS" or header_name == "ASSIGNMENTS" or header_name == "UNIVERSITY PROJECTS":
            add_val(P, x, s, e)
        elif header_name == "Courses" or header_name == "Relevant Courses" or header_name == "Appropriate Courses":
            add_val(RC, x, s, e)
        elif header_name == "OTHER" or header_name == "ADDITIONAL" or header_name == "ADDITIONAL INFORMATION" or \
                header_name == "CONTACT" or header_name == "HONOR-AWARDS" or header_name == "LANGUAGES":
            add_val(O, x, s, e)

    HEADER_LISTS = [WE, CS, E, S, C, P, RC, O]

    for arr in HEADER_LISTS:
        if len(arr) > 2:
            if arr[0].lower() == arr[1].lower():
                arr[1] = ""

    clean_data_resume = []
    templist = preprocess_text_in_list(HEADER_LISTS)
    for i in templist:
        if len(i) != 0:
            clean_data_resume.append(i)

    SKILLS.append(S)

    return clean_data_resume


# Add text under a header onto list and then on Excel - JD
def add_jd_val_to_list(dict, x):
    global clean_data_jd, table_values
    JD = ["JOB DESCRIPTION"]
    S = ["DESIRED CANDIDATE PROFILE"]
    length = len(dict)
    for k in range(length):
        if k != length - 1:
            s = dict[k]["pos"]
            e = dict[k + 1]["pos"]
        else:
            s = dict[k]["pos"]
            e = len(x) - 1
        header_name = dict[k]["text"]
        if header_name == "JOB DESCRIPTION" or header_name == "QUALIFICATIONS & EXPERIENCE" or \
                header_name == "PREFERRED EXPERIENCE" or header_name == "REQUIRED EXPERIENCE" \
                or header_name == "WHAT ARE WE LOOKING FOR":
            add_val(JD, x, s, e)
        elif header_name == "TECHNICAL SKILLS" or header_name == "KNOWLEDGE/SKILLS" or \
                header_name == "DESIRED CANDIDATE PROFILE" or header_name == "DESIRED COMPETENCIES/SKILLS":
            add_val(S, x, s, e)
    HEADER_LISTS = [JD, S]

    for arr in HEADER_LISTS:
        if len(arr) > 2:
            if arr[0].lower() == arr[1].lower():
                arr[1] = ""

    clean_data_jd = []
    templist = preprocess_text_in_list(HEADER_LISTS)
    for i in templist:
        if len(i) != 0:
            clean_data_jd.append(i)

    SKILLS.append(" ")

    return clean_data_jd


# Find similar words among clusters of resume and JD
def find_similar(count):
    global result, WC, SC
    word_count = ""
    similarity_word_count = 0
    resume_word_count = 0
    jd_word_count = 0
    for i in clean_data_resume:
        for j in clean_data_jd:
            resume = []
            jd = []
            similar = []
            if len(i) != 0 and len(j) != 0:
                for x in i:
                    if str(x) != 'nan':
                        for k in x.split(" "):
                            resume_word_count += 1
                            resume.append(k)
                for y in j:
                    if str(y) != 'nan':
                        for l in y.split(" "):
                            jd_word_count += 1
                            jd.append(l)
                for i1 in range(len(resume)):
                    for j1 in range(len(jd)):
                        if str(resume[i1]) == str(jd[j1]):
                            if str(resume[i1]) not in similar:
                                similar.append(str(resume[i1]))

            similarity_word_count += len(similar)
    similarity_metric = round(similarity_word_count / resume_word_count, 4)
    word_count = f'similarity_word_count = {similarity_word_count} resume_word_count = {resume_word_count} ' \
                 f'jd_word_count = {jd_word_count}'
    WC.append(word_count)
    result += f"Similarity Score {count} : " + str(similarity_metric) + "\t" + "\n"
    SC.append(similarity_metric)


def display():
    return result


def get_Skills(S):
    temp_string = ' '.join(S)
    return temp_string


def identify(id):
    global id_temp
    id_temp = id


def show():
    global table_values
    table_values.append(F)
    table_values.append(SKILLS)
    table_values.append(WC)
    table_values.append(SC)
    table_values.append(L)
    return table_values
