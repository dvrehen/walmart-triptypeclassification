import pandas as pd
pd.set_option('max_rows', 10)

#pdf = pd.pivot_table(df, values=['ScanCount', 'AggCount'], index=['TripType', 'VisitNumber', 'Weekday', 'Weekend'],
#                 columns=['FinelineNumber'], aggfunc=np.sum)

#pdf = pd.get_dummies(df, columns = ['Weekday', 'DepartmentID', 'DepartmentID', 'FinelineNumber', 'FinelineNumber'], sparse = True)

ls_departmentid = list(df_departmentid.ID)
ls_finelinenumberid = list(df_finelinenumberid.ID)
ls_upcprefix = list(df_upcprefix.ID)

import numpy as np
import scipy.sparse as sp

m_departmentid = sp.csr_matrix((list(df.ScanCount), (df.index, df.DepartmentID - 1)),
                            shape=(len(df.index), len(ls_departmentid)))
 
m_departmentid2 = sp.csr_matrix((list(df.RelativeScanCount), (df.index, df.DepartmentID - 1)),
                            shape=(len(df.index), len(ls_departmentid)))

m_finelinenumberid = sp.csr_matrix((list(df.ScanCount), (df.index, df.FinelineNumberID - 1)),
                            shape=(len(df.index), len(ls_finelinenumberid)))

m_finelinenumberid2 = sp.csr_matrix((list(df.RelativeScanCount), (df.index, df.FinelineNumberID - 1)),
                            shape=(len(df.index), len(ls_finelinenumberid)))

m_upcprefix = sp.csr_matrix((list(df.ScanCount), (df.index, df.UPCCompanyID - 1)),
                            shape=(len(df.index), len(ls_upcprefix)))

m_upcprefix2 = sp.csr_matrix((list(df.RelativeScanCount), (df.index, df.UPCCompanyID - 1)),
                            shape=(len(df.index), len(ls_upcprefix)))


m_df = sp.hstack((m_departmentid, m_departmentid2, m_finelinenumberid, m_finelinenumberid2, m_upcprefix, m_upcprefix2), format='csr')


import itertools
import operator

agg_m_df = None
agg_df = pd.DataFrame()

for visitnumber, group_idx in itertools.groupby(enumerate(df.VisitNumber), key=operator.itemgetter(1)):
    idx = [x[0] for x in list(group_idx)] # Convert to list of group_idxs
    
    print idx[0]
    
    #m_df[idx]
#    sp.
#    m_df[0] + m_df[1]
    agg_df = agg_df.append(df.loc[idx[0]])
    summed_row = list(sum(column) for column in zip(*m_df[idx]))
    
    if agg_m_df is None:
        agg_m_df = sp.csr_matrix(summed_row[0])
    else:
        agg_m_df = sp.vstack((agg_m_df, summed_row[0]), format='csr')
    
    #print visitnumber, a
    #print m_df[idx]
    #print [sum(column) for column in zip(*m_df[idx])]



eval_df = sp.hstack((sp.csr_matrix(agg_df[["TripType", "VisitNumber","Weekday_1", "Weekday_2","Weekday_3","Weekday_4","Weekday_5","Weekday_6","Weekday_7","Weekend", "VisitScanCount"]]), agg_m_df), format = 'csr')
#final_df = sp.hstack((sp.csr_matrix(agg_df[["TripType", "VisitNumber","Weekday", "Weekend"]]), agg_m_df), format = 'csr')


#pdf = pd.get_dummies(df, columns = ['FinelineNumber'], sparse = True)