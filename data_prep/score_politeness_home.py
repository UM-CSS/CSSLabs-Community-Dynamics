import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas()
import ipyparallel
import os
import sys
sys.path.append('/home/jwlock/smb4k/LSA-RESEARCH04.M.STORAGE.UMICH.EDU/lsa-research04/jwlock/reddit/CSSLabs_Community_Dynamics')
sys.path.append('/home/jwlock/smb4k/LSA-RESEARCH04.M.STORAGE.UMICH.EDU/lsa-research04/jwlock/reddit/CSSLabs_Community_Dynamics/politeness')

from politeness.scripts.format_input import format_doc
from politeness.model import score

c = ipyparallel.Client()
view = c.load_balanced_view()


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def process_df(df):
    import sys
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    
    sys.path.append('/home/jwlock/smb4k/LSA-RESEARCH04.M.STORAGE.UMICH.EDU/lsa-research04/jwlock/reddit/CSSLabs_Community_Dynamics')
    sys.path.append('/home/jwlock/smb4k/LSA-RESEARCH04.M.STORAGE.UMICH.EDU/lsa-research04/jwlock/reddit/CSSLabs_Community_Dynamics/politeness')

    from politeness.scripts.format_input import format_doc
    from politeness.model import score
    
    def get_politeness(txt):
        txt = str(txt)
        ps = []
        try:
            fs = format_doc(txt)
           
            for f in fs:
                ps.append(score(f)['polite'])
        except:
            with open('errors.txt', 'a') as o:
                o.write("\nSomething's broken with this:" + txt + "\n")
        return np.mean(ps)
    
    df['politeness'] = df.body.apply(get_politeness)
        
    return df

def get_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    l = len(dirname)
    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)
    for i in range(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)
    for i in range(len(filepaths)):
        filepaths[i] = filepaths[i][0][l+1:]

    return filepaths
           
def get_jobs():
    jobs = []
    
    files = get_files_by_file_size('data/home', reverse=False)
    done = os.listdir('data')
    
    for f in files:
        if f.endswith('tsv'):
            if f in done:
                print('already finished', f)
                pass
            else:
                print('adding', f)
                tmp = {}
                tmp['file'] = '/home/jwlock/smb4k/LSA-RESEARCH04.M.STORAGE.UMICH.EDU/lsa-research04/jwlock/reddit/CSSLabs_Community_Dynamics/data/home/'+f
                tmp['subreddit'] = f[:-4]
                jobs.append(tmp)
    
    return jobs

jobs = get_jobs()

while len(jobs)>0:
    j = jobs[0]
    print('Working on', j['subreddit'])
    df = pd.read_csv(j['file'], sep='\t')
    chunks = chunker(df, 100)
    result = view.map_async(process_df, chunks)
    result.wait_interactive()
    df = pd.concat(result)
    df.to_csv('data/'+j['subreddit']+'.tsv', sep='\t', index=False)
    jobs = get_jobs()
    
print('Done!')
