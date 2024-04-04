import pandas as pd
import subprocess

# Function to calculate GC content
def calculate_gc_content(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

# Modified MFE calculation function using RNAfold
def calculate_mfe(sequence):
    sequence = sequence.replace('T', 'U')  # Convert T to U for RNA
    try:
        process = subprocess.run(['RNAfold', '--noPS'], input=sequence, encoding='utf-8', capture_output=True, check=True)
        output = process.stdout.strip()
        mfe_line = output.splitlines()[-1]
        mfe_str = mfe_line.split()[-1]
        mfe_str = mfe_str.strip('()')
        mfe = float(mfe_str)
        return mfe
    except subprocess.CalledProcessError as exc:
        raise ValueError(f"RNAfold failed, error message: {exc.stderr}")
    except ValueError as e:
        raise ValueError(f"Error processing RNAfold output for sequence '{sequence}': {e}")

# Load the CSV file
df = pd.read_csv('./isoform_specific_csv_20240404/ACTB_ENST00000646584_kmers.csv')

# Apply GC content and MFE calculation for each kmer
df['GC_Content'] = df['kmer'].apply(calculate_gc_content)
df['MFE'] = df['kmer'].apply(calculate_mfe)

# Save the updated DataFrame to a new CSV file
df.to_csv('./isoform_specific_csv_20240404/ACTB_ENST00000646584_kmers_with_GC_and_MFE.csv', index=False)

print("Processing complete. GC content and MFE columns added.")
