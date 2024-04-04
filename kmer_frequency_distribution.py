from collections import defaultdict
import csv
import os


def read_fasta(file_path):
    headers = []
    sequences = []
    sequence = ""
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                sequence = ""
                headers.append(line[1:])  # Remove the '>' character
            else:
                sequence += line
        if sequence:
            sequences.append(sequence)
    return headers, sequences


def sanitize_filename(header):
    return header.replace('|', '_')


# Assumes that 'transcript_headers' contains the associated names for the transcripts
transcript_headers, transcripts = read_fasta('./unique_csv/mart_export_ACTB.txt')

output_directory = './isoform_specific_csv_20240404'
os.makedirs(output_directory, exist_ok=True)

kmer_length = 50
global_kmer_counts = defaultdict(int)
kmer_transcript_sets = defaultdict(set)  # Stores which transcripts contain the kmer

for isoform_index, sequence in enumerate(transcripts):
    for i in range(len(sequence) - kmer_length + 1):
        kmer = sequence[i:i + kmer_length]
        global_kmer_counts[kmer] += 1
        kmer_transcript_sets[kmer].add(isoform_index)  # Add index of transcript for the kmer

for isoform_index, header in enumerate(transcript_headers):
    output_csv_path = os.path.join(output_directory, sanitize_filename(header) + '_kmers.csv')

    with open(output_csv_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['kmer', 'Local_Frequency', 'Global_Frequency', 'Present_in_Transcripts'])

        # Local kmer occurrences for this transcript
        local_kmer_counts = defaultdict(int)

        for i in range(len(transcripts[isoform_index]) - kmer_length + 1):
            kmer = transcripts[isoform_index][i:i + kmer_length]
            local_kmer_counts[kmer] += 1

        # Write the kmers, frequencies and sets of transcripts where the kmer is present
        for kmer, local_freq in local_kmer_counts.items():
            global_freq = global_kmer_counts[kmer]
            transcripts_containing_kmer = ', '.join(transcript_headers[i] for i in kmer_transcript_sets[kmer])
            csv_writer.writerow([kmer, local_freq, global_freq, transcripts_containing_kmer])

print(f"Kmers for each transcript have been saved as CSV files in the directory: {output_directory}")
