import sys
sys.path.insert(1, snakemake.config['repodir'])
from evaluation import compute_explained_variance_ratio, compute_batch_association

import logging
logging.basicConfig(filename=snakemake.log[0],
                    level = logging.INFO)

import mudata as mu

def run_technical_evaluations(config, input_):

    # Read mudata
    mdata = mu.read(input_)

    # Compute explained variance ratio

    # Compute batch association
    compute_batch_association(mdata, n_jobs=mdata[config['prog_key']].shape[1],
                              batch_key=config['batch_key'], 
                              prog_key=config['prog_key'],
                              inplace=True)
    
    # Overwrite mudata
    # TODO: Fix formatting issues in batch storage
    # mdata.write(input_)

# Execution (assumes Snakemake)
with open(snakemake.log[0], 'a') as f:
    f.write('\nstderr:\n')
    sys.stderr = sys.stdout = f

    if __name__=='__main__':
        run_technical_evaluations(snakemake.config, 
                                  snakemake.input[0])
