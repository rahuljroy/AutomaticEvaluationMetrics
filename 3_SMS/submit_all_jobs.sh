#!/bin/bash

sbatch job_bert_sms.sh
sbatch job_bert_wms.sh
sbatch job_elmo_s+wms.sh
sbatch job_glove_sms.sh
sbatch job_glove_wms.sh
sbatch job_bert_s+wms.sh
sbatch job_elmo_sms.sh
sbatch job_elmo_wms.sh
sbatch job_glove_s+wms.sh