import pandas as pd
import numpy as np
from pandas import DataFrame


from SAS_processing import data
from bleu import BLEU


df = pd.read_csv('../data/ASAP_SAS/train.tsv', sep='\t')
n_gram = 4

reference_corpus, candidate_corpus, reference_id, candidate_id, candidate_scores, max_scores = data(df)

# Check the correctness of length
# for i in range(len(reference_corpus)):
#     print(len(reference_corpus[i]), len(candidate_corpus[i]), len(reference_id[i]), len(candidate_id[i]))

# print(reference_id[2], candidate_id[2], candidate_scores[2], max_scores)
print(BLEU(reference_corpus[2], reference_corpus[2][50], 4))

# bleu_scores = []

# for i in range(len(reference_corpus)):
#     bleu = []
#     for j in range(len(candidate_corpus[i])):
#         bleu.append(BLEU(reference_corpus[i], candidate_corpus[i][j], n_gram))
#     # print(bleu)
#     bleu_scores.append(list(bleu))

# # for i in range(len(bleu)):
# #     print(bleu[i])
# for i in range(len(reference_corpus)):
#     filename = "../results/BLEU_scores_"+"EssaySet_{}".format(i+1)+".txt"
#     with open(filename, 'w') as f:
#         f.write("candidate_id\tsimilarity\tscore\n")
#         for j in range(len(candidate_corpus[i])):
#             f.write("{0}\t{1}\t{2}\n".format(candidate_id[i][j], bleu_scores[i][j], candidate_scores[i][j]))

