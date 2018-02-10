import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas()
from time import sleep
from sklearn.utils import shuffle
import ipyparallel
import os
import sys
sys.path.append('/home/jwlock/research/reddit/CSSLabs_Community_Dynamics')
sys.path.append('/home/jwlock/research/reddit/CSSLabs_Community_Dynamics/politeness')

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
    
    sys.path.append('/home/jwlock/research/reddit/CSSLabs_Community_Dynamics')
    sys.path.append('/home/jwlock/research/reddit/CSSLabs_Community_Dynamics/politeness')

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
    
    files = get_files_by_file_size('../sampled', reverse=False)
    if 'TwoXChromosomes.tsv' in files:
        files.remove('TwoXChromosomes.tsv')
        files.insert(0, 'TwoXChromosomes.tsv')
    done = os.listdir('data/politeness/')
    
    for f in files:
        if f.endswith('tsv'):
            if f in done:
                print('already finished', f)
                pass
            else:
                print('adding', f)
                tmp = {}
                tmp['file'] = '/home/jwlock/research/reddit/sampled/'+f
                tmp['subreddit'] = f[:-4]
                jobs.append(tmp)
    
    return jobs

def checkpoint(df, part):
    df.to_csv(part+'.tmp', sep='\t', index=False)
    os.rename(part+'.tmp', part)
    return
    
chunk_s = 1000
out_cols = ['politeness']
jobs = get_jobs()

while len(jobs)>0:
    j = jobs[0]
    print('Working on', j['subreddit'])
    part = 'data/politeness/'+j['subreddit']+'.part'
    l = 0
    finished = 0
    
    if os.path.isfile(part):
        print('Resuming where we left off. Reading data...')
        sys.stdout.flush()
        df = pd.read_csv(part, sep='\t')
        finished = df.politeness.count()
        print('Already finsihed', finished)
        print('Shuffling...')
        sys.stdout.flush()
        tmp = shuffle(df[pd.isna(df.politeness)])
        chunks = chunker(tmp, chunk_s)
        l = tmp.shape[0]/chunk_s
    else:
        print('No checkpoints found. Reading data...')
        sys.stdout.flush()
        df = pd.read_csv(j['file'], sep='\t', usecols=['id', 'body'])
        df.body.fillna('', inplace=True)
        for o in out_cols:
            df[o] = np.nan
        print('Shuffling...')
        sys.stdout.flush()
        chunks = chunker(shuffle(df), chunk_s)
        l = df.shape[0]/chunk_s
    
    with tqdm(total=df.shape[0]) as pbar:
        sleep(1)
        pbar.update(finished)
        sys.stdout.flush()
        result = view.map_async(process_df, chunks)
        
        for i, r in enumerate(result):
            df.update(r)
            pbar.update(chunk_s)
            sys.stdout.flush()
            if i % 10 == 0:
                checkpoint(df=df, part=part)

    df.to_csv('data/'+j['subreddit']+'.tsv', sep='\t', index=False)
    jobs = get_jobs()
    
print('Done!')