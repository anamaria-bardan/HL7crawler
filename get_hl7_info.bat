rem @python C:\Users\Anamaria\Desktop\python_projects\hl7_parser\info_collector_from_hl7_sent_msgs.py %*
rem better add all the arguments in the bat -easier to edit
rem 							do not edit												  edit for:										file to be checked															    file to store results - do not create beforehand				   add all the HL7 fields you need separated by space
rem @python C:\Users\Anamaria\Desktop\python_projects\hl7_parser\info_collector_from_hl7_sent_msgs.py "C:\Users\Anamaria\Desktop\python_projects\hl7_parser\msg\HL7_ORDERS_PROD_hl7_target_ord1828_ORM^O01_20201101154641" C:\Users\Anamaria\Desktop\python_projects\hl7_parser\result_bat.txt PID.3 PID.5 OBR.3 ZDS.1
rem 																								dir to be checked								checking ORDERS or REPORTS  lower date range upper date range including hour result output hl7 segments
rem @python C:\Users\Anamaria\Desktop\python_projects\hl7_parser\info_collector_from_hl7_sent_msgs_v2.py C:\Users\Anamaria\Desktop\python_projects\hl7_parser\msg ORDERS 2020110114 2020110115 C:\Users\Anamaria\Desktop\python_projects\hl7_parser\result_date_range_upd.txt PID.3 PID.5 OBR.3 ZDS.1
@python C:\Users\Anamaria\Desktop\python_projects\hl7_parser\info_collector_from_hl7_sent_msgs_v2.py C:\Users\Anamaria\Desktop\python_projects\hl7_parser\msg ORDERS 2020100114 2020110115 C:\Users\Anamaria\Desktop\python_projects\hl7_parser\result_wo_lim.txt PID.3 PID.5 PID.7 OBR.3 ZDS.1


@pause
