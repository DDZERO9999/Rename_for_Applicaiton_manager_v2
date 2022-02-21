import csv
import replace as rp
from build_list import Create_list as bl

def activate_schedule(FILE, choice):
    if choice == 'Y':
        repactive = rp.Replace(FILE, 'aw_active=N', 'aw_active=Y')
        FILE = repactive.repsingle()
        return FILE
    elif choice == 'N':
        repactive = rp.Replace(FILE, 'aw_active=Y', 'aw_active=N')
        FILE = repactive.repsingle()
        return FILE
    else:
        print('Nothing to do')
        
def update_file(string_search, string_replace, csv_file, exp_file,jobs_chk, tasks_chk, libs_chk, choice):
    #Search fro input fields
    string_search = string_search.upper()
    string_replace = string_replace.upper()
    
    #Run create_list function for replace proccess. 
    search_list = bl(string_search)
    search_list = search_list.create_list()
    replace_list = bl(string_replace)
    replace_list = replace_list.create_list()

    #Convert .csv file into lists.
    if csv_file is not None:
        with open(csv_file) as inputData:
            data = csv.reader(inputData)
            list_search_csv = [row[0] for row in data]
            inputData.seek(0)
            list_replace_csv = [row[1] for row in data]

    #Open exp_file
    with open(exp_file,"r") as FR:
        FILE = FR.read()
        
        #Rename string from input fields
        strings = rp.Replace(FILE,string_search,string_replace)
        FILE = strings.repsingle()

        #CSV

        #Update jobs and Process flow names
        if jobs_chk == 1:
            prefx_str = (' ','so_module=','so_chain_name=','so_job_descr=','CHECK M ','so_program=','so_predecessors=','so_pred_ref_names=')
            if csv_file is not None:
                for j, f in zip(list_search_csv,list_replace_csv):
                    for x in prefx_str:
                        strings = rp.Replace(FILE, (f'{x}{j} '),(f'{x}{f} '))
                        FILE = strings.repsingle()
                        strings = rp.Replace(FILE, (f'{x}{j}\n'),(f'{x}{f}\n'))
                        FILE = strings.repsingle()
                        strings = rp.Replace(FILE, (f'{j}/'),(f'{f}/'))
                        FILE = strings.repsingle()

            #Remove new line
            delnewline = rp.Replace(FILE,'\n', '~~')
            FILE = delnewline.repsingle()
            #Run list search string srch_str
            remove_strings = ('\\~~so_predecessors=', '\\~~so_pred_ref_names=')
            for x in remove_strings:
                #Remove string replace ^
                repwithcarot = rp.Replace(FILE, x, '^')
                FILE = repwithcarot.repsingle()
                #Rename ^ CSV
                if csv_file is not None:
                    for a, b in zip(list_search_csv,list_replace_csv):
                        search_csvs = bl(a)
                        search_csvs = search_csvs.create_list_2space()
                        replace_csvs = bl(b)
                        replace_csvs = replace_csvs.create_list_2space()
                        repsearchstring = rp.Replace(FILE,search_csvs,replace_csvs)
                        FILE = repsearchstring.rep()
                        search_csvs = bl(a)
                        search_csvs = search_csvs.create_list_pspace()
                        replace_csvs = bl(b)
                        replace_csvs = replace_csvs.create_list_pspace()
                        repsearchstring = rp.Replace(FILE,search_csvs,replace_csvs)
                        FILE = repsearchstring.rep()        
                        search_csvs = bl(a)
                        search_csvs = search_csvs.create_list_slash()
                        replace_csvs = bl(b)
                        replace_csvs = replace_csvs.create_list_slash()
                        repsearchstring = rp.Replace(FILE,search_csvs,replace_csvs)
                        FILE = repsearchstring.rep()        

                #Add srch_st1 back
                removecarot = rp.Replace(FILE,'^',x)
                FILE = removecarot.repsingle()
            #Add new line
            addnewline = rp.Replace(FILE,'~~', '\n')
            FILE = addnewline.repsingle()

        #Update libraries
        if libs_chk == 1:
            prefx_str = ('so_library=','CHECK L ')
            if csv_file is not None:
                for j, f in zip(list_search_csv,list_replace_csv):
                    for x in prefx_str:
                        strings = rp.Replace(FILE, (f'{x}{j} '),(f'{x}{f} '))
                        FILE = strings.repsingle()
                        strings = rp.Replace(FILE, (f'{x}{j}\n'),(f'{x}{f}\n'))
                        FILE = strings.repsingle()

        #Update Tasks/Component aliases
        if tasks_chk == 1:
            if csv_file is not None:
                for j, f in zip(list_search_csv,list_replace_csv):
                    strings = rp.Replace(FILE, (f'\'{j}\''),(f'\'{f}\''))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'/{j}\\'),(f'/{f}\\'))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'/{j}\n'),(f'/{f}\n'))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'={j}\''),(f'={f}\''))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'={j} '),(f'={f} '))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'/{j} '),(f'/{f} '))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'so_task_name={j}\n'),(f'so_task_name={f}\n'))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'=={j}\n'),(f'=={f}\n'))
                    FILE = strings.repsingle()
                    strings = rp.Replace(FILE, (f'START={j}\n'),(f'START={f}\n'))
                    FILE = strings.repsingle()

            #Remove new line
            delnewline = rp.Replace(FILE,'\n', '~~')
            FILE = delnewline.repsingle()
       
            #Perform search and replace for chains.
            remove_strings = ('\\~~DELETE=','\\~~START=', '\\~~so_predecessors=', '\\~~so_pred_ref_names=')
            #Run list search string srch_str
            for x in remove_strings:
                #Remove string replace ^
                repwithcarot = rp.Replace(FILE, x, '^')
                FILE = repwithcarot.repsingle()
                #Rename ^ CSV
                if csv_file is not None:
                    for a, b in zip(list_search_csv,list_replace_csv):
                        search_csvs = bl(a)
                        search_csvs = search_csvs.create_list_space()
                        replace_csvs = bl(b)
                        replace_csvs = replace_csvs.create_list_space()
                        repsearchstring = rp.Replace(FILE,search_csvs,replace_csvs)
                        FILE = repsearchstring.rep()
                        search_csvq = bl(a)
                        search_csvq = search_csvq.create_list_quote()
                        replace_csvq = bl(b)
                        replace_csvq = replace_csvq.create_list_quote()
                        repsearchstring = rp.Replace(FILE,search_csvq,replace_csvq)
                        FILE = repsearchstring.rep()
                        search_csvq = bl(a)
                        search_csvq = search_csvq.create_list_espace()
                        replace_csvq = bl(b)
                        replace_csvq = replace_csvq.create_list_espace()
                        repsearchstring = rp.Replace(FILE,search_csvq,replace_csvq)
                        FILE = repsearchstring.rep()

                #Add srch_st1 back
                removecarot = rp.Replace(FILE,'^',x)
                FILE = removecarot.repsingle()

            #Add new line
            addnewline = rp.Replace(FILE,'~~', '\n')
            FILE = addnewline.repsingle()

        if choice is not None:
            FILE = activate_schedule(FILE, choice)

        #Write to the file     
        with open(exp_file,"w") as F:
            F.write(FILE)
    
        complete = 'Change Complete'
        return complete
