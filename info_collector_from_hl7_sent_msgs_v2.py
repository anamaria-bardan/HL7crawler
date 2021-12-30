# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:22:58 2021

@author: Anamaria
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:00:19 2021

@author: Anamaria
"""

#! python3
import logging,re,sys,time,os

#from itertools import groupby, chain, dropwhile
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

#logging.disable(logging.CRITICAL)




#fcn argumnet will be a list of args
#0 elem is the program name--not needing it
#1nd should be the dir path 
#2 chars to be containe din the file name ORDERS or REPORTS or specific filter name
#3 and 4 date range
#5 output dir
# 6 and beyond HL7 segments ---try to add segments to pass 9 args
#try to request missing segments


def get_hl7_fields_content(field,msg):
    seg=field.split('.')[0] 
    seq=field.split('.')[1]
    logging.debug(seg)
    logging.debug(seq)
    field_regex=re.compile(fr'{seg}\|(.*?\|){{{int(seq)-1}}}(.*?)\|')
    logging.debug(f'{field} is  {field_regex.findall(msg)}')
    try:
        field_val=field_regex.search(msg).group(2)
        logging.debug(field_val)  
    except:
        field_val='not_found'
    return field_val

def hl7_data_collector(args):
    start_time_all = time.time()
    file_cnt=0
    file_in_scope=0
    msgs_in_scope=0
    lst=[]
    #check if input/output dirs exist
    assert os.path.isdir(r""+args[1]), 'Input directory does not exist'
    outdir='\\'.join(args[5].split('\\')[0:-1])
    assert os.path.isdir(r""+outdir), 'Output directory does not exist'  
    
    #if the output file already exists it will be appended 
    for f in sorted(os.listdir(args[1])):
        #progress counter
        file_cnt+=1
        if file_cnt%10==0:
            print(f'Iterated through {file_cnt} out of {len(os.listdir(args[1]))} files')
        #does the file contain the needed keyword? 
        if args[2] in f:        
            #print(f)
            #is it in the needed date range?
            date_regex=re.compile(r'(.*)?_(\d{14})')
            current_file_date=date_regex.search(f).group(2)
            if current_file_date>=args[3] and current_file_date<=args[4]:
                print(f'  Found file {f} in scope of the search')
                #add counter for processed files
                file_in_scope+=1
                #time the processing of a file
                start_time = time.time()
                fname=args[1]+'\\'+f
                with open(r""+fname) as f:
                    data=f.read()
                    #spliting the file into chunks based on each chunk starting with "MSH
                    msgs_list=data.split('\"MSH')
                    #default collected info MSH 6- date and MSH 9 msg id            
                    for msg in msgs_list[1:]:
                        msgs_in_scope+=1 #message counter
                        msg='MSH'+msg
                        logging.debug(msg)
                        msh_regex=re.compile(r'MSH\|(.*?\|){5}(.*?)\|(.*?\|){2}(.*?)\|')
                        date=msh_regex.search(msg).group(2)
                        msgid=msh_regex.search(msg).group(4)
                        logging.debug(date)   
                        logging.debug(msgid)  
                        custom_fields=''
                        for field in args[6:]:
                            logging.debug(field)
                            custom_fields=custom_fields+'|'+get_hl7_fields_content(field,msg)
                        lst.append(fname+'|'+msgid+'|'+date+custom_fields)
                print(f'    processed file with {len(msgs_list)} messages in {(time.time() - start_time)} seconds')
    result=open(args[5],'a')
    #adding header
    result.write('filename|msgid|msgsndtm|'+'|'.join(args[6:]))    
    result.write('\n')
    #add limit of 500GB to file
    line_cnt=0
    for i in lst:
        line_cnt+=1
        result.write(i)
        result.write('\n')
        if result.tell()>600*1024: #600kb
            print('Result file exceeds 600kb creating multiple result files')
            break
    result.close()
    fcnt=2
    while line_cnt<len(lst) and fcnt<10:
        print(f'line cnt {line_cnt}, lst {len(lst)}, fcnt {fcnt}')
        result=open(r""+args[5].split('.')[0]+'_'+str(fcnt)+'.txt','a')
        #adding header
        result.write('filename|msgid|msgsndtm|'+'|'.join(args[6:]))    
        result.write('\n')
        for i in lst[line_cnt:]:
            line_cnt+=1
            result.write(i)
            result.write('\n')
            if result.tell()>600*1024: #600kb
                break
        result.close()
        fcnt+=1
            
    print('------------------STATS------------------')
    print(f'{len(os.listdir(args[1]))} files in the input directory')
    print(f'{file_in_scope} files in scope of the search')
    print(f'{msgs_in_scope} HL7 messages in scope of the search')
    print(f'{(time.time() - start_time_all)} seconds runtime')

hl7_data_collector(sys.argv)


#tested prog with more than 9 command line args - works
#tested prog with inputting not existing input/output paths - assert error raised
#tested prog with out of range HL& fileds - eg PID.35 - no err, but takes a  lot



#limitations 
#- getting OBX.5 data
#- getting the values for fileds above 29